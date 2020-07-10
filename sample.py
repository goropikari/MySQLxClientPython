host = "db"
# host = "127.0.0.1"
user = "root"
password = "test"
port = 33060

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
sock.recv(9) # notice

import mysqlx_session_pb2
import struct
# C -> S: SESS_AUTHENTICATE_START
auth = mysqlx_session_pb2.AuthenticateStart()
auth.mech_name = 'MYSQL41'
payload = auth.SerializeToString()
size = struct.pack("<I", len(payload) + 1)
SESS_AUTHENTICATE_START = 4
typ = struct.pack('B', SESS_AUTHENTICATE_START)
sock.send(size + typ + payload)


# S -> C: AuthenticateContinue
# https://github.com/mysql/mysql-server/blob/8.0/plugin/x/protocol/protobuf/mysqlx.proto#L106
# https://dev.mysql.com/doc/internals/en/x-protocol-messages-messages.html#Mysqlx.Session::AuthenticateContinue
size = sock.recv(4)
size = struct.unpack('<I', size)[0]
typ = sock.recv(1)
payload = sock.recv(size - 1)
auth_conti = mysqlx_session_pb2.AuthenticateContinue()
auth_conti.ParseFromString(payload)



# C -> S: SESS_AUTHENTICATE_CONTINUE  = 5
# HEX(SHA1(password) ^ SHA1(challenge + SHA1(SHA1(password))))
# https://github.com/mysql/mysql-server/blob/8.0/plugin/x/protocol/protobuf/mysqlx.proto#L62
from hashlib import sha1
challenge = auth_conti.auth_data
x = sha1(password.encode()).digest()
y = sha1(challenge + sha1(x).digest()).digest()
auth_data = bytes([i ^ j for i, j in zip(x,y)]).hex().encode()
# https://dev.mysql.com/doc/internals/en/x-protocol-authentication-authentication.html#x-protocol-authentication-mysql41-authentication
# The documentation says "3. C: [ authzid ] \0 authcid \0 response \0", 
# but it should be "C: [ authzid ] \00 authcid \00\2a response \00". \2a is required.
auth_data = b"\x00" + user.encode() + b"\x00\x2a" + auth_data + b"\x00"
auth_conti = mysqlx_session_pb2.AuthenticateContinue()
auth_conti.auth_data = auth_data
payload = auth_conti.SerializeToString()
size = len(payload) + 1
size = struct.pack('<I', size)
SESS_AUTHENTICATE_CONTINUE  = 5
typ = struct.pack('B', SESS_AUTHENTICATE_CONTINUE)
sock.send(size + typ + payload)


# S -> C: notice
size = sock.recv(4)
size = struct.unpack('I', size)[0] - 1
typ = sock.recv(1)
payload = sock.recv(size)
import mysqlx_notice_pb2
notice = mysqlx_notice_pb2.Frame()
notice.ParseFromString(payload)


# S -> C: SESS_AUTHENTICATE_OK = 4
# https://github.com/mysql/mysql-server/blob/8.0/plugin/x/protocol/protobuf/mysqlx.proto#L107
size = sock.recv(4)
size = struct.unpack('I', size)[0] - 1
typ = sock.recv(1)
payload = sock.recv(size)
auth_ok = mysqlx_session_pb2.AuthenticateOk()
auth_ok.ParseFromString(payload)

# C -> S: SQL_STMT_EXECUTE = 12
# https://github.com/mysql/mysql-server/blob/8.0/plugin/x/protocol/protobuf/mysqlx.proto#L66
import mysqlx_sql_pb2
stmt_execute = mysqlx_sql_pb2.StmtExecute()
stmt_execute.namespace = "sql"
stmt_execute.stmt = b"select * from foo.bar"
stmt_execute.compact_metadata = False
payload = stmt_execute.SerializeToString()
size = len(payload) + 1
size = struct.pack('<I', size)
SQL_STMT_EXECUTE = 12
typ = struct.pack('B', SQL_STMT_EXECUTE)
sock.send(size + typ + payload)


# S -> C: RESULTSET_COLUMN_META_DATA = 12
# https://github.com/mysql/mysql-server/blob/8.0/plugin/x/protocol/protobuf/mysqlx.proto#L112
import mysqlx_resultset_pb2
# id
resultset_id = mysqlx_resultset_pb2.ColumnMetaData()
size = sock.recv(4)
size = struct.unpack('I', size)[0]
typ = sock.recv(1)
payload = sock.recv(size - 1)
resultset_id.ParseFromString(payload)
print(resultset_id)

# name
resultset_name = mysqlx_resultset_pb2.ColumnMetaData()
size = sock.recv(4)
size = struct.unpack('I', size)[0]
typ = sock.recv(1)
payload = sock.recv(size - 1)
resultset_name.ParseFromString(payload)
print(resultset_name)

# RESULTSET_ROW = 13
# https://github.com/mysql/mysql-server/blob/8.0/plugin/x/protocol/protobuf/mysqlx.proto#L113
row1 = mysqlx_resultset_pb2.Row()
size = sock.recv(4)
size = struct.unpack('I', size)[0]
typ = sock.recv(1)
payload = sock.recv(size - 1)
row1.ParseFromString(payload)

row2 = mysqlx_resultset_pb2.Row()
size = sock.recv(4)
size = struct.unpack('I', size)[0]
typ = sock.recv(1)
payload = sock.recv(size - 1)
row2.ParseFromString(payload)

def rshift(val, n): return val>>n if val >= 0 else (val+0x100000000)>>n
def decode_zigzag(val): return rshift(val, 1) ^ - (val & 1)
# https://gist.github.com/mfuerstenau/ba870a29e16536fdbaba#file-zigzag-encoding-readme-L18
# https://stackoverflow.com/a/5833119
row1_id = decode_zigzag(struct.unpack('B', row1.field[0])[0])
row1_name = row1.field[1].decode('utf-8')[0:-1]
print(f"{row1_id=}, {row1_name=}")
row2_id = decode_zigzag(struct.unpack('B', row2.field[0])[0])
row2_name = row2.field[1].decode('utf-8')[0:-1]
print(f"{row2_id=}, {row2_name=}")

# RESULTSET_FETCH_DONE = 14
# https://github.com/mysql/mysql-server/blob/8.0/plugin/x/protocol/protobuf/mysqlx.proto#L114
fetch_done = mysqlx_resultset_pb2.FetchDone()
size = sock.recv(4)
size = struct.unpack('I', size)[0]
typ = sock.recv(1)
payload = sock.recv(size - 1)
fetch_done.ParseFromString(payload)


# notice
size = sock.recv(4)
size = struct.unpack('I', size)[0] - 1
typ = sock.recv(1)
payload = sock.recv(size)
notice = mysqlx_notice_pb2.Frame()
notice.ParseFromString(payload)


# SQL_STMT_EXECUTE_OK = 17
# https://github.com/mysql/mysql-server/blob/8.0/plugin/x/protocol/protobuf/mysqlx.proto#L118
size = sock.recv(4)
size = struct.unpack('I', size)[0] - 1
typ = sock.recv(1)
payload = sock.recv(size)
stmt_execute_ok = mysqlx_sql_pb2.StmtExecuteOk()
stmt_execute_ok.ParseFromString(payload)
