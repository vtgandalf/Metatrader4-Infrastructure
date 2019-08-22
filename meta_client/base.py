import os
import sys
sys.path.append(os.path.abspath('messages'))

import ast
import grpc
import time
import threading
import datetime
import json

from google.protobuf.json_format import MessageToJson

from concurrent import futures
from metatrader.mt4 import initizalize
from metatrader.backtest import BackTest
from metatrader.report import BacktestReport

from testing_data_pb2 import TestingData
from optimization_report_pb2 import OptimizationReport

def address_parser_server(file):
    with open(file) as json_file:
        parsed = json.loads(json_file.read())
        return parsed['server']['address']

def convertsion_report_to_message(report):
    report_message = OptimizationReport()
    # Assigning each value of the backtest report message
    # to its counterpart
    if report.profit:
        report_message.profit.value = report.profit

    if report.profit_factor:
        report_message.profit_factor.value = report.profit_factor

    if report.expected_payoff:
        report_message.expected_payoff.value = report.expected_payoff

    if report.max_drawdown:
        report_message.max_drawdown.value = report.max_drawdown

    if report.max_drawdown_rate:
        report_message.max_drawdown_rate.value = report.max_drawdown_rate

    if report.relative_drawdown:
        report_message.relative_drawdown.value = report.relative_drawdown

    if report.relative_drawdown_rate:
        report_message.relative_drawdown_rate.value = report.relative_drawdown_rate

    if report.abs_drawdown:
        report_message.abs_drawdown.value = report.abs_drawdown

    if report.abs_drawdown_rate:
        report_message.abs_drawdown_rate.value = report.abs_drawdown_rate

    if report.gross_profit:
        report_message.gross_profit.value = report.gross_profit

    if report.gross_loss:
        report_message.gross_loss.value = report.gross_loss

    if report.total_trades:
        report_message.total_trades.value = report.total_trades

    if report.largest_loss_trade:
        report_message.largest_loss_trade.value = report.largest_loss_trade

    if report.largest_profit_trade:
        report_message.largest_profit_trade.value = report.largest_profit_trade

    if report.average_loss_trade:
        report_message.average_loss_trade.value = report.average_loss_trade

    if report.average_profit_trade:
        report_message.average_profit_trade.value = report.average_profit_trade

    if report.modeling_quality_percentage:
        report_message.modeling_quality_percentage.value = report.modeling_quality_percentage

    if report.max_consecutive_loss:
        report_message.max_consecutive_loss.value = report.max_consecutive_loss

    if report.max_consecutive_loss_count:
        report_message.max_consecutive_loss_count.value = report.max_consecutive_loss_count

    if report.max_consecutive_losses_count:
        report_message.max_consecutive_losses_count.value = report.max_consecutive_losses_count

    if report.max_consecutive_losses_loss:
        report_message.max_consecutive_losses_loss.value = report.max_consecutive_losses_loss

    if report.max_consecutive_profit:
        report_message.max_consecutive_profit.value = report.max_consecutive_profit

    if report.max_consecutive_profit_count:
        report_message.max_consecutive_profit_count.value = report.max_consecutive_profit_count

    if report.max_consecutive_wins_count:
        report_message.max_consecutive_wins_count.value = report.max_consecutive_wins_count

    if report.max_consecutive_wins_profit:
        report_message.max_consecutive_wins_profit.value = report.max_consecutive_wins_profit

    if report.profit_trades:
        report_message.profit_trades.value = report.profit_trades

    if report.profit_trades_rate:
        report_message.profit_trades_rate.value = report.profit_trades_rate

    if report.loss_trades:
        report_message.loss_trades.value = report.loss_trades

    if report.loss_trades_rate:
        report_message.loss_trades_rate.value = report.loss_trades_rate

    if report.ave_consecutive_wins:
        report_message.ave_consecutive_wins.value = report.ave_consecutive_wins

    if report.ave_consecutive_losses:
        report_message.ave_consecutive_losses.value = report.ave_consecutive_losses

    if report.short_positions:
        report_message.short_positions.value = report.short_positions

    if report.short_positions_rate:
        report_message.short_positions_rate.value = report.short_positions_rate

    if report.long_positions:
        report_message.long_positions.value = report.long_positions

    if report.long_positions_rate:
        report_message.long_positions_rate.value = report.long_positions_rate

    # Return the message
    # print(report_message)
    return report_message

def convertsion_report_from_message(report_message):
    report = BacktestReport()
    # Assigning each value of the backtest report object
    # to its message counterpart
    if report_message.profit.value.value:
        report.profit = report_message.profit.value

    if report_message.profit_factor.value:
        report.profit_factor = report_message.profit_factor.value

    if report_message.expected_payoff.value:
        report.expected_payoff = report_message.expected_payoff.value

    if report_message.max_drawdown.value:
        report.max_drawdown = report_message.max_drawdown.value

    if report_message.max_drawdown_rate.value:
        report.max_drawdown_rate = report_message.max_drawdown_rate.value

    if report_message.relative_drawdown.value:
        report.relative_drawdown = report_message.relative_drawdown.value

    if report_message.relative_drawdown_rate.value:
        report.relative_drawdown_rate = report_message.relative_drawdown_rate.value

    if report_message.abs_drawdown.value:
        report.abs_drawdown = report_message.abs_drawdown.value

    if report_message.abs_drawdown_rate.value:
        report.abs_drawdown_rate = report_message.abs_drawdown_rate.value

    if report_message.gross_profit.value:
        report.gross_profit = report_message.gross_profit.value

    if report_message.gross_loss.value:
        report.gross_loss = report_message.gross_loss.value

    if report_message.total_trades.value:
        report.total_trades = report_message.total_trades.value

    if report_message.largest_loss_trade.value:
        report.largest_loss_trade = report_message.largest_loss_trade.value

    if report_message.largest_profit_trade.value:
        report.largest_profit_trade = report_message.largest_profit_trade.value

    if report_message.average_loss_trade.value:
        report.average_loss_trade = report_message.average_loss_trade.value

    if report_message.average_profit_trade.value:
        report.average_profit_trade = report_message.average_profit_trade.value

    if report_message.modeling_quality_percentage.value:
        report.modeling_quality_percentage = report_message.modeling_quality_percentage.value

    if report_message.max_consecutive_loss.value:
        report.max_consecutive_loss = report_message.max_consecutive_loss.value

    if report_message.max_consecutive_loss_count.value:
        report.max_consecutive_loss_count = report_message.max_consecutive_loss_count.value

    if report_message.max_consecutive_losses_count.value:
        report.max_consecutive_losses_count = report_message.max_consecutive_losses_count.value

    if report_message.max_consecutive_losses_loss.value:
        report.max_consecutive_losses_loss = report_message.max_consecutive_losses_loss.value

    if report_message.max_consecutive_profit.value:
        report.max_consecutive_profit = report_message.max_consecutive_profit.value

    if report_message.max_consecutive_profit_count.value:
        report.max_consecutive_profit_count = report_message.max_consecutive_profit_count.value

    if report_message.max_consecutive_wins_count.value:
        report.max_consecutive_wins_count = report_message.max_consecutive_wins_count.value

    if report_message.max_consecutive_wins_profit.value:
        report.max_consecutive_wins_profit = report_message.max_consecutive_wins_profit.value

    if report_message.profit_trades.value:
        report.profit_trades = report_message.profit_trades.value

    if report_message.profit_trades_rate.value:
        report.profit_trades_rate = report_message.profit_trades_rate.value

    if report_message.loss_trades.value:
        report.loss_trades = report_message.loss_trades.value

    if report_message.loss_trades_rate.value:
        report.loss_trades_rate = report_message.loss_trades_rate.value

    if report_message.ave_consecutive_wins.value:
        report.ave_consecutive_wins = report_message.ave_consecutive_wins.value

    if report_message.ave_consecutive_losses.value:
        report.ave_consecutive_losses = report_message.ave_consecutive_losses.value

    if report_message.short_positions.value:
        report.short_positions = report_message.short_positions.value

    if report_message.short_positions_rate.value:
        report.short_positions_rate = report_message.short_positions_rate.value

    if report_message.long_positions.value:
        report.long_positions = report_message.long_positions.value

    if report_message.long_positions.value:
        report.long_positions_rate = report_message.long_positions_rate.value

    # Return the report
    return report


def run_test(testing_data_message):
    # point mt4 install folder
    initizalize('C:\\Program Files (x86)\\MetaTrader 4 IC Markets')

    symbol = testing_data_message.symbol.value
    # print("Symbol: {}".format(symbol))

    period = testing_data_message.period.value
    # print("Period: {}".format(period))

    spread = testing_data_message.spread.value
    # print("Spread: {}".format(spread))

    ea_name = testing_data_message.algorithm.name.value
    # print("Al Name: {}".format(ea_name))

    param = ast.literal_eval(MessageToJson(testing_data_message.algorithm.parameters))
    # print("Al Param:")
    # print(param)

    from_date = datetime.datetime(\
        testing_data_message.time_period.initial_date.year.value,\
        testing_data_message.time_period.initial_date.month.value,\
        testing_data_message.time_period.initial_date.day.value)
    # print("Starting Date:")
    # print(from_date)

    to_date = datetime.datetime(\
        testing_data_message.time_period.final_date.year.value,\
        testing_data_message.time_period.final_date.month.value,\
        testing_data_message.time_period.final_date.day.value)
    # print("Starting Date:")
    # print(to_date)
    # create backtest object
    backtest = BackTest(ea_name, param, symbol, period, from_date, to_date)
    
    # run backtest
    ret = backtest.run()
    return convertsion_report_to_message(ret)
        
# x = TestingData()
# x.symbol.value = 'EURUSD'
# x.period.value = 'M5'
# x.spread.value = '5'
# x.time_period.initial_date.year.value = 2019
# x.time_period.initial_date.month.value = 8
# x.time_period.initial_date.day.value = 16
# x.time_period.final_date.year.value = 2019
# x.time_period.final_date.month.value = 8
# x.time_period.final_date.day.value = 17
# x.algorithm.name.value = 'Moving Average'
# x.algorithm.parameters.Lots.value = float(0.1)
# x.algorithm.parameters.MaximumRisk.value = float(0.02)
# x.algorithm.parameters.DecreaseFactor.value = float(3.0)
# x.algorithm.parameters.MovingPeriod.value = int(12)
# x.algorithm.parameters.MovingShift.value = int(6)
# report = convertsion_report_to_message(run_test(x))
# print(report)
