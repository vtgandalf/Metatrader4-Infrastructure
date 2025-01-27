# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: optimization_report.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import profit_pb2 as profit__pb2
import profit_factor_pb2 as profit__factor__pb2
import expected_payoff_pb2 as expected__payoff__pb2
import max_drawdown_pb2 as max__drawdown__pb2
import max_drawdown_rate_pb2 as max__drawdown__rate__pb2
import relative_drawdown_pb2 as relative__drawdown__pb2
import relative_drawdown_rate_pb2 as relative__drawdown__rate__pb2
import abs_drawdown_pb2 as abs__drawdown__pb2
import abs_drawdown_rate_pb2 as abs__drawdown__rate__pb2
import gross_profit_pb2 as gross__profit__pb2
import gross_loss_pb2 as gross__loss__pb2
import total_trades_pb2 as total__trades__pb2
import largest_profit_trade_pb2 as largest__profit__trade__pb2
import largest_loss_trade_pb2 as largest__loss__trade__pb2
import average_profit_trade_pb2 as average__profit__trade__pb2
import average_loss_trade_pb2 as average__loss__trade__pb2
import modeling_quality_percentage_pb2 as modeling__quality__percentage__pb2
import max_consecutive_profit_count_pb2 as max__consecutive__profit__count__pb2
import max_consecutive_profit_pb2 as max__consecutive__profit__pb2
import max_consecutive_loss_count_pb2 as max__consecutive__loss__count__pb2
import max_consecutive_loss_pb2 as max__consecutive__loss__pb2
import max_consecutive_wins_count_pb2 as max__consecutive__wins__count__pb2
import max_consecutive_wins_profit_pb2 as max__consecutive__wins__profit__pb2
import max_consecutive_losses_count_pb2 as max__consecutive__losses__count__pb2
import max_consecutive_losses_loss_pb2 as max__consecutive__losses__loss__pb2
import profit_trades_pb2 as profit__trades__pb2
import profit_trades_rate_pb2 as profit__trades__rate__pb2
import loss_trades_pb2 as loss__trades__pb2
import loss_trades_rate_pb2 as loss__trades__rate__pb2
import ave_consecutive_wins_pb2 as ave__consecutive__wins__pb2
import ave_consecutive_losses_pb2 as ave__consecutive__losses__pb2
import short_positions_pb2 as short__positions__pb2
import short_positions_rate_pb2 as short__positions__rate__pb2
import long_positions_pb2 as long__positions__pb2
import long_positions_rate_pb2 as long__positions__rate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='optimization_report.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19optimization_report.proto\x1a\x0cprofit.proto\x1a\x13profit_factor.proto\x1a\x15\x65xpected_payoff.proto\x1a\x12max_drawdown.proto\x1a\x17max_drawdown_rate.proto\x1a\x17relative_drawdown.proto\x1a\x1crelative_drawdown_rate.proto\x1a\x12\x61\x62s_drawdown.proto\x1a\x17\x61\x62s_drawdown_rate.proto\x1a\x12gross_profit.proto\x1a\x10gross_loss.proto\x1a\x12total_trades.proto\x1a\x1alargest_profit_trade.proto\x1a\x18largest_loss_trade.proto\x1a\x1a\x61verage_profit_trade.proto\x1a\x18\x61verage_loss_trade.proto\x1a!modeling_quality_percentage.proto\x1a\"max_consecutive_profit_count.proto\x1a\x1cmax_consecutive_profit.proto\x1a max_consecutive_loss_count.proto\x1a\x1amax_consecutive_loss.proto\x1a max_consecutive_wins_count.proto\x1a!max_consecutive_wins_profit.proto\x1a\"max_consecutive_losses_count.proto\x1a!max_consecutive_losses_loss.proto\x1a\x13profit_trades.proto\x1a\x18profit_trades_rate.proto\x1a\x11loss_trades.proto\x1a\x16loss_trades_rate.proto\x1a\x1a\x61ve_consecutive_wins.proto\x1a\x1c\x61ve_consecutive_losses.proto\x1a\x15short_positions.proto\x1a\x1ashort_positions_rate.proto\x1a\x14long_positions.proto\x1a\x19long_positions_rate.proto\"\x9d\r\n\x12OptimizationReport\x12\x17\n\x06profit\x18\x01 \x01(\x0b\x32\x07.Profit\x12$\n\rprofit_factor\x18\x02 \x01(\x0b\x32\r.ProfitFactor\x12(\n\x0f\x65xpected_payoff\x18\x03 \x01(\x0b\x32\x0f.ExtectedPayoff\x12\"\n\x0cmax_drawdown\x18\x04 \x01(\x0b\x32\x0c.MaxDrawDown\x12+\n\x11max_drawdown_rate\x18\x05 \x01(\x0b\x32\x10.MaxDrawDownRate\x12,\n\x11relative_drawdown\x18\x06 \x01(\x0b\x32\x11.RelativeDrawDown\x12\x35\n\x16relative_drawdown_rate\x18\x07 \x01(\x0b\x32\x15.RelativeDrawDownRate\x12\"\n\x0c\x61\x62s_drawdown\x18\x08 \x01(\x0b\x32\x0c.AbsDrawDown\x12+\n\x11\x61\x62s_drawdown_rate\x18\t \x01(\x0b\x32\x10.AbsDrawDownRate\x12\"\n\x0cgross_profit\x18\n \x01(\x0b\x32\x0c.GrossProfit\x12\x1e\n\ngross_loss\x18\x0b \x01(\x0b\x32\n.GrossLoss\x12\"\n\x0ctotal_trades\x18\x0c \x01(\x0b\x32\x0c.TotalTrades\x12\x31\n\x14largest_profit_trade\x18\r \x01(\x0b\x32\x13.LargestProfitTrade\x12-\n\x12largest_loss_trade\x18\x0e \x01(\x0b\x32\x11.LargestLossTrade\x12\x31\n\x14\x61verage_profit_trade\x18\x0f \x01(\x0b\x32\x13.AverageProfitTrade\x12-\n\x12\x61verage_loss_trade\x18\x10 \x01(\x0b\x32\x11.AverageLossTrade\x12?\n\x1bmodeling_quality_percentage\x18\x11 \x01(\x0b\x32\x1a.ModelingQualityPercentage\x12@\n\x1cmax_consecutive_profit_count\x18\x12 \x01(\x0b\x32\x1a.MaxConsecutiveProfitCount\x12\x35\n\x16max_consecutive_profit\x18\x13 \x01(\x0b\x32\x15.MaxConsecutiveProfit\x12<\n\x1amax_consecutive_loss_count\x18\x14 \x01(\x0b\x32\x18.MaxConsecutiveLossCount\x12\x31\n\x14max_consecutive_loss\x18\x15 \x01(\x0b\x32\x13.MaxConsecutiveLoss\x12<\n\x1amax_consecutive_wins_count\x18\x16 \x01(\x0b\x32\x18.MaxConsecutiveWinsCount\x12>\n\x1bmax_consecutive_wins_profit\x18\x17 \x01(\x0b\x32\x19.MaxConsecutiveWinsProfit\x12@\n\x1cmax_consecutive_losses_count\x18\x18 \x01(\x0b\x32\x1a.MaxConsecutiveLossesCount\x12>\n\x1bmax_consecutive_losses_loss\x18\x19 \x01(\x0b\x32\x19.MaxConsecutiveLossesLoss\x12$\n\rprofit_trades\x18\x1a \x01(\x0b\x32\r.ProfitTrades\x12-\n\x12profit_trades_rate\x18\x1b \x01(\x0b\x32\x11.ProfitTradesRate\x12 \n\x0bloss_trades\x18\x1c \x01(\x0b\x32\x0b.LossTrades\x12)\n\x10loss_trades_rate\x18\x1d \x01(\x0b\x32\x0f.LossTradesRate\x12\x31\n\x14\x61ve_consecutive_wins\x18\x1e \x01(\x0b\x32\x13.AveConsecutiveWins\x12\x35\n\x16\x61ve_consecutive_losses\x18\x1f \x01(\x0b\x32\x15.AveConsecutiveLosses\x12(\n\x0fshort_positions\x18  \x01(\x0b\x32\x0f.ShortPositions\x12\x31\n\x14short_positions_rate\x18! \x01(\x0b\x32\x13.ShortPositionsRate\x12&\n\x0elong_positions\x18\" \x01(\x0b\x32\x0e.LongPositions\x12/\n\x13long_positions_rate\x18# \x01(\x0b\x32\x12.LongPositionsRateb\x06proto3')
  ,
  dependencies=[profit__pb2.DESCRIPTOR,profit__factor__pb2.DESCRIPTOR,expected__payoff__pb2.DESCRIPTOR,max__drawdown__pb2.DESCRIPTOR,max__drawdown__rate__pb2.DESCRIPTOR,relative__drawdown__pb2.DESCRIPTOR,relative__drawdown__rate__pb2.DESCRIPTOR,abs__drawdown__pb2.DESCRIPTOR,abs__drawdown__rate__pb2.DESCRIPTOR,gross__profit__pb2.DESCRIPTOR,gross__loss__pb2.DESCRIPTOR,total__trades__pb2.DESCRIPTOR,largest__profit__trade__pb2.DESCRIPTOR,largest__loss__trade__pb2.DESCRIPTOR,average__profit__trade__pb2.DESCRIPTOR,average__loss__trade__pb2.DESCRIPTOR,modeling__quality__percentage__pb2.DESCRIPTOR,max__consecutive__profit__count__pb2.DESCRIPTOR,max__consecutive__profit__pb2.DESCRIPTOR,max__consecutive__loss__count__pb2.DESCRIPTOR,max__consecutive__loss__pb2.DESCRIPTOR,max__consecutive__wins__count__pb2.DESCRIPTOR,max__consecutive__wins__profit__pb2.DESCRIPTOR,max__consecutive__losses__count__pb2.DESCRIPTOR,max__consecutive__losses__loss__pb2.DESCRIPTOR,profit__trades__pb2.DESCRIPTOR,profit__trades__rate__pb2.DESCRIPTOR,loss__trades__pb2.DESCRIPTOR,loss__trades__rate__pb2.DESCRIPTOR,ave__consecutive__wins__pb2.DESCRIPTOR,ave__consecutive__losses__pb2.DESCRIPTOR,short__positions__pb2.DESCRIPTOR,short__positions__rate__pb2.DESCRIPTOR,long__positions__pb2.DESCRIPTOR,long__positions__rate__pb2.DESCRIPTOR,])




_OPTIMIZATIONREPORT = _descriptor.Descriptor(
  name='OptimizationReport',
  full_name='OptimizationReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='profit', full_name='OptimizationReport.profit', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profit_factor', full_name='OptimizationReport.profit_factor', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expected_payoff', full_name='OptimizationReport.expected_payoff', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_drawdown', full_name='OptimizationReport.max_drawdown', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_drawdown_rate', full_name='OptimizationReport.max_drawdown_rate', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relative_drawdown', full_name='OptimizationReport.relative_drawdown', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relative_drawdown_rate', full_name='OptimizationReport.relative_drawdown_rate', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abs_drawdown', full_name='OptimizationReport.abs_drawdown', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abs_drawdown_rate', full_name='OptimizationReport.abs_drawdown_rate', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gross_profit', full_name='OptimizationReport.gross_profit', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gross_loss', full_name='OptimizationReport.gross_loss', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_trades', full_name='OptimizationReport.total_trades', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='largest_profit_trade', full_name='OptimizationReport.largest_profit_trade', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='largest_loss_trade', full_name='OptimizationReport.largest_loss_trade', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='average_profit_trade', full_name='OptimizationReport.average_profit_trade', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='average_loss_trade', full_name='OptimizationReport.average_loss_trade', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modeling_quality_percentage', full_name='OptimizationReport.modeling_quality_percentage', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_consecutive_profit_count', full_name='OptimizationReport.max_consecutive_profit_count', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_consecutive_profit', full_name='OptimizationReport.max_consecutive_profit', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_consecutive_loss_count', full_name='OptimizationReport.max_consecutive_loss_count', index=19,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_consecutive_loss', full_name='OptimizationReport.max_consecutive_loss', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_consecutive_wins_count', full_name='OptimizationReport.max_consecutive_wins_count', index=21,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_consecutive_wins_profit', full_name='OptimizationReport.max_consecutive_wins_profit', index=22,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_consecutive_losses_count', full_name='OptimizationReport.max_consecutive_losses_count', index=23,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_consecutive_losses_loss', full_name='OptimizationReport.max_consecutive_losses_loss', index=24,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profit_trades', full_name='OptimizationReport.profit_trades', index=25,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profit_trades_rate', full_name='OptimizationReport.profit_trades_rate', index=26,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loss_trades', full_name='OptimizationReport.loss_trades', index=27,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loss_trades_rate', full_name='OptimizationReport.loss_trades_rate', index=28,
      number=29, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ave_consecutive_wins', full_name='OptimizationReport.ave_consecutive_wins', index=29,
      number=30, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ave_consecutive_losses', full_name='OptimizationReport.ave_consecutive_losses', index=30,
      number=31, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='short_positions', full_name='OptimizationReport.short_positions', index=31,
      number=32, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='short_positions_rate', full_name='OptimizationReport.short_positions_rate', index=32,
      number=33, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_positions', full_name='OptimizationReport.long_positions', index=33,
      number=34, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_positions_rate', full_name='OptimizationReport.long_positions_rate', index=34,
      number=35, type=11, cpp_type=10, label=1,
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
  serialized_start=950,
  serialized_end=2643,
)

_OPTIMIZATIONREPORT.fields_by_name['profit'].message_type = profit__pb2._PROFIT
_OPTIMIZATIONREPORT.fields_by_name['profit_factor'].message_type = profit__factor__pb2._PROFITFACTOR
_OPTIMIZATIONREPORT.fields_by_name['expected_payoff'].message_type = expected__payoff__pb2._EXTECTEDPAYOFF
_OPTIMIZATIONREPORT.fields_by_name['max_drawdown'].message_type = max__drawdown__pb2._MAXDRAWDOWN
_OPTIMIZATIONREPORT.fields_by_name['max_drawdown_rate'].message_type = max__drawdown__rate__pb2._MAXDRAWDOWNRATE
_OPTIMIZATIONREPORT.fields_by_name['relative_drawdown'].message_type = relative__drawdown__pb2._RELATIVEDRAWDOWN
_OPTIMIZATIONREPORT.fields_by_name['relative_drawdown_rate'].message_type = relative__drawdown__rate__pb2._RELATIVEDRAWDOWNRATE
_OPTIMIZATIONREPORT.fields_by_name['abs_drawdown'].message_type = abs__drawdown__pb2._ABSDRAWDOWN
_OPTIMIZATIONREPORT.fields_by_name['abs_drawdown_rate'].message_type = abs__drawdown__rate__pb2._ABSDRAWDOWNRATE
_OPTIMIZATIONREPORT.fields_by_name['gross_profit'].message_type = gross__profit__pb2._GROSSPROFIT
_OPTIMIZATIONREPORT.fields_by_name['gross_loss'].message_type = gross__loss__pb2._GROSSLOSS
_OPTIMIZATIONREPORT.fields_by_name['total_trades'].message_type = total__trades__pb2._TOTALTRADES
_OPTIMIZATIONREPORT.fields_by_name['largest_profit_trade'].message_type = largest__profit__trade__pb2._LARGESTPROFITTRADE
_OPTIMIZATIONREPORT.fields_by_name['largest_loss_trade'].message_type = largest__loss__trade__pb2._LARGESTLOSSTRADE
_OPTIMIZATIONREPORT.fields_by_name['average_profit_trade'].message_type = average__profit__trade__pb2._AVERAGEPROFITTRADE
_OPTIMIZATIONREPORT.fields_by_name['average_loss_trade'].message_type = average__loss__trade__pb2._AVERAGELOSSTRADE
_OPTIMIZATIONREPORT.fields_by_name['modeling_quality_percentage'].message_type = modeling__quality__percentage__pb2._MODELINGQUALITYPERCENTAGE
_OPTIMIZATIONREPORT.fields_by_name['max_consecutive_profit_count'].message_type = max__consecutive__profit__count__pb2._MAXCONSECUTIVEPROFITCOUNT
_OPTIMIZATIONREPORT.fields_by_name['max_consecutive_profit'].message_type = max__consecutive__profit__pb2._MAXCONSECUTIVEPROFIT
_OPTIMIZATIONREPORT.fields_by_name['max_consecutive_loss_count'].message_type = max__consecutive__loss__count__pb2._MAXCONSECUTIVELOSSCOUNT
_OPTIMIZATIONREPORT.fields_by_name['max_consecutive_loss'].message_type = max__consecutive__loss__pb2._MAXCONSECUTIVELOSS
_OPTIMIZATIONREPORT.fields_by_name['max_consecutive_wins_count'].message_type = max__consecutive__wins__count__pb2._MAXCONSECUTIVEWINSCOUNT
_OPTIMIZATIONREPORT.fields_by_name['max_consecutive_wins_profit'].message_type = max__consecutive__wins__profit__pb2._MAXCONSECUTIVEWINSPROFIT
_OPTIMIZATIONREPORT.fields_by_name['max_consecutive_losses_count'].message_type = max__consecutive__losses__count__pb2._MAXCONSECUTIVELOSSESCOUNT
_OPTIMIZATIONREPORT.fields_by_name['max_consecutive_losses_loss'].message_type = max__consecutive__losses__loss__pb2._MAXCONSECUTIVELOSSESLOSS
_OPTIMIZATIONREPORT.fields_by_name['profit_trades'].message_type = profit__trades__pb2._PROFITTRADES
_OPTIMIZATIONREPORT.fields_by_name['profit_trades_rate'].message_type = profit__trades__rate__pb2._PROFITTRADESRATE
_OPTIMIZATIONREPORT.fields_by_name['loss_trades'].message_type = loss__trades__pb2._LOSSTRADES
_OPTIMIZATIONREPORT.fields_by_name['loss_trades_rate'].message_type = loss__trades__rate__pb2._LOSSTRADESRATE
_OPTIMIZATIONREPORT.fields_by_name['ave_consecutive_wins'].message_type = ave__consecutive__wins__pb2._AVECONSECUTIVEWINS
_OPTIMIZATIONREPORT.fields_by_name['ave_consecutive_losses'].message_type = ave__consecutive__losses__pb2._AVECONSECUTIVELOSSES
_OPTIMIZATIONREPORT.fields_by_name['short_positions'].message_type = short__positions__pb2._SHORTPOSITIONS
_OPTIMIZATIONREPORT.fields_by_name['short_positions_rate'].message_type = short__positions__rate__pb2._SHORTPOSITIONSRATE
_OPTIMIZATIONREPORT.fields_by_name['long_positions'].message_type = long__positions__pb2._LONGPOSITIONS
_OPTIMIZATIONREPORT.fields_by_name['long_positions_rate'].message_type = long__positions__rate__pb2._LONGPOSITIONSRATE
DESCRIPTOR.message_types_by_name['OptimizationReport'] = _OPTIMIZATIONREPORT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OptimizationReport = _reflection.GeneratedProtocolMessageType('OptimizationReport', (_message.Message,), {
  'DESCRIPTOR' : _OPTIMIZATIONREPORT,
  '__module__' : 'optimization_report_pb2'
  # @@protoc_insertion_point(class_scope:OptimizationReport)
  })
_sym_db.RegisterMessage(OptimizationReport)


# @@protoc_insertion_point(module_scope)
