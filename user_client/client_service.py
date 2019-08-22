import os
import sys
sys.path.append(os.path.abspath('messages_py'))

import grpc
import time
import threading
from concurrent import futures

import service_pb2 as service
import service_pb2_grpc as service_grpc
from google.protobuf.empty import Empty

from testing_data_pb2 import TestingData

import base as base

class Listener(service_grpc.MetaTrader4ServiceServicer):
    server_address = None

    def __inti__(self, *args, **kwargs):
        self.lastPrintTime = time.time()

    def set_result(self, report, context):
        print("Result from {}:".format(str(report.station_id.value)))
        print(report)
        return Empty()



def client_action_set_testing_data(testing_data, address):
    with grpc.insecure_channel(address) as channel:
        stub = service_grpc.MetaTrader4ServiceStub(channel)
        response = stub.set_testing_data(testing_data)
        channel.unsubscribe(close)

def serve():
    listener = Listener()
    listener.server_address = base.address_parser_server('./../addresses.json')

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    service_grpc.add_MetaTrader4ServiceServicer_to_server(listener, server)
    server.add_insecure_port("[::]:9998")
    server.start()

    try:
        while True:
            index = input()
            testing_data = mock_testing_data()
            if index == '1':
                client_action_set_testing_data(mock_testing_data(), listener.server_address)
                print("Testing data sent")
            time.sleep(10)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)

def mock_testing_data():
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
    return x
    
if __name__ == "__main__":
    serve()