#==================================================================
# Using Pickle
# Loading multiple Variables/Objects 
#==================================================================

import pickle   

#=== Writing to file with Pickle ===

# Data to store
myShoppingList = ["Milk", "Pens", "Erasers", "Water"]
myStudyList = ["Math", "Physics"]
myPhoneNumber = 1234567

# Open the file with "wb" attribute
# Give the file name a .pickle extension identify it as pickle file
myFile = open("myData.pickle", "wb")

# Put the data into file
pickle.dump([myShoppingList, myStudyList, myPhoneNumber], myFile)

#=== Reading from Pickle File ===

# Open the file with "rb" attribute
myFile = open("myData.pickle", "rb")

# Load the data to an object (variable)
myData = pickle.load(myFile)

print(myData)



#=== Another way of loading multiple variables/objects using Pickle ===
import pickle   

# Data to store
myShoppingList = ["Milk", "Pens", "Erasers", "Water"]
myStudyList = ["Math", "Science"]

# Open the file with "wb"
myFile = open("data.pickle", "wb")

# Put the data into file
pickle.dump(myShoppingList, myFile)
pickle.dump(myStudyList, myFile)

myFile.close()

myFile = open("data.pickle", "rb")
line1 = pickle.load(myFile)
line2 = pickle.load(myFile)

print(line1)
print(line2)



