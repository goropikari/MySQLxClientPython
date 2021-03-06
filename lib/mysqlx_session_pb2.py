# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mysqlx_session.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import mysqlx_pb2 as mysqlx__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mysqlx_session.proto',
  package='Mysqlx.Session',
  syntax='proto2',
  serialized_options=b'\n\027com.mysql.cj.x.protobuf',
  serialized_pb=b'\n\x14mysqlx_session.proto\x12\x0eMysqlx.Session\x1a\x0cmysqlx.proto\"Y\n\x11\x41uthenticateStart\x12\x11\n\tmech_name\x18\x01 \x02(\t\x12\x11\n\tauth_data\x18\x02 \x01(\x0c\x12\x18\n\x10initial_response\x18\x03 \x01(\x0c:\x04\x88\xea\x30\x04\"3\n\x14\x41uthenticateContinue\x12\x11\n\tauth_data\x18\x01 \x02(\x0c:\x08\x90\xea\x30\x03\x88\xea\x30\x05\")\n\x0e\x41uthenticateOk\x12\x11\n\tauth_data\x18\x01 \x01(\x0c:\x04\x90\xea\x30\x04\"\'\n\x05Reset\x12\x18\n\tkeep_open\x18\x01 \x01(\x08:\x05\x66\x61lse:\x04\x88\xea\x30\x06\"\r\n\x05\x43lose:\x04\x88\xea\x30\x07\x42\x19\n\x17\x63om.mysql.cj.x.protobuf'
  ,
  dependencies=[mysqlx__pb2.DESCRIPTOR,])




_AUTHENTICATESTART = _descriptor.Descriptor(
  name='AuthenticateStart',
  full_name='Mysqlx.Session.AuthenticateStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mech_name', full_name='Mysqlx.Session.AuthenticateStart.mech_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth_data', full_name='Mysqlx.Session.AuthenticateStart.auth_data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_response', full_name='Mysqlx.Session.AuthenticateStart.initial_response', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\3520\004',
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=143,
)


_AUTHENTICATECONTINUE = _descriptor.Descriptor(
  name='AuthenticateContinue',
  full_name='Mysqlx.Session.AuthenticateContinue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_data', full_name='Mysqlx.Session.AuthenticateContinue.auth_data', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\220\3520\003\210\3520\005',
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=196,
)


_AUTHENTICATEOK = _descriptor.Descriptor(
  name='AuthenticateOk',
  full_name='Mysqlx.Session.AuthenticateOk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_data', full_name='Mysqlx.Session.AuthenticateOk.auth_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\220\3520\004',
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=239,
)


_RESET = _descriptor.Descriptor(
  name='Reset',
  full_name='Mysqlx.Session.Reset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keep_open', full_name='Mysqlx.Session.Reset.keep_open', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_options=b'\210\3520\006',
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=241,
  serialized_end=280,
)


_CLOSE = _descriptor.Descriptor(
  name='Close',
  full_name='Mysqlx.Session.Close',
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
  serialized_options=b'\210\3520\007',
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=295,
)

DESCRIPTOR.message_types_by_name['AuthenticateStart'] = _AUTHENTICATESTART
DESCRIPTOR.message_types_by_name['AuthenticateContinue'] = _AUTHENTICATECONTINUE
DESCRIPTOR.message_types_by_name['AuthenticateOk'] = _AUTHENTICATEOK
DESCRIPTOR.message_types_by_name['Reset'] = _RESET
DESCRIPTOR.message_types_by_name['Close'] = _CLOSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthenticateStart = _reflection.GeneratedProtocolMessageType('AuthenticateStart', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATESTART,
  '__module__' : 'mysqlx_session_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Session.AuthenticateStart)
  })
_sym_db.RegisterMessage(AuthenticateStart)

AuthenticateContinue = _reflection.GeneratedProtocolMessageType('AuthenticateContinue', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATECONTINUE,
  '__module__' : 'mysqlx_session_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Session.AuthenticateContinue)
  })
_sym_db.RegisterMessage(AuthenticateContinue)

AuthenticateOk = _reflection.GeneratedProtocolMessageType('AuthenticateOk', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATEOK,
  '__module__' : 'mysqlx_session_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Session.AuthenticateOk)
  })
_sym_db.RegisterMessage(AuthenticateOk)

Reset = _reflection.GeneratedProtocolMessageType('Reset', (_message.Message,), {
  'DESCRIPTOR' : _RESET,
  '__module__' : 'mysqlx_session_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Session.Reset)
  })
_sym_db.RegisterMessage(Reset)

Close = _reflection.GeneratedProtocolMessageType('Close', (_message.Message,), {
  'DESCRIPTOR' : _CLOSE,
  '__module__' : 'mysqlx_session_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Session.Close)
  })
_sym_db.RegisterMessage(Close)


DESCRIPTOR._options = None
_AUTHENTICATESTART._options = None
_AUTHENTICATECONTINUE._options = None
_AUTHENTICATEOK._options = None
_RESET._options = None
_CLOSE._options = None
# @@protoc_insertion_point(module_scope)
