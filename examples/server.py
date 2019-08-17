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

class Listener(service_grpc.MetaTrader4ServiceServicer):
    # adding testing object with some data
    data = TestingData()
    data.symbol.value = 'test_symbol'
    data.period.value = 'test_period'
    data.spread.value = 'test_spread'

    lastPrintTime = 0

    def __inti__(self, *args, **kwargs):
        self.counter = 0
        self.lastPrintTime = time.time()

    def get_testing_data(self, request, context):
        return self.data
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    service_grpc.add_MetaTrader4ServiceServicer_to_server(Listener(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    try:
        while True:
            print("server on: threads %i" % (threading.active_count()))
            time.sleep(10)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)
    
if __name__ == "__main__":
    serve()