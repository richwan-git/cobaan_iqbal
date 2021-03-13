#==================================================================
# Coding Lab
# S121 - Demo Script
# To Do List
#==================================================================
import pickle


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
    D: Delete an item from your to do list
    E: Exit program\n>>""")

    #=== Create new to do ===
    if response == "C":
        newToDo = input("What do you need to do?: ")
        toDoList.append(newToDo)

    #=== Show to do list ===
    elif response == "S":

        if len(toDoList) == 0:
            print("You have nothing in your to do list")
        else:
            print("\nYour To Do Items are:")

            for i in range(0,len(toDoList)):
                print(str(i+1) + ") " + toDoList[i])

        print("")

    #=== Delete To Do Item ===
    elif response == "D":
        if len(toDoList) == 0:
            print("You have nothing in your do to list\n")
        else:
            errFlag = True
            while errFlag:
                try:
                    itemToDel = int(input("Which item do you want to delete? (Enter 0 to cancel): "))
                    errFlag = False
                except:
                    print("Please enter a number")

            if itemToDel > len(toDoList) or itemToDel < 0:
                print("Item does not exist")
            elif itemToDel > 0:
                print("Deleting " + toDoList[itemToDel-1] + "\n")
                del toDoList[itemToDel - 1]
            else:
                print("Cancelling delete. Nothing will be deleted")
    
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


