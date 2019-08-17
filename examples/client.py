import sys
sys.path.append("./messages")

import os
import grpc
import time
import threading
from concurrent import futures

import messages.service_pb2 as service
import messages.service_pb2_grpc as service_grpc

from messages.testing_data_pb2 import TestingData
from google.protobuf.empty_pb2 import Empty

def run():
    counter = 0
    pid = os.getppid()
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = service_grpc.MetaTrader4ServiceStub(channel)
        response = stub.get_testing_data(Empty())
        print(response)
        channel.unsubscribe(close)
        exit()

def close(channel):
    channel.close

if __name__ == "__main__":
    run()