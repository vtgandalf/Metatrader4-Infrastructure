# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gross_loss.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gross_loss.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10gross_loss.proto\"\x1a\n\tGrossLoss\x12\r\n\x05value\x18\x01 \x01(\x02\x62\x06proto3')
)




_GROSSLOSS = _descriptor.Descriptor(
  name='GrossLoss',
  full_name='GrossLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='GrossLoss.value', index=0,
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
  serialized_start=20,
  serialized_end=46,
)

DESCRIPTOR.message_types_by_name['GrossLoss'] = _GROSSLOSS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GrossLoss = _reflection.GeneratedProtocolMessageType('GrossLoss', (_message.Message,), {
  'DESCRIPTOR' : _GROSSLOSS,
  '__module__' : 'gross_loss_pb2'
  # @@protoc_insertion_point(class_scope:GrossLoss)
  })
_sym_db.RegisterMessage(GrossLoss)


# @@protoc_insertion_point(module_scope)
