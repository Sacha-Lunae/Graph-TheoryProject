from question2 import *
from question1 import *



matrix =  getAdjacencyMatrix(11)
countrowcol= []







def remove_rowcol(adj_matrix, finderrow, findercol):
    # We sort out the row indices and the column indices so that we can erase them simpler next time
    row_indices = [row for row in range(len(adj_matrix)) if row in finderrow]
    col_indices = [col for col in range(len(adj_matrix[0])) if col in findercol]

    # putting the list in ascending order so we can remove the columns first and the the rows after
    row_indices.sort(reverse=True)
    col_indices.sort(reverse=True)
    # we remove the columns
    for col in col_indices:
        if col < len(adj_matrix[0]):
            for row in range(len(adj_matrix)):
                if len(adj_matrix[row]) > col:
                    adj_matrix[row].pop(col)
    #and then we remove the rows in this next loop
    for row in row_indices:
        if row < len(adj_matrix):
            adj_matrix.pop(row)
    return adj_matrix














def remove_zeros(matrix):

    #here is the attribution of the variables
    #running if for the while loop
    running=True
    countrowcol = []
    for i in range(len(matrix)):#we initialise the countrowcol variable to be the size of the matrix, which will help us to keep track for the whole operation
        countrowcol.append(i)

    test=[]#this variable will be log step by step the multiple or single row erasion in a 2d list
    my_dict = {}


    while running:
        try:
            columns_erased=0

            #we attribute the parameter of the function to a variable
            adj_matrix = matrix
            #if the matrix is a 0(1 row and column) , or only a 1, it will return false
            if adj_matrix == [[0]]or adj_matrix==[[1]]:
                return False

            #we attribute the counters for the next parts
            num_rows = len(adj_matrix)
            adj_matrix[0]
            num_cols = len(adj_matrix[0])
            finderrow = []
            findercol = []

            #these two loops will gather where is located the deleted row or column
            for col in range(num_cols):
                col_has_zeros = all(adj_matrix[row][col] == 0 for row in range(num_rows))#the all function will detect the columns that are full of 0
                if col_has_zeros:
                    findercol.append(col)#we will remember them if we append in the findercol variable
            for row in range(num_rows):
                row_has_zeros = all(adj_matrix[row][col] == 0 for col in range(num_cols))#the all function will detect the rows that are full of 0
                if row_has_zeros:
                    finderrow.append(row)#same here

            #for these two "for" conditions, we will fuse the informations of the columns and rows of 0 so that we can erase them later in the function remove_rowcol
            #IE: the finderrow and findercol are always equal because we are in a square matrix
            for i in range(len(findercol)):
                finderrow.append(findercol[i])
                columns_erased+=1#we are loggin the informations if a row or a columns is going to be erased
            for i in range(len(finderrow)):
                findercol.append(finderrow[i])
                columns_erased+=1#the logging is the same here

            finderrow = list(set(finderrow + findercol))
            findercol = list(set(findercol + finderrow))

            #now we append all of the columns/row that have been erased so that we can review them after
            test.append(findercol)
            #this is just a small check here if something gets wrong
            if adj_matrix == [[0]]:
                return False

            else:
                #this is where the columns and rows are erased simulaneousely
                adj_matrix = remove_rowcol(adj_matrix, finderrow, findercol)
                # now the columns_erased are put in good use here, if there is a cycle,
                # so that means we can break out of the infinite loop because no modification occurred
                if columns_erased==0:
                    break#we got out of the algorithm now
        except IndexError:
            return False
        pass

    #initialisation of the dictionary so that we have a mark of which columns/row is erased,
    # the dictionary will look like : {0:0, 1:1 [and so on]}
    for i in range(len(countrowcol)):
        my_dict[countrowcol[i]] = i
    #this is initializing the test function into an ascending order of the 2d list
    for sublist in test:
        sublist.sort(reverse=True)

    # This loop is erasing the value inside of the dictionary and after that it re-initialize the values in ascending order
    for sublist in test:#access the first dimension of the list
        for item in sublist:#accession the second dimension of the list, so that we can access the periodicly log of the erased columns
            if item in my_dict.values():
                key_to_delete = [key for key in my_dict if my_dict[key] == item][0]
                del my_dict[key_to_delete]#we delete the searched key
                #we now do a loop to reorganize the dictionnary, so we have ascending values so that we can avoid the IndexError
                i = 0
                for key in sorted(my_dict.keys()):
                    my_dict[key] = i
                    i += 1
            #if the value that we are trying to delete is not existing, we are fetching the last one (it usualy is)
            elif item > max(my_dict.values()):
                key_to_delete = max(my_dict.keys())
                del my_dict[key_to_delete]#deletion of the searched key
    #we store the keys of the dictionnary (the columns that remains) into a list
    columns_affected= list(my_dict.keys())
    return True, columns_affected



#remove_zeros(matrix)







def singleentrypoint(n):
    adj_matrix = getAdjacencyMatrix(n)
    positionsingle=[]
    countsigle=0
    # we are looking in the first row of the matrix,
    # were the successor of the alpha are located, which mean the entry points
    for i in range(len(adj_matrix[0])):
        countsigle += adj_matrix[0][i]#we log the number of entry points
        if adj_matrix[0][i] == 1:#here is to find if there is a 1
            positionsingle.append(i)
    if countsigle > 1:#if there are multiple entry points
        return False, positionsingle
    else:
        return True,positionsingle



def singleexitpoint(n):
    adj_matrix = getAdjacencyMatrix(n)
    positionsingle=[]
    countsigle=0
    #we are looking at the last column of the matrix, where the successor to omega are located
    for i in range(len(adj_matrix)):
        countsigle+=adj_matrix[i][-1]#we log the number of exit points
        if adj_matrix[i][-1]==1:#here is to find if there is a 1
            positionsingle.append(i)
    if countsigle>1:#if there are multiple exit points

        return False, positionsingle
    else:
        return True, positionsingle







def negative_edges(n):
    #we open the file
    fileName = "tables/" + str(n) + ".txt"
    with open(fileName) as file:
        for line in file:#we split the file into lines
            columns = line.split()#and we put those lines inside a 2d list
            if len(columns) > 1:#we check if there is more than one column

                second_column = int(columns[1])#we put the second column in a variable
                if second_column < 0:#if it is negative, it is printed
                    return False
    return True



