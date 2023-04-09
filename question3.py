from question2 import *
from question1 import *

matrix = getAdjacencyMatrix(getConsTable(15))
def detect0(matrix):
    adj_matrix = matrix
    for row in adj_matrix:
        print(row)

    num_rows = len(adj_matrix)
    num_cols = len(adj_matrix[0])
    finderrow = []
    findercol= []

    supprowcol=[]
    for col in range(num_cols):
        if col in findercol:
            continue
        # Check if the column has only 0's
        col_has_zeros = all(adj_matrix[row][col] == 0 for row in range(num_rows))
        if col_has_zeros:
            findercol.append(col)

    for row in range (num_rows):
        row_has_zeros = all(adj_matrix[row][col]==0 for col in range(num_cols))
        if row_has_zeros:
            finderrow.append(row)

    print("finderrow (row erased):", finderrow, )
    print("findercol (column erased):", findercol, )
    for i in range(len(findercol)):
        supprowcol.append(findercol[i])
    for i in range(len(finderrow)):
        supprowcol.append(finderrow[i])

    print("supprowcol :", supprowcol, )
    if len(supprowcol)==0:
        return False

    else:
        adj_matrix= remove_rowcol(adj_matrix,supprowcol)
        print("new matrix :")
        for i in adj_matrix:
            print(i)
        return True





def remove_rowcol(adj_matrix,supprowcol):
    # sort the list in descending order so that we remove the columns first, then the rows
    supprowcol.sort(reverse=True)
    # determine the number of rows and columns in the matrix
    num_rows = len(adj_matrix)
    num_cols = len(adj_matrix[0])
    # create a set of indices to remove (including duplicates)
    remove_indices = set(supprowcol)
    # remove columns first
    for col in sorted(remove_indices):
        if col < num_cols:
            for row in range(num_rows):
                if len(adj_matrix[row]) > col:
                    adj_matrix[row].pop(col)
    # remove rows
    for row in sorted(remove_indices):
        if row < num_rows:
            adj_matrix.pop(row)
    return adj_matrix








def remove_zeros(matrix):
    while detect0(matrix):
        pass
        print("redo loop")
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
        print("mutiple single points")
    else:
        print("only a single point")

def singleexitpoint(n):
    adj_matrix = getAdjacencyMatrix(getConsTable(n))
    countsigle = 0
    print("voici les exit points",adj_matrix[-1])
    for i in range(len(adj_matrix[-1])):
        countsigle += adj_matrix[-1][i]
    if countsigle > 1:
        print("mutiple exit points")
    else:
        print("only an exit point")
