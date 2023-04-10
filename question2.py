from question1 import *
from prettyTables import * 

def swapMatrix(matrix) :
    #the following function puts the rows in the lines and vice-versa
    n = len(matrix)
    # we fill the new matrix with 0
    swapped = [[0 for j in range(n)] for i in range(n)]
    #We go through the whole matrix and we inverse lines and columns
    for i in range(n):
        for j in range(n):
            swapped[j][i] = matrix[i][j]
    return swapped


def alphaOmega(matrix):
    #The logic behind this : if there are only 0's (= if there are no predecessors/successors, depending on when we use the function)
    #we add 1 at the end (to indicate that alpha is the predecessor / omega is the sucessor)
    alphaOmega = []
    for i, line in enumerate(matrix):
        if all(element == 0 for element in line):
            alphaOmega.append(1)
        else :
            alphaOmega.append(0)
    return alphaOmega

def getAdjacencyMatrix(graphNum):
    consTable = getConsTable(graphNum)
    numberOfVertices = len(consTable)
    #Setting up the 2D matrix
    adjacency_matrix = [[0] * numberOfVertices for i in range(numberOfVertices)]

    #We run a loop through each vertice
    for vertice in range(numberOfVertices):
        #We run another loop through each constraint
        for constraint in range(2, len(consTable[vertice])):
            #We add the '-1' because python indexes begin at 0
            adjacency_matrix[vertice][consTable[vertice][constraint] - 1] = 1

    #Initialization of the alpha row
    alpha = alphaOmega(adjacency_matrix)

    #Swapping the matrix
    adjacency_matrix = swapMatrix(adjacency_matrix)

    #Initialization of the omega row
    omega = alphaOmega(adjacency_matrix)

    #Insertion of alpha at the begenning of the matrix
    adjacency_matrix.insert(0, alpha)

    #Insertion of omega at the end of the matrix
    adjacency_matrix.append(omega)


    for i in range (len(adjacency_matrix)) : 
        #Make sure that the first column is only 0's (by inserting 0's at the beginning of each row)

        adjacency_matrix[i].insert(0,0)

        if all(element == 0 for element in adjacency_matrix[i]):
                adjacency_matrix[i].append(1)
        else : 
            adjacency_matrix[i].append(0)


    for i in range (len(adjacency_matrix)) :
        #Make sure that the last row is only 0's
        if adjacency_matrix[-1][i] == 1 :
            adjacency_matrix[-1][i] = 0

    return adjacency_matrix
        
def getWeights(graphNum) :
    graph = getConsTable(graphNum)
    weights = []
    for i in range (len(graph)) :
        weights.append(graph[i][1])

    weights.insert(0,0)
    weights.append(0)

    return weights


def bellman(graphNum):
    graph = getAdjacencyMatrix(graphNum)
    weights = getWeights(graphNum)
    n = len(graph)

    #initialisation de l'algo de bellman
    dist = [float('-inf')] * n
    dist[0] = 0


    for i in range(n - 1):
        for u in range(n):
            for v in range(n):
                if graph[u][v] == 1:
                    if dist[v] < dist[u] + weights[u]:
                        dist[v] = dist[u] + weights[u]

    return dist


prettyAdjacency(getAdjacencyMatrix(11))