# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ave_consecutive_losses.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ave_consecutive_losses.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1c\x61ve_consecutive_losses.proto\"%\n\x14\x41veConsecutiveLosses\x12\r\n\x05value\x18\x01 \x01(\x05\x62\x06proto3')
)




_AVECONSECUTIVELOSSES = _descriptor.Descriptor(
  name='AveConsecutiveLosses',
  full_name='AveConsecutiveLosses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='AveConsecutiveLosses.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=32,
  serialized_end=69,
)

DESCRIPTOR.message_types_by_name['AveConsecutiveLosses'] = _AVECONSECUTIVELOSSES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AveConsecutiveLosses = _reflection.GeneratedProtocolMessageType('AveConsecutiveLosses', (_message.Message,), {
  'DESCRIPTOR' : _AVECONSECUTIVELOSSES,
  '__module__' : 'ave_consecutive_losses_pb2'
  # @@protoc_insertion_point(class_scope:AveConsecutiveLosses)
  })
_sym_db.RegisterMessage(AveConsecutiveLosses)


# @@protoc_insertion_point(module_scope)