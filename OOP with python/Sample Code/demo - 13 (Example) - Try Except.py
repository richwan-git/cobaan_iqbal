#==================================================================
# Try ... Except
#==================================================================

#=== simple use of try ... except ===
userInput = input("Please enter your birth year: ")
try:
    birthYear = int(userInput)
    print("Your age is: " + str(2018 - birthYear))
except:
    print("You need to enter a number")

#=== Keep checking until a correct input is received ===

errFlag = True
while errFlag:
    try:
        birthYear = int(input("Please enter your birth year: "))
        errFlag = False
    except:
        print("You must enter an integer")

print("Your age is " + str(2017 - birthYear))

