from earliestTables import *
from commonFunctionsEarlLate import *
from adjacency import *


def singleentrypoint(n):
    adj_matrix = getAdjacencyMatrix(n)
    positionsingle = []
    countsigle = 0
    for i in range(len(adj_matrix[0])):
        countsigle += adj_matrix[0][i]
        if adj_matrix[0][i] == 1:
            positionsingle.append(i)
    return positionsingle


def getSuccessors(n, vertex):
    table = getConsTable(n)
    succ = []
    for i in range(len(table)):
        for j in range(2, len(table[i])):
            if table[i][j] == vertex:  # if the vertex is a predecessor for others vertex
                succ.append(table[i][0])  # insert the vertex as a successor
    return succ


def setSuccessorsOrder(n):
    table = getConsTable(n)
    rankDico = find_rank(add_column_number(del_omega(getAdjacencyMatrix(n))), rank=0, ranklist={})  # list of vertex in order of ranks
    listSucc = []
    for cle in rankDico.keys():
        newline = []

        if int(cle) == -2:  # if cle is equal to gamma
            listSucc.append(newline)  # thus it has no predecessors, so we insert [] in listPred

        elif int(cle) == 0:  # if cle is equal to alpha
            listSucc.append(singleentrypoint(n))  # listPred insert successors of alpha

        elif hasSuccessorsVertex(n, int(cle)) == 0:  # if the vertex cle has no successors then
            newline.append(-2)  # its predecessor is gamma

        for i in range(len(table)):
            if int(cle) == table[i][0]:  # if a vertex cle is equal to a vertex (first column)
                for l in range(len(table)):
                    for m in range(2, len(table[l])):
                        if table[l][m] == int(cle):  # does this vertex appear as a predecessor in the file txt ? if yes then
                            newline.append(table[l][0])  # insert the vertex on the same line where there were a predecessor
                listSucc.append(newline)  # insert all successors
    return listSucc


def latestBySuccessors(n):
    listEarliest = earliestByPredecessors(n)  # list Earliest dates
    vertexRank = rankDicoInlist(n)  # list of vertex in order of ranks
    listTempo1 = []
    listTempo2 = {}
    listTempo3 = []
    listLateSuccFINAL = []
    departurePoint = listEarliest[
        len(listEarliest) - 1]  # assign the result of the last earliest duration (the biggest value in earliest)
    for i in range(len(vertexRank) - 1, -1, -1):  # we start backward
        if vertexRank[i] == 0:
            listTempo2.update({vertexRank[i]: 0})

        elif vertexRank[i] == -2:  # if the vertex is gamma
            listTempo2.update({vertexRank[i]: departurePoint})  # we insert at position gamma the value departurePoint (the result of the last earliest duration)

        elif hasSuccessorsVertex(n, vertexRank[i]) == 0:  # if the vertex is an exit
            listTempo2.update({vertexRank[i]: departurePoint - getDurationByVertex(n, vertexRank[i])})  # the duration of the predecessor of gamma is departurePoint - the duration of the vertex
        else:
            Succ = getSuccessors(n, vertexRank[i])  # we get the successors of omega
            for j in range(len(Succ)):  # for those successors
                for cle, valeur in listTempo2.items():
                    if cle == Succ[j]:  # if cle is equal to one of the successors of omega
                        temp = valeur - getDurationByVertex(n, vertexRank[i])  # temp takes the duration at the successor + duration of the successors
                        listTempo1.append(temp)
            listTempo1.sort()  # sort the temporary list listTempo1
            final = listTempo1[0]  # final take the smallest value in listTempo1
            listTempo1 = []
            listTempo2.update({vertexRank[i]: final})  # listTempo2 insert the final value
    for valeur in listTempo2.values():  # for all latest durations calculated
        listTempo3.append(valeur)  # add them in a list
    for i in range(len(listTempo3) - 1, -1, -1):  # reverse the list
        listLateSuccFINAL.append(listTempo3[i])
    return listLateSuccFINAL


def displayLatest(n):
    rankDico = find_rank(add_column_number(del_omega(getAdjacencyMatrix(n))), rank=0, ranklist={})  # dictionary containing vertex and their rank
    listRank = []
    listVertex = []
    for valeur in rankDico.values():
        listRank.append(valeur)
    for cle in rankDico.keys():
        listVertex.append(cle)

    listSucc = setSuccessorsOrder(n)
    listLateSuccINIT = setDurationOrder(n)
    listLateSuccFINAL = latestBySuccessors(n)

    print("Ranks             |", listRank, "|")  # display list of ranks
    print("Vertex            |", listVertex, "|")  # display list of vertex in order of ranks
    print("Successors        |", listSucc, "|")  # display list of successors of vertex in order of ranks
    print("Initial duration  |", listLateSuccINIT, "|")  # display list of duration of each vertex without any calculation in order of ranks
    print("Latest dates      |", listLateSuccFINAL, "|")  # display final list of duration of each vertex with calculations in order of ranks

def returnLatest(n):
    #Exact same function as above, I just need to transform the prints into returns for the traces - Sacha
    rankDico = find_rank(add_column_number(del_omega(getAdjacencyMatrix(n))), rank=0, ranklist={})  # dictionary containing vertex and their rank
    listRank = []
    listVertex = []
    for valeur in rankDico.values():
        listRank.append(valeur)
    for cle in rankDico.keys():
        listVertex.append(cle)

    listSucc = setSuccessorsOrder(n)
    listLateSuccINIT = setDurationOrder(n)
    listLateSuccFINAL = latestBySuccessors(n)
    
    return("Ranks             |" + str(listRank) + "| \nVertex            |" +str(listVertex)+
            "| \nSuccessors      |" + str(listSucc) + "| \nInitial duration  |"+ str(listLateSuccINIT)+
            "| \nLatest dates    |"+ str(listLateSuccFINAL)+ "|" )