# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mat_trend_period.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mat_trend_period.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16mat_trend_period.proto\"\x1e\n\rMATrendPeriod\x12\r\n\x05value\x18\x01 \x01(\x02\x62\x06proto3')
)




_MATRENDPERIOD = _descriptor.Descriptor(
  name='MATrendPeriod',
  full_name='MATrendPeriod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='MATrendPeriod.value', index=0,
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
  serialized_start=26,
  serialized_end=56,
)

DESCRIPTOR.message_types_by_name['MATrendPeriod'] = _MATRENDPERIOD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MATrendPeriod = _reflection.GeneratedProtocolMessageType('MATrendPeriod', (_message.Message,), {
  'DESCRIPTOR' : _MATRENDPERIOD,
  '__module__' : 'mat_trend_period_pb2'
  # @@protoc_insertion_point(class_scope:MATrendPeriod)
  })
_sym_db.RegisterMessage(MATrendPeriod)


# @@protoc_insertion_point(module_scope)
