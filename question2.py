from question1 import *

def swapMatrix(matrix) :
    #the following function puts the rows in the lines and vice-versa
    n = len(matrix)
    # we fill the new matrix with 0
    swapped = [[0 for j in range(n)] for i in range(n)]
    # parcourir la matrice d'origine et inverser les lignes et colonnes
    for i in range(n):
        for j in range(n):
            swapped[j][i] = matrix[i][j]
    return swapped


def alphaOmega(matrix):
    alphaOmega = []
    for i, line in enumerate(matrix):
        if all(element == 0 for element in line):
            alphaOmega.append(1)
        else :
            alphaOmega.append(0)
    return alphaOmega

def getAdjacencyMatrix(consTable):
    numberOfVertices = len(consTable)
    #Setting up the 2D matrix
    adjacency_matrix = [[0] * numberOfVertices for i in range(numberOfVertices)]

    #We run a loop through each vertice
    for vertice in range(numberOfVertices):
        #We run another loop through each constraint
        for constraint in range(2, len(consTable[vertice])):
            #We add the '-1' because python indexes begin at 0
            adjacency_matrix[vertice][consTable[vertice][constraint] - 1] = 1

    alpha = alphaOmega(adjacency_matrix)
    adjacency_matrix = swapMatrix(adjacency_matrix)
    omega = alphaOmega(adjacency_matrix)
    adjacency_matrix.insert(0, alpha)
    adjacency_matrix.append(omega)


    for i in range (len(adjacency_matrix)) : 

        adjacency_matrix[i].insert(0,0)


        if all(element == 0 for element in adjacency_matrix[i]):
            adjacency_matrix[i].append(1)
        else : 
            adjacency_matrix[i].append(0)

    return adjacency_matrix
        
def weights(graph) :
    weights = []
    for i in range (len(graph)) :
        weights.append(graph[i][1])

    weights.insert(0,0)
    weights.append(0)

    return weights


def bellman(graph, weights):
    n = len(graph)
    dist = [float('-inf')] * n
    dist[0] = 0
    for i in range(n - 1):
        for u in range(n):
            for v in range(n):
                if graph[u][v] != 0:
                    if dist[v] < dist[u] + weights[u]:
                        dist[v] = dist[u] + weights[u]

    return dist


print (weights(getConsTable(11)))
print(bellman(getAdjacencyMatrix(getConsTable(11)), weights(getConsTable(11))))
    


#print(bellman_ford(getAdjacencyMatrix(getConsTable((11))), weights(getConsTable(11)), 0))


