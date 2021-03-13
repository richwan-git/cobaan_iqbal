#==================================================================
# Let's Experiment with Try ... Except
# Demo/Practice 13
#==================================================================

#=== Execute this portion of the code if the file exists ===
try:
    file = open("myDataFile.txt")
    content  = file.read()
    print(content)
    
#=== Execute this portion of the code if myDataFile does not exist ===
except FileNotFoundError:
    print("The file does not exist")
