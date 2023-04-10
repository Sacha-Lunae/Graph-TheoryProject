def getFile(n) : 
    fileName = "tables/" + str(n) + ".txt" 
    with open(fileName) as file : 
        return file.readlines()

def getConsTable(n) : 
    consTable = []
    for array in getFile(n):
        #The current array from getFile returns an array of strings, which is unuseable. Let's fix this.
        rightArray = []
        for element in array.split():
            #I only append the integers, which allows me to skip the \n
            rightArray.append(int(element))
        consTable.append(rightArray)
    return consTable
