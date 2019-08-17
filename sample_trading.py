import datetime
from metatrader.mt4 import initizalize
from metatrader.backtest import BackTest

# point mt4 install folder
initizalize('C:\\Program Files (x86)\\MetaTrader 4 IC Markets')

# specify backtest period by datetime format
from_date = datetime.datetime(2019, 8, 1)
to_date = datetime.datetime(2019, 8, 2)

ea_name = 'Moving Average'

# create ea param by dict.
param = {
         'Lots': {'value': 0.1},
         'MaximumRisk': {'value': 0.02},
         'DecreaseFactor': {'value': 3.0},
         'MovingPeriod': {'value': 12},
         'MovingShift': {'value': 6},
         }
# create backtest object
backtest = BackTest(ea_name, param, 'EURUSD', 'M5', from_date, to_date)

# run backtest
ret = backtest.run()

# you can get result from result object
# for example you can print gross profit
print(ret.gross_profit)