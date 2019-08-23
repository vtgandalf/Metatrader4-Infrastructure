import os
import sys
sys.path.append(os.path.abspath('messages'))

import grpc
import time
import threading
from concurrent import futures

import service_pb2 as service
import service_pb2_grpc as service_grpc
from google.protobuf.empty_pb2 import Empty

from testing_data_pb2 import TestingData

import base as base




class Station():
    address = str()
    working = bool()



class Listener(service_grpc.MetaTrader4ServiceServicer):
    job_queue = list()
    station_list = list()
    user_list = list()

    def __inti__(self, *args, **kwargs):
        self.lastPrintTime = time.time()

    def fill_station_list(self, stations = []):
        for address in stations:
            station = Station()
            station.address = address
            station.working = False
            self.station_list.append(station)

        print("Stations list initialized:")
        print(self.station_list)

    def fill_user_list(self, users = []):
        self.user_list.extend(users)
        print("User list initialized:")
        print(self.user_list)

    def set_testing_data(self, testing_data, context):
        for i, station in self.station_list:
            if not station.working:
                testing_data.station_id.value = i
                client_action_set_testing_data(testing_data, station.address)
                sration.working = True
                print("Station working on it:")
                print(station)
                break
        else:
            job_queue.queue.append(testing_data)

        return Empty()

    def set_result(self, report, context):
        for user in user_list:
            self.station_list[report.station_id.value].working = False
            client_action_set_result(report, user_list)
        return Empty()



def client_action_set_testing_data(testing_data, address):
    with grpc.insecure_channel(address) as channel:
        stub = service_grpc.MetaTrader4ServiceStub(channel)
        response = stub.set_testing_data(testing_data)
        channel.unsubscribe(close)
        return

def client_action_set_result(report, address):
    with grpc.insecure_channel(address) as channel:
        stub = service_grpc.MetaTrader4ServiceStub(channel)
        response = stub.set_result(report)
        channel.unsubscribe(close)
        return

def serve():
    listener = Listener()
    stations = base.address_parser_meta('./../addresses.json')
    users = base.address_parser_user('./../addresses.json')
    listener.fill_station_list(stations)
    listener.fill_user_list(users)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    service_grpc.add_MetaTrader4ServiceServicer_to_server(listener, server)
    server.add_insecure_port("[::]:9998")
    server.start()

    try:
        while True:
            if listener.job_queue:
                for job in listener.job_queue:
                    for i, station in listener.station_list:
                        if not station.working:
                            job.station_id.value = i
                            client_action_set_testing_data(job, station.address)
                            job_queue.remove(job)
            time.sleep(10)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)
    
if __name__ == "__main__":
    serve()