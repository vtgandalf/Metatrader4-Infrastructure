# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: algorithm_parameters.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import lots_pb2 as lots__pb2
import take_profit_pb2 as take__profit__pb2
import trailing_stop_pb2 as trailing__stop__pb2
import macd_open_level_pb2 as macd__open__level__pb2
import mat_trend_period_pb2 as mat__trend__period__pb2
import maximum_risk_pb2 as maximum__risk__pb2
import decrease_factor_pb2 as decrease__factor__pb2
import moving_period_pb2 as moving__period__pb2
import moving_shift_pb2 as moving__shift__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='algorithm_parameters.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1a\x61lgorithm_parameters.proto\x1a\nlots.proto\x1a\x11take_profit.proto\x1a\x13trailing_stop.proto\x1a\x15macd_open_level.proto\x1a\x16mat_trend_period.proto\x1a\x12maximum_risk.proto\x1a\x15\x64\x65\x63rease_factor.proto\x1a\x13moving_period.proto\x1a\x12moving_shift.proto\"\xd3\x02\n\x13\x41lgorithmParameters\x12\x13\n\x04Lots\x18\x01 \x01(\x0b\x32\x05.Lots\x12\x1f\n\nTakeProfit\x18\x02 \x01(\x0b\x32\x0b.TakeProfit\x12#\n\x0cTrailingStop\x18\x03 \x01(\x0b\x32\r.TrailingStop\x12%\n\rMACDOpenLevel\x18\x04 \x01(\x0b\x32\x0e.MACDOpenLevel\x12&\n\x0eMATTrendPeriod\x18\x05 \x01(\x0b\x32\x0e.MATrendPeriod\x12!\n\x0bMaximumRisk\x18\x06 \x01(\x0b\x32\x0c.MaximumRisk\x12\'\n\x0e\x44\x65\x63reaseFactor\x18\x07 \x01(\x0b\x32\x0f.DecreaseFactor\x12#\n\x0cMovingPeriod\x18\x08 \x01(\x0b\x32\r.MovingPeriod\x12!\n\x0bMovingShift\x18\t \x01(\x0b\x32\x0c.MovingShiftb\x06proto3')
  ,
  dependencies=[lots__pb2.DESCRIPTOR,take__profit__pb2.DESCRIPTOR,trailing__stop__pb2.DESCRIPTOR,macd__open__level__pb2.DESCRIPTOR,mat__trend__period__pb2.DESCRIPTOR,maximum__risk__pb2.DESCRIPTOR,decrease__factor__pb2.DESCRIPTOR,moving__period__pb2.DESCRIPTOR,moving__shift__pb2.DESCRIPTOR,])




_ALGORITHMPARAMETERS = _descriptor.Descriptor(
  name='AlgorithmParameters',
  full_name='AlgorithmParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Lots', full_name='AlgorithmParameters.Lots', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TakeProfit', full_name='AlgorithmParameters.TakeProfit', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TrailingStop', full_name='AlgorithmParameters.TrailingStop', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MACDOpenLevel', full_name='AlgorithmParameters.MACDOpenLevel', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MATTrendPeriod', full_name='AlgorithmParameters.MATTrendPeriod', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MaximumRisk', full_name='AlgorithmParameters.MaximumRisk', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='DecreaseFactor', full_name='AlgorithmParameters.DecreaseFactor', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MovingPeriod', full_name='AlgorithmParameters.MovingPeriod', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MovingShift', full_name='AlgorithmParameters.MovingShift', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=214,
  serialized_end=553,
)

_ALGORITHMPARAMETERS.fields_by_name['Lots'].message_type = lots__pb2._LOTS
_ALGORITHMPARAMETERS.fields_by_name['TakeProfit'].message_type = take__profit__pb2._TAKEPROFIT
_ALGORITHMPARAMETERS.fields_by_name['TrailingStop'].message_type = trailing__stop__pb2._TRAILINGSTOP
_ALGORITHMPARAMETERS.fields_by_name['MACDOpenLevel'].message_type = macd__open__level__pb2._MACDOPENLEVEL
_ALGORITHMPARAMETERS.fields_by_name['MATTrendPeriod'].message_type = mat__trend__period__pb2._MATRENDPERIOD
_ALGORITHMPARAMETERS.fields_by_name['MaximumRisk'].message_type = maximum__risk__pb2._MAXIMUMRISK
_ALGORITHMPARAMETERS.fields_by_name['DecreaseFactor'].message_type = decrease__factor__pb2._DECREASEFACTOR
_ALGORITHMPARAMETERS.fields_by_name['MovingPeriod'].message_type = moving__period__pb2._MOVINGPERIOD
_ALGORITHMPARAMETERS.fields_by_name['MovingShift'].message_type = moving__shift__pb2._MOVINGSHIFT
DESCRIPTOR.message_types_by_name['AlgorithmParameters'] = _ALGORITHMPARAMETERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AlgorithmParameters = _reflection.GeneratedProtocolMessageType('AlgorithmParameters', (_message.Message,), {
  'DESCRIPTOR' : _ALGORITHMPARAMETERS,
  '__module__' : 'algorithm_parameters_pb2'
  # @@protoc_insertion_point(class_scope:AlgorithmParameters)
  })
_sym_db.RegisterMessage(AlgorithmParameters)


# @@protoc_insertion_point(module_scope)