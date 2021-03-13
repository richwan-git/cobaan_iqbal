#==================================================================
# Let's Experiment with Using Pickle
# Demo/Practice - 12
#==================================================================

import pickle   

myShoppingList = ["Milk", "Pens", "Erasers", "Water"]

# Open the file with "wb"
myFile = open("shoppingList.txt", "wb")

# Put the data into file
pickle.dump(myShoppingList, myFile)

myFile.close()



