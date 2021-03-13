#==================================================================
# Let's Experiment with Overriding
# Demo/Practice - 42
# Demonstration of inheritance with Person-Student-Teacher
# Person is the superclass
# Student and Teacher is a subclass of person and inherits from Person
#==================================================================

#==================================================================
# Define the Person class
# Each person object will have three attributes: 
#   (1) First Name
#   (2) Last Name
#   (3) National ID number
#==================================================================

class Person:
    def __init__(self, first, last, id):
        self.firstName = first
        self.lastName = last
        self.id = id

    def getFullName(self):
        return self.firstName + " " + self.lastName

    def getFullInfo(self):
        return self.firstName + " " + self.lastName + ", ID: " + self.id

#==================================================================
# Define the Teacher Class
# Each teacher object will have five attributes: 
#   (1) First Name
#   (2) Last Name
#   (3) National ID number
#   (4) Teacher ID
#   (5) Department
# Attribute (1) - (3) are exactly the same as that of a person
#==================================================================

class Teacher(Person):
    def __init__(self, first, last, id, teacherId, department):
        Person.__init__(self, first, last, id)
        self.teacherId = teacherId
        self.department = department

    #=== Overriding the getFullInfor method in the baseclass === 
    def getFullInfo(self):
        return super().getFullInfo() + " " + self.teacherId + " from " + self.department + " department"

    

#==================================================================
# Main Program
#==================================================================

#-----------------------------------------------------
# Create instances of a person and a teacher
#-----------------------------------------------------
julius = Person("Julius", "Ang", "S12345678")
teacherSharon = Teacher("Sharon", "Tze", "S12345679", "CL001", "Math")

#-----------------------------------------------------
# Demonstrate that getFullName() method is also available in the teacher instance
# even though we didn't write that method
#-----------------------------------------------------
print("The full name of the student is " + str(julius.getFullName()))
print("The full name of the teacher is " + str(teacherSharon.getFullName()))
print("============")

#-----------------------------------------------------
# For Python, the instance variable can be accessed directly
# unlike other OO programs like Java, "Private" instance variables don't exist
# A convention is using double underscore to prevent access
# We will not cover that in this course
#-----------------------------------------------------

print("The first name of the student is " + str(julius.firstName))
print("The first name of the teacher is " + str(teacherSharon.firstName))
print("============")

#-----------------------------------------------------
# We can even directly write to the instance variable
#-----------------------------------------------------
julius.firstName = "New Julius"
print("The updated full name of the student is " + str(julius.getFullName()))
print("============")

#-----------------------------------------------------
# Demonstrate overriding of method
#-----------------------------------------------------
print("The student's information: " + str(julius.getFullInfo()))
print("The teacher's information: " + str(teacherSharon.getFullInfo()))
print("============")
