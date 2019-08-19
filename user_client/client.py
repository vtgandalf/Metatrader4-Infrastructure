import os
import sys
sys.path.append(os.path.abspath('messages_py'))

import grpc
import time
import threading
from concurrent import futures

import service_pb2 as service
import service_pb2_grpc as service_grpc

from testing_data_pb2 import TestingData
from google.protobuf.empty_pb2 import Empty

def run():
    x = TestingData()
    x.symbol.value = 'EURUSD'
    x.period.value = 'M5'
    x.spread.value = '5'
    x.time_period.initial_date.year.value = 2019
    x.time_period.initial_date.month.value = 8
    x.time_period.initial_date.day.value = 16
    x.time_period.final_date.year.value = 2019
    x.time_period.final_date.month.value = 8
    x.time_period.final_date.day.value = 17
    x.algorithm.name.value = 'Moving Average'
    x.algorithm.parameters.Lots.value = float(0.1)
    x.algorithm.parameters.MaximumRisk.value = float(0.02)
    x.algorithm.parameters.DecreaseFactor.value = float(3.0)
    x.algorithm.parameters.MovingPeriod.value = int(12)
    x.algorithm.parameters.MovingShift.value = int(6)

    with grpc.insecure_channel("192.168.1.11:9998") as channel:
        stub = service_grpc.MetaTrader4ServiceStub(channel)
        response = stub.execute_test(x)
        print(response)
        channel.unsubscribe(close)
        exit()

def close(channel):
    channel.close

if __name__ == "__main__":
    run()