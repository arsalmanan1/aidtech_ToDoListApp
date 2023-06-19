import os

class Task:
    def __init__(self, title="", des="", status=False):
        self.title = title
        self.description = des
        self.status = status
    
    def settask(self):
        t = input("Enter task title: ")
        d = input("Enter description of the task: ")
        s = input("Enter 'Done' status of task (True or False): ")
        self.title = t
        self.description = d
        self.status = bool(s)
    
    def __repr__(self): 
        if self.status:
            st = "done"
        else:
            st = "pending"
        return f"\n---------------------\nTITLE OF TASK '{self.title}' , \nDESCRIPTION {self.description} , \nTHE TASK IS {st}"
    
    def outputtask(self):
        if self.status:
            st = "done"
        else:
            st = "pending"
        print("\n---------------------\nTITLE OF TASK ", self.title, "\nDESCRIPTION ", self.description, "\nTHE TASK IS ", st)


class ToDoList:
    def __init__(self):
        self.tasklist = []
    
    def add_task(self, title="", des="", st=False):
        print("ADDING TASK TO TODOLIST !!!")
        if len(title) > 0:
            newTask = Task(title, des, st)
        else:
            newTask = Task()
            newTask.settask()
        self.tasklist.append(newTask)
    
    def delete_task(self, tasktitle):
        for tasks in self.tasklist:
            if tasks.title == tasktitle:
                ind = self.tasklist.index(tasks)
                print("DELETING TASK", ind+1, "that is", tasks)
                self.tasklist.pop(ind)
    
    def view_tasks(self):
        for task in self.tasklist:
            task.outputtask()
    
    def save_tasks(self, file):
        for task in self.tasklist:
            file.write(repr(task))
            file.write('\n')
    def load_tasks(self,file):
        for line in file:
            # Process each line of the file
            print(line)



mylist = ToDoList()
print("========= ADDING TASKS =========\n\n")
mylist.add_task("Number guessing game", "generate random num 1-100 and guess", True)
mylist.add_task("ToDoListapp", "OOP in python", True)
mylist.add_task("Dice roller", "random num 1-6", False)
mylist.add_task("gems game", "c++ 2d array", True)
mylist.add_task()

print("\n\n========= VIEW TASKS =========\n\n\n\n")
mylist.view_tasks()

print("\n\n========= DELETING TASKS =========\n\n\n")
mylist.delete_task("gems game")

print("\n\n========= VIEW TASKS =========\n\n\n\n")
mylist.view_tasks()

print("\n\n========= SAVING TASKS TO FILE =========\n\n\n\n")
file_path = "todolist.txt"
with open(file_path, "w") as my_file:
    mylist.save_tasks(my_file)

print("\n\n========= LOADING TASKS FROM FILE =========\n\n\n\n")
with open(file_path, 'r') as my_file:
    mylist.load_tasks(my_file)

my_file.close()
