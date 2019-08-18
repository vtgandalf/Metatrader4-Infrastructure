import os
import sys
sys.path.append(os.path.abspath('messages'))

import grpc
import time
import threading
import datetime

from google.protobuf.json_format import MessageToJson

from concurrent import futures
from metatrader.mt4 import initizalize
from metatrader.backtest import BackTest
from metatrader.report import BacktestReport

from testing_data_pb2 import TestingData
from optimization_report_pb2 import OptimizationReport

def convertsion_report_to_message(report: BacktestReport):
    report_message = OptimizationReport()
    # Assigning each value of the backtest report message
    # to its counterpart
    report_message.profit.value = report.profit
    report_message.profit_factor.value = report.profit_factor
    report_message.expected_payoff.value = report.expected_payoff
    report_message.max_drawdown.value = report.max_drawdown
    report_message.max_drawdown_rate.value = report.max_drawdown_rate
    report_message.relative_drawdown.value = report.relative_drawdown
    report_message.relative_drawdown_rate.value = report.relative_drawdown_rate
    report_message.abs_drawdown.value = report.abs_drawdown
    report_message.abs_drawdown_rate.value = report.abs_drawdown_rate
    report_message.gross_profit.value = report.gross_profit
    report_message.gross_loss.value = report.gross_loss
    report_message.total_trades.value = report.total_trades
    report_message.largest_loss_trade.value = report.largest_loss_trade
    report_message.largest_profit_trade.value = report.largest_profit_trade
    report_message.average_loss_trade.value = report.average_loss_trade
    report_message.average_profit_trade.value = report.average_profit_trade
    report_message.modeling_quality_percentage.value = report.modeling_quality_percentage
    report_message.max_consecutive_loss.value = report.max_consecutive_loss
    report_message.max_consecutive_loss_count.value = report.max_consecutive_loss_count
    report_message.max_consecutive_losses_count.value = report.max_consecutive_losses_count
    report_message.max_consecutive_losses_loss.value = report.max_consecutive_losses_loss
    report_message.max_consecutive_profit.value = report.max_consecutive_profit
    report_message.max_consecutive_profit_count.value = report.max_consecutive_profit_count
    report_message.max_consecutive_wins_count.value = report.max_consecutive_wins_count
    report_message.max_consecutive_wins_profit.value = report.max_consecutive_wins_profit
    report_message.profit_trades.value = report.profit_trades
    report_message.profit_trades_rate.value = report.profit_trades_rate
    report_message.loss_trades.value = report.loss_trades
    report_message.loss_trades_rate.value = report.loss_trades_rate
    report_message.ave_consecutive_wins.value = report_message.ave_consecutive_wins
    report_message.ave_consecutive_losses.value = report.ave_consecutive_losses
    report_message.short_positions.value = report.short_positions
    report_message.short_positions_rate.value = report.short_positions_rate
    report_message.long_positions.value = report.long_positions
    report_message.long_positions_rate.value = report.long_positions_rate
    # Return the message
    print(report_message)
    return report_message

def convertsion_report_from_message(report_message: OptimizationReport):
    report = BacktestReport()
    # Assigning each value of the backtest report object
    # to its message counterpart
    report.profit = report_message.profit.value
    report.profit_factor = report_message.profit_factor.value
    report.expected_payoff = report_message.expected_payoff.value 
    report.max_drawdown = report_message.max_drawdown.value
    report.max_drawdown_rate = report_message.max_drawdown_rate.value
    report.relative_drawdown = report_message.relative_drawdown.value
    report.relative_drawdown_rate = report_message.relative_drawdown_rate.value
    report.abs_drawdown = report_message.abs_drawdown.value
    report.abs_drawdown_rate = report_message.abs_drawdown_rate.value
    report.gross_profit = report_message.gross_profit.value
    report.gross_loss = report_message.gross_loss.value
    report.total_trades = report_message.total_trades.value
    report.largest_loss_trade = report_message.largest_loss_trade.value
    report.largest_profit_trade = report_message.largest_profit_trade.value
    report.average_loss_trade = report_message.average_loss_trade.value
    report.average_profit_trade = report_message.average_profit_trade.value
    report.modeling_quality_percentage = report_message.modeling_quality_percentage.value
    report.max_consecutive_loss = report_message.max_consecutive_loss.value
    report.max_consecutive_loss_count = report_message.max_consecutive_loss_count.value
    report.max_consecutive_losses_count = report_message.max_consecutive_losses_count.value
    report.max_consecutive_losses_loss = report_message.max_consecutive_losses_loss.value
    report.max_consecutive_profit = report_message.max_consecutive_profit.value
    report.max_consecutive_profit_count = report_message.max_consecutive_profit_count.value
    report.max_consecutive_wins_count = report_message.max_consecutive_wins_count.value
    report.max_consecutive_wins_profit = report_message.max_consecutive_wins_profit.value
    report.profit_trades = report_message.profit_trades.value
    report.profit_trades_rate = report_message.profit_trades_rate.value
    report.loss_trades = report_message.loss_trades.value
    report.loss_trades_rate = report_message.loss_trades_rate.value
    report_message.ave_consecutive_wins = report_message.ave_consecutive_wins.value
    report.ave_consecutive_losses = report_message.ave_consecutive_losses.value
    report.short_positions = report_message.short_positions.value
    report.short_positions_rate = report_message.short_positions_rate.value
    report.long_positions = report_message.long_positions.value
    report.long_positions_rate = report_message.long_positions_rate.value
    # Return the report
    print(report)
    return report


def run_test(testing_data_message: TestingData):
    # point mt4 install folder
    initizalize('C:\\Program Files (x86)\\MetaTrader 4 IC Markets')

    symbol = testing_data_message.symbol.value
    print("Symbol: {}".format(symbol))
    period = testing_data_message.period.value
    print("Period: {}".format(period))
    spread = testing_data_message.spread.value
    print("Spread: {}".format(spread))

    # for example 'Moving Average'
    ea_name = testing_data_message.algotithm.name.value
    print("Al Name: {}".format(ea_name))
    # param = {
    #         'Lots': {'value': 0.1},
    #         'MaximumRisk': {'value': 0.02},
    #         'DecreaseFactor': {'value': 3.0},
    #         'MovingPeriod': {'value': 12},
    #         'MovingShift': {'value': 6},
    #         }
    param = MessageToJson(testing_data_message.algotithm.parameters)
    print("Al Param:")
    print(param)

    from_date = datetime.datetime(\
        testing_data_message.time_period.initial_date.year.value,\
        testing_data_message.time_period.initial_date.month.value,\
        testing_data_message.time_period.initial_date.day.value)\
    print("Starting Date: {}".format(str(from_date).strip()))

    to_date = datetime.datetime(\
        testing_data_message.time_period.final_date.year.value,\
        testing_data_message.time_period.final_date.month.value,\
        testing_data_message.time_period.final_date.day.value)
    print("Starting Date: {}".format(str(to_date).strip()))


    # create backtest object
    # backtest = BackTest(ea_name, param, symbol, period, from_date, to_date)

    # run backtest
    # ret = backtest.run()

    # you can get result from result object
    # for example you can print gross profit
    # print(ret.gross_profit)
    return
        

