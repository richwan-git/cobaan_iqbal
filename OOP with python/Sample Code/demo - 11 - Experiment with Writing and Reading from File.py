#==================================================================
# Let's Experiment with Writing and Reading from a File
# Demo/Practice 11
#==================================================================

#=== Open file myDataFile.txt for writing ===
dataFile = open("myDataFile.txt", "w")
#=== To store numbers, you need to convert them to strings ===
number = 34
dataFile.write(str(number))
dataFile.write("This is my data file which I am able to write to\n")
dataFile.close()

#=== Open myDataFile.txt for reading only ===
dataFile = open("myDataFile.txt", "r")
content = dataFile.read()
print("Content of file is:\n" + content)

#=== Open myDataFile.txt for appending ===
dataFile = open("myDataFile.txt", "a")
additionalContent = ""
for i in range(0,5):
    additionalContent = additionalContent + "this is line " + str(i) + ".\n"
dataFile.write(additionalContent)
dataFile.close()

#=== Open file for reading and read line by line ===
dataFile = open("myDataFile.txt", "r")
fileInList = []
line = dataFile.readline()
while line:
    fileInList.append(line)
    line = dataFile.readline()
dataFile.close()
print(fileInList)
