#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program


class ToDoActions(object):
    """ Class for interacting with a to do list file """
    exitSelected = False
    toDoDict = {}
    toDoList = []

    def __init__(self, to_do_file):
        """ Initiate the class with the to do list file """
        self.toDoFile = to_do_file

    def read_todo(self):
        """ Function to read a to do list file line by line and calls another function to store within toDoList """
        for line in self.toDoFile.readlines():
            keyed_line = line.rstrip("\n\r").split(",")  
            self.add_new(keyed_line[0], keyed_line[1])

    def add_new(self, thing_to_do, importance):
        """ Function to add passed variables to toDoList """
        new_thing_to_do = {"Task": thing_to_do, "Priority": importance}
        self.toDoList += [new_thing_to_do]

    def remove_existing(self, index):
        """ Function removes an existing item from toDoList """
        
        try:
            removed_item = self.toDoList.pop(int(index))
            return removed_item["Task"] + " has been removed"
        except:
            return "The task was not removed"

    def save_data(self):
        """ Function saves back to toDoFile """
        for listItem in self.toDoList:
            self.toDoFile.write(listItem["Task"] + "," + listItem["Priority"] + "\n")

    def delete_file_content(self):
        """ Function to delete all existing lines in toDoFile """
        self.toDoFile.seek(0)
        self.toDoFile.truncate()

    def show_data(self):
        """shows data of list to console"""
        print("Index\t:\t Task \t:\t Priority")
        for idx, item in enumerate(self.toDoList):  
            print(idx, "\t\t:\t", item["Task"], "\t:\t", item["Priority"])

    def option_select(self):
        """ Function to print options to user and act upon user selection """
        
        print("""\tMenu of Options
        1) Show current data.
        2) Add a new item.
        3) Remove an existing item.
        4) Save data to file.
        5) Exit program.""")
        selitem = input("Choice: ")
        
        if selitem == "1":
            self.show_data()
        elif selitem == "2":
            thing_to_do = input("What is the task: ")
            importance = input("Priority?: ")
            self.add_new(thing_to_do, importance)
            print("Task added \n")
        elif selitem == "3":
            self.show_data() 
            index = input("Which item would you like removed?: ")
            remove_line = self.remove_existing(index)
            print(remove_line)
        elif selitem == "4":
            self.delete_file_content()
            self.save_data()
            print("List saved to " + TO_DO_DOC + "\n")
        elif selitem == "5":
            self.exitSelected = True
        else:
            print("That wasn't an option \n")
        print()



folder = "C:\Program Files\Python37"
module = "Module06\\Assignment06\\"
name = "ToDo.txt"
TO_DO_DOC = folder + module + name
try:
    objToDoFile = open(TO_DO_DOC, "r+")  
except:
    print("Exiting, please make sure that ", name, " is at: ", folder, module)
    import sys
    sys.exit()

toDoFunctions = ToDoActions(objToDoFile)


toDoFunctions.read_todo()  
while toDoFunctions.exitSelected is False:
    toDoFunctions.option_select()
toDoFunctions.toDoFile.close()
print("PROGRAM SUCCESSFULLY EXITED")