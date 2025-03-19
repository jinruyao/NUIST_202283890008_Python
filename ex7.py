# Author: Jinru Yao
# Using function

def studList(studentNames):
    # Print a list of students with "Evans" for each name
    for name in studentNames:
        print(name, "Evans")  

def addToList(studentNames, newName):
    # Returns the list with the new name added.
    return studentNames + [newName]

studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
print("The primary student list is:")
studList(studentNames)

studentNames = addToList(studentNames, "Mike")
print("\nThe later student list is:")
studList(studentNames)
