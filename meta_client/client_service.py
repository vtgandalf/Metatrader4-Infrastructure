import os
import sys
sys.path.append(os.path.abspath('messages'))

import grpc
import time
import threading
from concurrent import futures

import service_pb2 as service
import service_pb2_grpc as service_grpc

from testing_data_pb2 import TestingData
from google.protobuf.empty_pb2 import Empty
import base as base

class Listener(service_grpc.MetaTrader4ServiceServicer):
    running = False
    server_address = None
    testing_data = None
    report = None
    station_id = None

    def __inti__(self, *args, **kwargs):
        self.lastPrintTime = time.time()

    def get_testing_data(self, request, context):
        return self.data

    def set_testing_data(self, testing_data, context):
        self.testing_data = testing_data
        self.station_id = testing_data.station_id.value
        print("Testing data received")
        return Empty()

def client_action_set_result(report, address):
    with grpc.insecure_channel(address) as channel:
        stub = service_grpc.MetaTrader4ServiceStub(channel)
        response = stub.set_result(report)
        channel.unsubscribe(close)
        return

def close(channel):
    channel.close
    
def serve():
    listener = Listener()
    listener.server_address = base.address_parser_server('./../addresses.json')

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    service_grpc.add_MetaTrader4ServiceServicer_to_server(listener, server)
    server.add_insecure_port("[::]:9999")
    server.start()

    running_status = listener.running
    try:
        while True:
            if not listener.running == running_status:
                print("MT4 status changed from " + str(running_status) + " to " + str(listener.running))
                running_status = listener.running

            if listener.running and listener.testing_data:
                report = base.run_test(listener.testing_data)
                report.station_id.value = listener.station_id
                client_action_set_result(report, listener.server_address)
                listener.running = False
                listener.testing_data = None

            time.sleep(10)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)
    
if __name__ == "__main__":
    serve()