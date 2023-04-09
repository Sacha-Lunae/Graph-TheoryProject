from question2 import *
from question1 import *



matrix =  getAdjacencyMatrix(6)
countrowcol= []

def initlabelrowcol(countrowcol, adj_matrix):
    for i in range(len(adj_matrix)):
        countrowcol.append(i)
    return countrowcol





def remove_rowcol(adj_matrix, finderrow, findercol):
    # separate row indices and column indices
    row_indices = [row for row in range(len(adj_matrix)) if row in finderrow]

    col_indices = [col for col in range(len(adj_matrix[0])) if col in findercol]

    # sort the lists in descending order so that we remove the columns first, then the rows
    row_indices.sort(reverse=True)
    col_indices.sort(reverse=True)
    # remove columns first
    for col in col_indices:
        if col < len(adj_matrix[0]):
            for row in range(len(adj_matrix)):
                if len(adj_matrix[row]) > col:
                    adj_matrix[row].pop(col)
    # remove rows
    for row in row_indices:
        if row < len(adj_matrix):
            adj_matrix.pop(row)
    return adj_matrix














def remove_zeros(matrix):

    #here is the attribution of the variables
    #running if for the while loop
    running=True
    countrowcol = []
    countrowcol = initlabelrowcol(countrowcol, matrix)
    test=[]
    my_dict = {}
    cpt=countrowcol


    while running:
        try:
            columns_erased=0
            print("\n")
            #we attribute the parameter of the function to a variable
            adj_matrix = matrix
            #we print the matrix
            for i in adj_matrix:
                print(i)
            #if the matrix is a 0(1 row and column) , or only a 1, it will return false
            if adj_matrix == [[0]]or adj_matrix==[[1]]:
                print("connection terminated")
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

            #this line is a debug line
            #print("findercol (column erased):", findercol)

            #now we append all of the columns/row that have been erased so that we can review them after
            test.append(findercol)
            #this is just a small check here if something gets wrong
            if adj_matrix == [0]:
                return False

            else:#this is where the columns and rows are erased simulaneousely
                adj_matrix = remove_rowcol(adj_matrix, finderrow, findercol)
                if columns_erased==0:#now the columns_erased are put in good use here, if there is a cycle, so that means we can break out of the infinite loop because no modification occured
                    break#we got out of the algorithm now
        except IndexError:
            print("ATTENTION")
            return False
        pass

    #initialisation of the dictionnary so that we have a mark of which columns/row is erased, the dictionnary will look like : {0:0, 1:1 [and so on]}
    for i in range(len(cpt)):
        my_dict[cpt[i]] = i
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
    print("COLUMNS AND ROWS AFFECTED : ",columns_affected)
    print("final matrix :")
    for i in matrix:
        print(i)
    return True, columns_affected



remove_zeros(matrix)







def singleentrypoint(n):
    adj_matrix = getAdjacencyMatrix(n)
    positionsingle=[]
    countsigle=0
    for i in range(len(adj_matrix[0])):
        countsigle += adj_matrix[0][i]
        if adj_matrix[0][i] == 1:
            positionsingle.append(i)
    if countsigle > 1:
        print(countsigle, "points into one at position :", positionsingle)
    else:
        print("only a single entry point :")
        print(positionsingle)


def singleexitpoint(n):
    adj_matrix = getAdjacencyMatrix(n)
    positionsingle=[]
    countsigle=0
    for i in range(len(adj_matrix)):
        countsigle+=adj_matrix[i][-1]
        if adj_matrix[i][-1]==1:
            positionsingle.append(i)
    if countsigle>1:
        print(countsigle, " points merge into one at :", positionsingle)
    else:
        print("only a single exit point at :" ,positionsingle)



for i in matrix:
    print(i)
#singleentrypoint(12)

def is_scheduling_graph(graph_matrix):
    # Iterate through each vertex in the graph
    for vertex in range(len(graph_matrix)):
        # Get the weights of all outgoing edges of the vertex
        outgoing_weights = set([graph_matrix[vertex][j] for j in range(len(graph_matrix)) if graph_matrix[vertex][j] != 0])

        # Check if all outgoing edges have the same weight
        if len(outgoing_weights) != 1:
            print("heh you failed")
            return False

    # If all vertices satisfy the condition, return True
    print("YOLO TRUEEEE")
    return True



def outgoingzero(graph_matrix):
    # Check if the entry vertex has any outgoing edges
    if any(graph_matrix[0][j] != 0 for j in range(1, len(graph_matrix))):
        print("false begin")
        return False

    # Iterate through each vertex in the graph except for the entry vertex
    for vertex in range(1, len(graph_matrix)):
        # Get the weights of all outgoing edges of the vertex
        outgoing_weights = set([graph_matrix[vertex][j] for j in range(len(graph_matrix)) if graph_matrix[vertex][j] != 0])

        # Check if all outgoing edges have the same weight
        if len(outgoing_weights) != 1:
            print("NO")
            return False

    # If all vertices satisfy the conditions, return True
    print("YEAH")
    return True

