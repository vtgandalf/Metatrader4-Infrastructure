# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trailing_stop.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='trailing_stop.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13trailing_stop.proto\"\x1d\n\x0cTrailingStop\x12\r\n\x05value\x18\x01 \x01(\x02\x62\x06proto3')
)




_TRAILINGSTOP = _descriptor.Descriptor(
  name='TrailingStop',
  full_name='TrailingStop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='TrailingStop.value', index=0,
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
  serialized_start=23,
  serialized_end=52,
)

DESCRIPTOR.message_types_by_name['TrailingStop'] = _TRAILINGSTOP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrailingStop = _reflection.GeneratedProtocolMessageType('TrailingStop', (_message.Message,), {
  'DESCRIPTOR' : _TRAILINGSTOP,
  '__module__' : 'trailing_stop_pb2'
  # @@protoc_insertion_point(class_scope:TrailingStop)
  })
_sym_db.RegisterMessage(TrailingStop)


# @@protoc_insertion_point(module_scope)
