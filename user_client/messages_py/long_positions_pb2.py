# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: long_positions.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='long_positions.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14long_positions.proto\"\x1e\n\rLongPositions\x12\r\n\x05value\x18\x01 \x01(\x02\x62\x06proto3')
)




_LONGPOSITIONS = _descriptor.Descriptor(
  name='LongPositions',
  full_name='LongPositions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='LongPositions.value', index=0,
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
  serialized_start=24,
  serialized_end=54,
)

DESCRIPTOR.message_types_by_name['LongPositions'] = _LONGPOSITIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LongPositions = _reflection.GeneratedProtocolMessageType('LongPositions', (_message.Message,), {
  'DESCRIPTOR' : _LONGPOSITIONS,
  '__module__' : 'long_positions_pb2'
  # @@protoc_insertion_point(class_scope:LongPositions)
  })
_sym_db.RegisterMessage(LongPositions)


# @@protoc_insertion_point(module_scope)
