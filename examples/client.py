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

def run():
    counter = 0
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = service_grpc.MetaTrader4ServiceStub(channel)
        response = stub.execute_test(Empty())
        print(response)
        channel.unsubscribe(close)
        exit()

def close(channel):
    channel.close

if __name__ == "__main__":
    run()