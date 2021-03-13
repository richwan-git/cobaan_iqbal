#==================================================================
# Coding Lab
# S121 - Demo Script
# Create a Class
#==================================================================

#=== Define a Class named Rectangle ===
class Rectangle(object):

    #=== Initializer ===
    def __init__(self, width, height):
        self.width = width
        self.height = height

    #=== Define Method ===
    def resize(self, factor):
        self.width = self.width * factor
        self.height = self.height * factor

    #=== Method to return paremeter length ===       
    def perimeter(self):
        return (self.width + self.height) * 2

    #=== Method to return the area ===
    def area(self):
        return self.width * self.height
        
        
#=== Create an Instance ===
smallRect = Rectangle(4, 6)

#=== Accessing the attributes ===
print("The width of smallRect: " + str(smallRect.width))
print("The height of smallRect: " + str(smallRect.height))
print("The area of smallRect: " + str(smallRect.area()))


#=== Calling a Method ===
smallRect.resize(1.5)

print("The updated width of smallRect: " +str(smallRect.width))
print("The updated height of smallRect: " +str(smallRect.height))
print("The updated area of smallRect: " + str(smallRect.area()))
#=== Calling a Method with return value ===
perimeter = smallRect.perimeter()
print("The perimeter of smallRect is: " + str(perimeter))


