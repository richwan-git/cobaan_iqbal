#==================================================================
# Create a program: A Simple School Database
#==================================================================

import pickle

class Person:
    def __init__(self, firstName, lastName, id):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id

    def getFullName(self):
        return self.firstName + " " + self.lastName

    def getFullInfo(self):
        return "Name: " + self.getFullName() + " | ID: " + self.id

class Teacher (Person):
    def __init__(self, firstName, lastName, id, staffId, department):
        Person.__init__(self, firstName, lastName, id)
        self.staffId = staffId
        self.department = department

    def getFullInfo(self):
        return super().getFullInfo() + " | Staff ID: " + self.staffId + " | Department: " + self.department

class Student (Person):
    def __init__(self, firstName, lastName, id, staffId, formClass):
        Person.__init__(self, firstName, lastName, id)
        self.studentId = staffId
        self.formClass = formClass

    def getFullInfo(self):
        return super().getFullInfo() + " | Student ID: " + self.studentId + " | Form Class: " + self.formClass

#==========================================================================
# Main Program 
#==========================================================================
dbFileName = "schoolDB.pickle"


#==============================================================
# Load data from pickle data file 
#==============================================================


try:  
    myFile = open(dbFileName, "rb")
    teachersList = pickle.load(myFile)
    studentsList = pickle.load(myFile)
except:
    teachersList = []
    studentsList = []

flagToDo = ""

while flagToDo != "E":
    flagToDo = input("""\nWhat do you want to do? Choose from the following option:
        E - Exit
        A - Add
        S - Show List in Database
        D - Delete an entry
        U - Update an entry
    >>""")    

    #------------------------------------------------
    # User Chose to Exit
    #------------------------------------------------
    if flagToDo == "E":
        # --- Write data to file ---
        print("Please wait, saving data to disk...")
        myFile = open(dbFileName, "wb")
        pickle.dump(teachersList, myFile)
        pickle.dump(studentsList, myFile)
        print("Saving completed. Thank You for using our system ")

    #------------------------------------------------
    # Show Lists
    #------------------------------------------------    
    elif flagToDo == "S":
        flagListToShow = ""

        while not(flagListToShow == "S" or flagListToShow == "T"):
            flagListToShow = input("""\nWhich list do you want to show? Choose from the following options:
                S - Students
                T - Teachers
            >>""")
            
            if flagListToShow == "S":
                listToShow = studentsList
                print("=== List of Students ===")
            elif flagListToShow == "T":
                listToShow = teachersList
                print("=== List of Teachers ===")
            else:
                print("Invalid selection. Please try again")

        if bool(listToShow):
            i = 1
            for entry in listToShow:
                print(str(i) + ")" + entry.getFullInfo() )
                i += 1 

    #------------------------------------------------
    # Add Entries
    #------------------------------------------------  
    elif flagToDo == "A":
        flagEntryTypeToAdd = ""
        
        while not(flagEntryTypeToAdd == "S" or flagEntryTypeToAdd == "T" ):
            flagEntryTypeToAdd = input("""Which entry do you want to add? Choose from the following options:
                S - Students
                T - Teachers
            >>""")

            # === Add Student ====
            if flagEntryTypeToAdd == "S": 
                newFirstName = input("Student's First Name: ")
                newLastName = input("Student's Last Name: ")
                newID = input("Student's National ID: ")
                newStudentID = input("Student's School ID: ")
                newStudentFormClass = input("Student's Form Class: ")
                
                newStudent = Student(newFirstName, newLastName, newID, newStudentID, newStudentFormClass)
                studentsList.append(newStudent)

            # === Add Teacher ====
            elif flagEntryTypeToAdd == "T":
                newFirstName = input("Teacher's First Name: ")
                newLastName = input("Teacher's Last Name: ")
                newID = input("Teacher's National ID: ")
                newTeacherID = input("Teacher's School ID: ")
                newTeacherDept = input("Teacher's Department: ")
                
                newTeacher = Student(newFirstName, newLastName, newID, newTeacherID, newTeacherDept)
                teachersList.append(newTeacher)

            else:
                print("Invalid input. Please try again")
        
    #------------------------------------------------
    # Delete Entries
    #------------------------------------------------  
    elif flagToDo == "D":
        flagListToDel = ""
        while not(flagListToDel == "S" or flagListToDel == "T"):
            flagListToDel = input("""\nWhich list do you want to delete from? Choose from the following options:
                S - Students
                T - Teachers
            >>""")
            if flagListToDel == "S":
                listToDel = studentsList
            elif flagListToDel == "T":
                listToDel = teachersList
            else:
                print("Invalid selection. Please try again")

        try:
            entryToDel = int(input("Which entry do you wish to delete?: "))
            if 0 < entryToDel <= len(listToDel):
                tempEntry = listToDel[entryToDel-1].getFullInfo()
                del listToDel[entryToDel-1]
                print("Deleting: " + tempEntry)
        except: 
            print("Invalid entry. Please enter a number")

    elif flagToDo == "U":
        print ("\nFeature currently not supported\n ")
    else:
        print ("Invalid selection. Please try again")





