#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   <YOUR NAME HERE>, ???, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

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
#-------------------------------

objFileName = "C:\\Program Files\\Python37\\Todo.txt"
strData = ""
dicRow = {}
lstTable = []

objFile = open(objFileName, "r")
for line in objFile:
    strData = line.split(",") # readline() reads a line of the data into 2 elements
    dicRow = {"Task":strData[0].strip(), "Priority":strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()
# Step 1 - Load data from a file
    # When the program starts, load each "row" of data 
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"
 

# Step 2 - Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print( "The tasks to do are:")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        continue
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
       strTask = str(input("What is the task? - ")).strip()
       strPriority = str(input("What is the priority? [high|low] - ")).strip()
       dicRow = {"Task":strTask,"Priority":strPriority}
       lstTable.append(dicRow)
       print("Things to be done:")
       for dicRow in lstTable:
            print(dicRow)
            
       print("The current tasks to do are:")
       for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
       continue
    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        strKeyToRemove = input("Which TASK would you like removed? - ")
        blnItemRemoved = False 
        intRowNumber = 0
        while(intRowNumber < len(lstTable)):
            if(strKeyToRemove == str(list(dict(lstTable[intRowNumber]).values())[0])):
                del lstTable[intRowNumber]
                blnItemRemoved = True
            intRowNumber += 1
        if(blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("That task wasn't on the list.")

        print("The current tasks to do are:")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        continue 

    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            objFile = open(objFileName, "w")
            for dicRow in lstTable:
                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objFile.close()
            input("The tasks has been saved; press the enter key to continue.")
        else:
            input("The tasks have note been saved; press the enter key to continue.")
        continue
    elif (strChoice == '5'):
        if(input("Type 'exit' to leave the program:")): break #and Exit the program
        



