from question2 import *
from question1 import *



matrix = getAdjacencyMatrix(getConsTable(1))
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
    running=True
    countrowcol = []
    countrowcol = initlabelrowcol(countrowcol, matrix)
    test=[]
    my_dict = {}
    cpt=countrowcol


    while running:
        try:
            print("NEW ITERATION")
            adj_matrix = matrix
            

            num_rows = len(adj_matrix)
            num_cols = len(adj_matrix[0])
            finderrow = []
            findercol = []

            for col in range(num_cols):
                if col in findercol:
                    continue
                # Check if the column has only 0's
                col_has_zeros = all(adj_matrix[row][col] == 0 for row in range(num_rows))
                if col_has_zeros:
                    findercol.append(col)

            for row in range(num_rows):
                row_has_zeros = all(adj_matrix[row][col] == 0 for col in range(num_cols))
                if row_has_zeros:
                    finderrow.append(row)


            # print("finderrow (row erased):", finderrow, )
            # print("findercol (column erased):", findercol, )
            for i in range(len(findercol)):
                finderrow.append(findercol[i])
            for i in range(len(finderrow)):
                findercol.append(finderrow[i])
            finderrow = list(set(finderrow + findercol))
            findercol = list(set(findercol + finderrow))

            #print("finderrow (row erased):", finderrow, )
            print("findercol (column erased):", findercol, n ,)
            if findercol== []:
                running = False

            test.append(findercol)


            if len(finderrow) == 0:
                running=False
                print("oute")
            if len(finderrow)<1:
                print("AHHHAHAHAHHAHAAHHAH")
                return matrix
            else:
                adj_matrix = remove_rowcol(adj_matrix, finderrow, findercol)
                print("new matrix :")
                for i in adj_matrix:
                    print(i)

        except IndexError:
            print("ATTENTION")
            return False
        pass

    for i in range(len(cpt)):
        my_dict[cpt[i]] = i
    for sublist in test:
        sublist.sort(reverse=True)

    # Erasing the value inside of the dictionary and re-initializing the values in ascending order
    for sublist in test:

        for item in sublist:

            if item in my_dict.values():
                key_to_delete = [key for key in my_dict if my_dict[key] == item][0]
                del my_dict[key_to_delete]
                i = 0
                for key in sorted(my_dict.keys()):
                    my_dict[key] = i
                    i += 1

            elif item > max(my_dict.values()):
                key_to_delete = max(my_dict.keys())
                del my_dict[key_to_delete]


    columns_affected= list(my_dict.keys())
    print("COLUMNS AFFECTED : ",columns_affected)
    print("final matrix !!")
    for i in matrix:
        print(i)
    return matrix



remove_zeros(matrix)







def singleentrypoint(n):
    adj_matrix = getAdjacencyMatrix(getConsTable(n))

    countsigle=0
    for i in range(len(adj_matrix[0])):
        countsigle+=adj_matrix[0][i]
    if countsigle>1:
        print(countsigle, " points into one")
    else:
        print("only a single point")

def singleexitpoint(n):
    adj_matrix = getAdjacencyMatrix(getConsTable(n))
    countsigle = 0
    print("voici les exit points",adj_matrix[-1])
    for i in range(len(adj_matrix[-1])):
        countsigle += adj_matrix[-1][i]
    if countsigle > 1:
        print(countsigle,"exit points into one")
    else:
        print("only an exit point")
