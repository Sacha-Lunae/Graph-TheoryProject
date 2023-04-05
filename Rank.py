import numpy as np
from question2 import *


def display_matrix(matrix):
    """
    Takes a 2D matrix as input and displays it in a clean and easily readable way, with "1" values printed in red.
    """
    ## Print the column indices at the top
    #for i in range(len(matrix[0])):
    #    print(str(i + 1), end=" ")
    #print()

    # Print the matrix rows, highlighting "1" values in red
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
        return ranklist
# { "1": 0,"5": 1,"4": 2, "2": 3,"6": 3,"3": 4,"7": 5, "8": 6}
# | [[],   [1], [1, 5], [1, 4], [4, 5], [2], [3, 5], [2, 4, 6, 7]] |
# | [[],   [1], [1, 5], [1, 2], [2, 5], [1], [4, 5], [1, 2, 6, 3]] |

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



#print(add_column_number(getAdjacencyMatrix(getConsTable(2))))
#display_matrix(getAdjacencyMatrix(getConsTable(4)))


#print(getAdjacencyMatrix(getConsTable(11)))

#print(find_rank(
    #    add_column_number(
    #   getAdjacencyMatrix(
#       getConsTable(11))),rank=0,ranklist={}))
#[[], [1], [1, 5], [1, 4], [4, 5], [2], [3, 5], [2, 4, 6, 7]]
