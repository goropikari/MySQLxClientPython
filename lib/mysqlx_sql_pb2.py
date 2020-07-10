# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mysqlx_sql.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import mysqlx_pb2 as mysqlx__pb2
import mysqlx_datatypes_pb2 as mysqlx__datatypes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mysqlx_sql.proto',
  package='Mysqlx.Sql',
  syntax='proto2',
  serialized_options=b'\n\027com.mysql.cj.x.protobuf',
  serialized_pb=b'\n\x10mysqlx_sql.proto\x12\nMysqlx.Sql\x1a\x0cmysqlx.proto\x1a\x16mysqlx_datatypes.proto\"\x7f\n\x0bStmtExecute\x12\x16\n\tnamespace\x18\x03 \x01(\t:\x03sql\x12\x0c\n\x04stmt\x18\x01 \x02(\x0c\x12#\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\x15.Mysqlx.Datatypes.Any\x12\x1f\n\x10\x63ompact_metadata\x18\x04 \x01(\x08:\x05\x66\x61lse:\x04\x88\xea\x30\x0c\"\x15\n\rStmtExecuteOk:\x04\x90\xea\x30\x11\x42\x19\n\x17\x63om.mysql.cj.x.protobuf'
  ,
  dependencies=[mysqlx__pb2.DESCRIPTOR,mysqlx__datatypes__pb2.DESCRIPTOR,])




_STMTEXECUTE = _descriptor.Descriptor(
  name='StmtExecute',
  full_name='Mysqlx.Sql.StmtExecute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='Mysqlx.Sql.StmtExecute.namespace', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"sql".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stmt', full_name='Mysqlx.Sql.StmtExecute.stmt', index=1,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='Mysqlx.Sql.StmtExecute.args', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compact_metadata', full_name='Mysqlx.Sql.StmtExecute.compact_metadata', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\3520\014',
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=197,
)


_STMTEXECUTEOK = _descriptor.Descriptor(
  name='StmtExecuteOk',
  full_name='Mysqlx.Sql.StmtExecuteOk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\220\3520\021',
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=220,
)

_STMTEXECUTE.fields_by_name['args'].message_type = mysqlx__datatypes__pb2._ANY
DESCRIPTOR.message_types_by_name['StmtExecute'] = _STMTEXECUTE
DESCRIPTOR.message_types_by_name['StmtExecuteOk'] = _STMTEXECUTEOK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StmtExecute = _reflection.GeneratedProtocolMessageType('StmtExecute', (_message.Message,), {
  'DESCRIPTOR' : _STMTEXECUTE,
  '__module__' : 'mysqlx_sql_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Sql.StmtExecute)
  })
_sym_db.RegisterMessage(StmtExecute)

StmtExecuteOk = _reflection.GeneratedProtocolMessageType('StmtExecuteOk', (_message.Message,), {
  'DESCRIPTOR' : _STMTEXECUTEOK,
  '__module__' : 'mysqlx_sql_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Sql.StmtExecuteOk)
  })
_sym_db.RegisterMessage(StmtExecuteOk)


DESCRIPTOR._options = None
_STMTEXECUTE._options = None
_STMTEXECUTEOK._options = None
# @@protoc_insertion_point(module_scope)
