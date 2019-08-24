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

grpc_timeout = 5


class Station():
    address = str()
    working = bool()
    def __init__(self, address, working):
        self.address = address
        self.working = working



class Listener(service_grpc.MetaTrader4ServiceServicer):
    report_list = list()
    job_queue = list()
    station_list = list()
    user_list = list()

    def __inti__(self, *args, **kwargs):
        self.lastPrintTime = time.time()

    def fill_station_list(self, stations = []):
        for address in stations:
            station = Station(address, False)
            self.station_list.append(Station(address, False))

        print("INFO: Stations list initialized:")
        print(self.station_list)


    def fill_user_list(self, users = []):
        self.user_list.extend(users)
        print("INFO: User list initialized:")
        print(self.user_list)

    def set_testing_data(self, testing_data, context):
        self.job_queue.append(testing_data)
        print("INFO: Job received and added to job queue.")
        return Empty()

    def set_result(self, report, context):
        print("INFO: Result received from MT4 station.")
        self.report_list.append(report)
        return Empty()

    def check_online(self, request, context):
        return Empty()



def client_action_set_testing_data(testing_data, address):
    with grpc.insecure_channel(address) as channel:
        stub = service_grpc.MetaTrader4ServiceStub(channel)
        stub.set_testing_data(testing_data)
        channel.unsubscribe(close)
        return

def client_action_set_result(report, address):
    with grpc.insecure_channel(address) as channel:
        stub = service_grpc.MetaTrader4ServiceStub(channel)
        stub.set_result(report)
        channel.unsubscribe(close)
        return

def client_check_online(address):
    with grpc.insecure_channel(address) as channel:
        stub = service_grpc.MetaTrader4ServiceStub(channel)
        stub.check_online(Empty(), grpc_timeout)
        channel.unsubscribe(close)
        return

def close(channel):
    channel.close

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
                    i = 0
                    for station in listener.station_list:
                        if not station.working:
                            try:
                                client_check_online(station.address)
                            except Exception as err:
                                # print(err)
                                print("ERROR: Could not connect to station({})!".format(str(station.address)))
                            else:
                                print("INFO: Station({}) working on it.".format(str(station.address)))
                                station.working = True
                                job.station_id.value = i
                                client_action_set_testing_data(job, station.address)
                                listener.job_queue.remove(job)
                                break
                        i = i + 1
            if listener.report_list:
                for report in listener.report_list:
                    i = 0
                    for user in listener.user_list:
                        print("INFO: Sending report to user({}).".format(str(user)))
                        listener.station_list[report.station_id.value].working = False         
                        try:
                            client_check_online(user)
                        except Exception as err:
                            # print(err)
                            print("ERROR: Could not connect to user({})!".format(str(user)))
                        else:
                            client_action_set_result(report, user)
                        listener.report_list.remove(report)
                    i = i + 1
            # time.sleep(0.5)
    except KeyboardInterrupt:
        print("INFO: KeyboardInterrupt.")
        server.stop(0)
    
if __name__ == "__main__":
    serve()