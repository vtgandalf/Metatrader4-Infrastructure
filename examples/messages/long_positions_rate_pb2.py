# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: long_positions_rate.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='long_positions_rate.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19long_positions_rate.proto\"\"\n\x11LongPositionsRate\x12\r\n\x05value\x18\x01 \x01(\x02\x62\x06proto3')
)




_LONGPOSITIONSRATE = _descriptor.Descriptor(
  name='LongPositionsRate',
  full_name='LongPositionsRate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='LongPositionsRate.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=63,
)

DESCRIPTOR.message_types_by_name['LongPositionsRate'] = _LONGPOSITIONSRATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LongPositionsRate = _reflection.GeneratedProtocolMessageType('LongPositionsRate', (_message.Message,), {
  'DESCRIPTOR' : _LONGPOSITIONSRATE,
  '__module__' : 'long_positions_rate_pb2'
  # @@protoc_insertion_point(class_scope:LongPositionsRate)
  })
_sym_db.RegisterMessage(LongPositionsRate)


# @@protoc_insertion_point(module_scope)