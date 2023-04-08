import numpy as np
from question2 import *


def display_matrix(matrix):
    """
    Takes a 2D matrix as input and displays it in a clean and easily readable way, with "1" values printed in red.
    """

    for row in matrix:
        formatted_row = [("\033[91m" + str(element) + "\033[0m") if element == 1 else str(element) for element in row]
        print(" ".join(formatted_row))
    print("\n\n\n")


def add_column_number(matrix):
    # We find the number of columns
    num_cols = len(matrix[0])
    # We create a list of the number of the column
    lst = [i + 1 for i in range(num_cols)]
    # We add it to the begining of the matrix
    matrix.insert(0, lst)

    return matrix


def find_rank(matrix,rank,ranklist):

    display_matrix(matrix)

    if len(matrix) == 0 or all(len(row) == 0 for row in matrix):
        print(f"The rank of column number omega column is {rank}")
        ranklist['omega'] = rank
        return ranklist


    """
    Takes a 2D matrix as input, deletes all columns and rows with a sum of 0, and returns the modified matrix.
    """
    # Convert the matrix to a NumPy array
    matrix = np.array(matrix)

    # Calculate the sum of each column and add the index to a list if it is 0
    zero_sum_cols = []
    for col_index in range(matrix.shape[1]):
        col_sum = np.sum(matrix[1:, col_index])
        if col_sum == 0:
            if rank == 0:
                zero_sum_cols.append(col_index)
                print(f"The rank of column number alpha column is {rank}")
                ranklist.update({"alpha": rank})

            else:
                zero_sum_cols.append(col_index)
                print(f"The rank of column number {matrix[0][col_index]} column is {rank}")
                ranklist.update({matrix[0][col_index]:rank})

    # Delete the zero-sum columns from the matrix
    if len(zero_sum_cols) > 0:
        matrix = np.delete(matrix, zero_sum_cols, axis=1)

    # Find the unique row indices corresponding to the deleted columns
    zero_sum_rows = np.unique(zero_sum_cols)+1

    # Delete the corresponding rows from the modified matrix
    if len(zero_sum_rows) > 0:
        matrix = np.delete(matrix, zero_sum_rows, axis=0)

    matrix = matrix.tolist()


    # Return the modified matrix
    return find_rank(matrix,rank+1,ranklist)


def del_omega(matrix):
    new_matrix = [row[:-1] for row in matrix[:-1]]  # Remove last column and last row using list slicing
    return new_matrix


#print(add_column_number(getAdjacencyMatrix(getConsTable(2))))
#display_matrix(getAdjacencyMatrix(getConsTable(4)))


#print(display_matrix(getAdjacencyMatrix(
#            getConsTable(2))))



print(find_rank(
        add_column_number(
            del_omega(
                 getAdjacencyMatrix(
                    getConsTable(7)))),rank=0,ranklist={}))
