#==================================================================
# Coding Lab
# S121 - Demo Script
# An advanced To Do List (Using Objects)
#==================================================================
import pickle

class ToDoItem:
    def __init__(self, toDo, priority, dueDate):
        self.toDo = toDo
        self.priority = priority
        self.dueDate = dueDate

    def display(self):
        return (self.toDo + ", " + self.priority + " priority by " + self.dueDate)

    def update(self, field, newValue):
        oldToDo = self.display()
        if field == 1:
            self.toDo = newValue
        elif field == 2:
            self.priority = newValue
        elif field == 3:
            self.DueDate = newValue

        newToDo = self.display()
        print("Updated:\n" + oldToDo + "\nto:\n" + newToDo)
        

#=== Define Helper Functions ===

def promptUserForItem(promptMsg):
    errFlag = True
    while errFlag:
        try:
            itemSelected = int(input(promptMsg))
            errFlag = False
        except:
            print("Please enter a number")

    return itemSelected


#=== Main Program ===

filename = "todolist.pickle"

#==== Open To Do List File and Load into memory ===
try:
    f = open(filename, 'rb')
    toDoList = pickle.load(f)
    f.close()
except:
    print("Creating new file..")
    toDoList = []

#=== Run Program ===
    
runFlag = True
while runFlag:

    #=== Main program selection ===        
    response = input("""What do you want to do?
    C: Create a new to do item
    S: Display your to do list
    U: Update your to do list
    D: Delete an item from your to do list
    E: Exit program\n>>""")

    #=== Create new to do ===
    if response == "C":
        newToDo = input("What do you need to do?: ")
        newPriority = input("What is the priority?: ")
        newDueDate = input("When is the due date?: ")
        newToDoItem = ToDoItem(newToDo, newPriority, newDueDate)
        toDoList.append(newToDoItem)

    #=== Show to do list ===
    elif response == "S":

        if len(toDoList) == 0:
            print("You have nothing in your to do list")
        else:
            print("\nYour To Do Items are:")

            for i in range(0,len(toDoList)):
                print(str(i+1) + ") " + toDoList[i].display())

        print("")

    #=== Delete To Do Item ===
    elif response == "D":
        if len(toDoList) == 0:
            print("You have nothing in your do to list\n")
        else:
            itemToDel = promptUserForItem("Which item do you want to delete? (enter 0 to cancel): ")
            if itemToDel > len(toDoList) or itemToDel < 0:
                print("Item does not exist")
            elif itemToDel > 0:
                print("Deleting " + toDoList[itemToDel-1].toDo + "\n")
                del toDoList[itemToDel - 1]
            else:
                print("Cancelling delete. Nothing will be deleted")

    elif response == "U":
        if len(toDoList) == 0:
            print("You have nothing in your to do list\n")
        else:
            itemToUpdate = promptUserForItem("Which item do you want to update? (0 to cancel): ")

            if itemToUpdate > len(toDoList) or itemToUpdate < 0:
                print("Item does not exist")
            elif itemToUpdate > 0:
                validField = False
                while not validField:
                    fieldToUpdate =  promptUserForItem("Which field do you want to update?\n"
                                                     "1: To-Do description\n" 
                                                     "2: Priority\n"
                                                     "3: Due Date\n"
                                                     "0: to cancel update\n: " )

                    if fieldToUpdate == 0:
                        print("Cancelling update. Nothing will be updated")
                        validField = True
                    elif 1 <= fieldToUpdate <= 3:
                        newValue = input("What is the updated value?: ")
                        toDoList[itemToUpdate-1].update(fieldToUpdate, newValue)
                        validField = True
                    else:
                        print("Invalid selection. Please try again\n")
            else:
                print("Nothing will be updated\n")
    
                    
    
    #=== Exit Program ===                
    elif response == "E":
        print("Saving to file...")
        f = open(filename, 'wb')
        pickle.dump(toDoList, f)
        f.close()
        
        print("Exiting program...")
        runFlag = False
        
    else:
        print("Invalid input. Please try again\n")


