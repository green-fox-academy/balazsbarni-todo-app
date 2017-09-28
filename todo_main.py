import sys 
import os


class Todo(object):
    def __init__(self):
        self.commands = [
            {"argument": "-l", "description": "Lists all the tasks"},
            {"argument": "-a", "description": "Adds new task"},
            {"argument": "-r", "description":"Removes a task"},
            {"argument": "-c", "description":"Completes a task"}
        ]

    def commands_printer(self):
        print ("Command Line Todo application\n" +
        "=============================\n\n" +
        "Command line arguments:")
        for items in self.commands:
            print(items["argument"]+ " " + items["description"])


   
def start_todo():
    os.system("clear")
    app = Todo()
    args = sys.argv[1:]
    if not args:
        app.commands_printer()


start_todo()













