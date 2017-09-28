import sys 
import os


class Todo(object):
    def __init__(self):
        os.system("clear")
        self.arguments = [
            {"argument": "-l", "description": "Lists all the tasks"},
            {"argument": "-a", "description": "Adds new task"},
            {"argument": "-r", "description":"Removes a task"},
            {"argument": "-c", "description":"Completes a task"}
        ]
        if len(sys.argv) == 2 and sys.argv[1] == "-l":
            return self.list_todo()
        elif len(sys.argv) == 3 and sys.argv[1] == "-a":
            item = str(sys.argv[2])
            return self.add_todo(item)
        elif len(sys.argv) == 3 and sys.argv[1] == "-r":
            index = int(sys.argv[2])
            return self.remove_item(index)
        elif len(sys.argv) == 3 and sys.argv[1] == "-c":
            index = int(sys.argv[2])
            return self.check_item(index)
        else:
            print ("Command Line Todo application\n" +
            "=============================\n\n" +
            "Command line arguments:")
            for items in self.arguments:
                print(items["argument"]+ " " + items["description"])
    
    
    def add_todo(self, item):
        file = open("todo_list.txt", "a") 
        file.write(str(item + "\n")) 
        file.close()


    def list_todo(self):
        with open('todo_list.txt') as f:
            lines = [line.rstrip('\n') for line in open('todo_list.txt')]
            index_num = 1
            for i in lines:
                print(index_num, "[ ]" , i)
                index_num +=1


    def remove_item(self, index):
        with open("todo_list.txt","r") as textobj:
            listed = list(textobj)
            del listed[index - 1]    
        with open("todo_list.txt","w") as textobj:
            for n in listed:
                textobj.write(n)

    def check_item(self, index):
        with open('todo_list.txt') as f:
            lines = [line.rstrip('\n') for line in open('todo_list.txt')]
            index_num = 1
            if index == index_num:
                print(index_num, "[X]" , i)
            else:    
                index_num +=1

def start_todo():
    app = Todo()
    
    
       


start_todo()













