import tkinter
from tkinter import *
import json

class Example(Frame):
    json_file = 'gui.json'
    algorithm_list = list()
    window_elements_container = list()
    parsed = None
    with open(json_file) as f:
        parsed = json.loads(f.read())

    def parse_algorithms(self, json_file):
        for algorithm in self.parsed['algorithms']:
            self.algorithm_list.append(algorithm['name'])

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
        actions_menu.add_command(label = "Exit", command = self.onExit)

        algorithm_menu = tkinter.Menu(root_menu)
        # it creates the name of the sub menu
        root_menu.add_cascade(label = "Algorithms", menu = algorithm_menu)
        i = 0
        for algorithm in self.parsed['algorithms']:
            algorithm_menu.add_command(label = algorithm['name'], command = lambda x=algorithm['name']: self.refreshUI(x))
            i = i + 1
        

    def onSend(self):
        pass

    def onExit(self):
        self.quit()


    def refreshUI(self, name):
        print(name)
        for algorithm in self.parsed['algorithms']:
            if algorithm['name'] == name:
                for element in self.window_elements_container:
                    if element:
                        for widget in element:
                            widget.destroy()
                self.window_elements_container = list()
                i = 0
                for element in (algorithm['parameters']):
                    name = list(element.keys())[0]
                    label = tkinter.Label(self.master, text = name)
                    label.grid(row = i)
                    default = StringVar(self.master, value=element.get(name))
                    text_box = tkinter.Entry(self.master, textvariable=default)
                    text_box.grid(row = i, column = 1)
                    self.window_elements_container.append([label,text_box])
                    i = i + 1


def main():
    window = Tk()
    # window.geometry("250x150+300+300")
    app = Example()
    window.mainloop()


if __name__ == '__main__':
    main()
