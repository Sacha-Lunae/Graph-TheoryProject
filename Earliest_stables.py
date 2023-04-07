from Rank import *
import numpy as np

"""rankDico=find_rank(
    add_column_number(
        getAdjacencyMatrix(
            getConsTable(11))),rank=0,ranklist={})"""

rankDico = {"1": 0, "5": 1, "4": 2, "2": 3, "6": 3, "3": 4, "7": 5, "8": 6}


def globalDurations(graph):  # If you want to test the function: globalDurations(getConsTable(11)
    durations = []
    for i in range(len(graph)):
        durations.append(graph[i][1])

    durations.insert(0, 0)
    durations.append(0)
    return durations


def earliestByPredecessorsUsingBellman(graph,
                                       durations):  # If you want to test the function: earliestByPredecessorsUsingBellman(
    # getAdjacencyMatrix(getConsTable(11)),globalDurations(getConsTable(11)))
    n = len(graph)
    dist = [float('-inf')] * n
    dist[0] = 0
    for i in range(n - 1):
        for u in range(n):
            for v in range(n):
                if graph[u][v] != 0:
                    if dist[v] < dist[u] + durations[u]:
                        dist[v] = dist[u] + durations[u]
    return np.sort(dist)


def getDurationByVertex(table, vertex):  # If you want to test the function: getDurationByVertex(getConsTable(n),vertex)
    for i in range(len(table)):
        if not vertex:
            duration = table[i][1]
            return duration
        if table[i][0] == vertex:
            duration = table[i][1]
            return duration


def setPredecessorsOrder(table):  # If you want to test the function: setPredecessorsOrder(getConsTable(n))
    listPred = []
    for cle in rankDico.keys():
        for i in range(len(table)):  # getAdjacencyMatrix(getConsTable(11))))
            if int(cle) == table[i][0]:
                listPred.append(table[i][2:])
    return listPred


def setDurationOrder(n, listPredecessors):  # If you want to test the function: setDurationOrder(n, setPredecessorsOrder(rankDico))
    listEarlDura = []
    for i in range(len(listPredecessors)):
        newline = []
        if listPredecessors[i] == 0:
            newline.append(0)
            listEarlDura.append(newline)
        for j in range(len(listPredecessors[i])):
            dur = getDurationByVertex(getConsTable(n),listPredecessors[i][j])
            newline.append(dur)
        listEarlDura.append(newline)
    return listEarlDura


def displayEarliest(n, Ranklist):  # If you want to test the function: displayEarliest(n, rankDico)
    listRank = []
    listVertex = []  # Comment on appelle les états en anglais ?
    for value in Ranklist.values():
        listRank.append(value)
    for key in Ranklist.keys():
        listVertex.append(int(key))

    listPred = setPredecessorsOrder(getConsTable(n))
    listEarlPredINIT = setDurationOrder(n, listPred)
    listEarlPredFINAL = earliestByPredecessorsUsingBellman(getAdjacencyMatrix(getConsTable(n)),
                                                           globalDurations(getConsTable(n)))


    print("|", listRank, "|")
    print("|", listVertex, "|")
    print("|", listPred, "|")
    print("|", listEarlPredINIT, "|")
    print("|", listEarlPredFINAL, "|")


displayEarliest(11, rankDico)
