import os
import sys
sys.path.append(os.path.abspath('messages'))

import ast
import grpc
import time
import threading
import datetime
import json

from testing_data_pb2 import TestingData
from optimization_report_pb2 import OptimizationReport

def address_parser_meta(file):
    with open(file) as json_file:
        parsed = json.loads(json_file.read())
        addr_list = list()
        for address in parsed['meta_clients']
            addr_list.append(address['address'])
        return addr_list

def address_parser_user(file):
    with open(file) as json_file:
        parsed = json.loads(json_file.read())
        addr_list = list()
        for address in parsed['user_clients']
            addr_list.append(address['address'])
        return addr_list

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
    print(report_message)
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
    print(report)
    return report