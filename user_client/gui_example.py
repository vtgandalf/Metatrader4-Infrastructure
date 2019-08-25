import os
import sys
sys.path.append(os.path.abspath('messages_py'))

import tkinter
from tkinter import *
import json
import google.protobuf.json_format as json_format

import grpc
import time
import threading
from multiprocessing import Process
from concurrent import futures

import service_pb2 as service
import service_pb2_grpc as service_grpc
from google.protobuf.empty_pb2 import Empty

from testing_data_pb2 import TestingData

import base as base

# GLOBALS
testing_data_queue = []
lock = threading.Lock()

# THREADS
gui_thread = threading.Thread()
grpc_thread = threading.Thread()

# SERVER
grpc_timeout = 5

class Listener(service_grpc.MetaTrader4ServiceServicer):
    server_address = None
    report_count = 0

    def __inti__(self, *args, **kwargs):
        self.lastPrintTime = time.time()

    def set_result(self, report, context):
        self.report_count = self.report_count + 1
        print("Result from station({}):".format(str(report.station_id.value)))
        print(report)
        print("Report Count({})".format(str(self.report_count)))
        return Empty()

    def check_online(self, request, context):
        return Empty()



def client_action_set_testing_data(testing_data, address):
    with grpc.insecure_channel(address) as channel:
        stub = service_grpc.MetaTrader4ServiceStub(channel)
        response = stub.set_testing_data(testing_data)
        channel.unsubscribe(close)

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
    listener.server_address = base.address_parser_server('./../addresses.json')

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    service_grpc.add_MetaTrader4ServiceServicer_to_server(listener, server)
    server.add_insecure_port("[::]:9998")
    server.start()

    try:
        while True:
            queue_cpy = None
            global testing_data_queue
            lock.acquire()
            if testing_data_queue:
                queue_cpy = testing_data_queue
            lock.release()
            if queue_cpy:
                for message in queue_cpy:
                    try:
                        client_check_online(listener.server_address)
                    except Exception as err:
                        # print(err)
                        print("ERROR: Could not connect to server({})!".format(str(listener.server_address)))
                    else:
                        client_action_set_testing_data(message, listener.server_address)
                        queue_cpy.remove(message)
                        print("INFO: Testing data sent to server({}).".format(str(listener.server_address)))
                        break
                lock.acquire()
                testing_data_queue = queue_cpy
                lock.release()

            time.sleep(1)
    except KeyboardInterrupt:
        print("INFO: KeyboardInterrupt.")
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
# END SERVER

# FORM
class Example(Frame):
    json_file = 'gui.json'
    window_elements_container = list()
    algorithms = list()
    common_elements = list()
    parameter_list = list()
    parsed = None
    chosen_algorithm = None
    with open(json_file) as f:
        parsed = json.loads(f.read())

    def refresh_parsed(self):
        with open(self.json_file) as f:
            self.parsed = json.loads(f.read())

    def parse_algorithms(self, json_file):
        for algorithm in self.parsed['algorithms']:
            self.algorithms.append(algorithm)

    def __init__(self):
        super().__init__()
        self.parse_algorithms(self.json_file)
        self.initUI()

    def initUI(self):
        self.master.title("GUI")
        # creating a root menu to insert all the sub menus
        root_menu = tkinter.Menu(self.master)
        self.master.config(menu = root_menu)

        # creating sub menus in the root menu
        # it intializes a new sub menu in the root menu
        actions_menu = tkinter.Menu(root_menu)
        root_menu.add_cascade(label = "Actions", menu = actions_menu)
        actions_menu.add_command(label = "Send", command = self.onSend)

        algorithm_menu = tkinter.Menu(root_menu)
        # it creates the name of the sub menu
        root_menu.add_cascade(label = "Algorithms", menu = algorithm_menu)
        i = 0
        for algorithm in self.algorithms:
            algorithm_menu.add_command(label = algorithm['name'], command = lambda x=algorithm['name']: self.refreshUI(x))
            i = i + 1
        
        i = 0
        for element in self.parsed['common']:
            try:
                self.parsed['common'][element][0]
            except:
                for obj in self.parsed['common'][element]:
                    name = obj
                    label = tkinter.Label(self.master, text = name)
                    label.grid(row = i)
                    i = i + 1
                    for param in self.parsed['common'][element][obj]:
                        name = param
                        label = tkinter.Label(self.master, text = name)
                        label.grid(row = i)
                        default = StringVar(self.master, value=self.parsed['common'][element][obj][param])
                        text_box = tkinter.Entry(self.master, textvariable=default)
                        text_box.grid(row = i, column = 1)
                        self.common_elements.append([obj, name, text_box])
                        i = i + 1
            else:
                name = element
                label = tkinter.Label(self.master, text = name)
                label.grid(row = i)
                default = StringVar(self.master, value=self.parsed['common'][element])
                text_box = tkinter.Entry(self.master, textvariable=default)
                text_box.grid(row = i, column = 1)
                self.common_elements.append([name, text_box])
                i = i + 1

        b = Button(self.master, text="Send", command = self.onSend).grid(row = i)

    def getMessageFromJson(self):
        for element in self.parsed['common']:
            try:
                self.parsed['common'][element][0]
            except:
                for x in self.common_elements:
                    for obj in self.parsed['common'][element]:
                        if obj == x[0]:
                            self.parsed['common'][element][obj][x[1]] = x[2].get()
                            break
            else: 
                for x in self.common_elements:
                    if x[0] == element:
                        self.parsed['common'][element] = x[1].get()
                        break
            
        if self.chosen_algorithm:
            i = 0
            for algorithm in self.parsed['algorithms']:
                if algorithm['name'] == self.chosen_algorithm:
                    for parameter in algorithm['parameters']:
                        for x in self.parameter_list:
                            if x[0] == parameter:
                                algorithm['parameters'][parameter] = x[1].get()
                else:
                    del self.parsed['algorithms'][i]
                i = i + 1


        dict_data = dict()
        for el in self.parsed['common']:
            try:
                self.parsed['common'][el][0]
            except:
                sub_dict = dict()
                for x in self.parsed['common'][el]:
                    sub_sub_dict = dict()
                    for y in self.parsed['common'][el][x]:
                        sub_sub_dict.update({y: {"value": self.parsed['common'][el][x][y]}})
                    sub_dict.update({x: sub_sub_dict})
                dict_data.update({el: sub_dict})
                    
            else: 
                dict_data.update({el: {"value": self.parsed['common'][el]}})

        algorithm_dict = dict()
        for algorithm in self.parsed['algorithms']:
            for el in algorithm:
                try:
                    algorithm[el][0]
                except:
                    sub_dict = dict()
                    for x in algorithm[el]:
                        sub_dict.update({x: {"value": algorithm[el][x]}})
                    algorithm_dict.update({el: sub_dict})
                        
                else: 
                    if el == "name":
                        algorithm_dict.update({el: {"value": algorithm[el]}})

                dict_data.update({"algorithm": algorithm_dict})
        
        js = json.dumps(dict_data)
        message = TestingData()
        json_format.Parse(js, message, ignore_unknown_fields=False)
        print(message)
        return(message)


    def onSend(self):
        if self.chosen_algorithm:
            message = self.getMessageFromJson()
            global testing_data_queue
            lock.acquire()
            testing_data_queue.append(message)
            lock.release()
            

    def refreshUI(self, name):
        self.chosen_algorithm = name
        self.refresh_parsed()
        for algorithm in self.algorithms:
            if algorithm['name'] == name:
                for element in self.window_elements_container:
                    if element:
                        for widget in element:
                            widget.destroy()
                self.window_elements_container = list()
                self.parameter_list = list()
                i = 0
                for element in (algorithm['parameters']):
                    name = element
                    label = tkinter.Label(self.master, text = name)
                    label.grid(row = i, column = 2)
                    default = StringVar(self.master, value=algorithm['parameters'][element])
                    text_box = tkinter.Entry(self.master, textvariable=default)
                    text_box.grid(row = i, column = 3)
                    self.window_elements_container.append([label,text_box])
                    self.parameter_list.append([name, text_box])
                    i = i + 1
# END FORM
def init_threads():
    print("start gui")
    gui_thread = threading.Thread(target=main).start()
    print("start grpc")
    grpc_thread = threading.Thread(target=serve).start()
    # gui_thread
    # grpc_thread

def main():
    window = Tk()
    # window.geometry("250x150+300+300")
    app = Example()
    window.mainloop()

if __name__ == '__main__':
    init_threads()
