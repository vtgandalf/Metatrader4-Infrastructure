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

# import base as base

class Listener(service_grpc.MetaTrader4ServiceServicer):
    running = False

    def __inti__(self, *args, **kwargs):
        self.lastPrintTime = time.time()

    def get_testing_data(self, request, context):
        return self.data

    def execute_test(self, testing_data, context):
        self.running = True
        report = client_action(testing_data)
        self.running = False
        return report



def client_action(testing_data):
    counter = 0
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = service_grpc.MetaTrader4ServiceStub(channel)
        response = stub.execute_test(testing_data)
        channel.unsubscribe(close)
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    listener = Listener()
    service_grpc.add_MetaTrader4ServiceServicer_to_server(listener, server)
    server.add_insecure_port("[::]:9998")
    server.start()
    running_status = listener.running
    try:
        while True:
            if not listener.running == running_status:
                print("MT4 status changed from " + str(running_status) + " to " + str(listener.running))
                running_status = listener.running
            time.sleep(10)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)
    
if __name__ == "__main__":
    serve()