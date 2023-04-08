from Earliest_stables import *

ranklist = {"1": 0, "5": 1, "4": 2, "2": 3, "6": 3, "3": 4, "7": 5, "8": 6}
listPred = [[], [1], [1, 5], [1, 4], [4, 5], [2], [3, 5], [2, 4, 6, 7]]
rankl = [1, 5, 4, 2, 6, 3, 7, 8]


def getSuccessors(matrix, vertex):  # If you want to test the function: getSuccessors(getConsTable(n), vertex)
    succ = []
    for i in range(len(matrix)):
        for j in range(2, len(matrix[i])):
            if matrix[i][j] == vertex:
                succ.append(matrix[i][0])
    return succ


def hasSuccessorsState(matrix, vertex):  # If you want to test the function: hasSuccessorsState(getConsTable(n), vertex)
    count = 0
    for i in range(len(matrix)):
        for j in range(2, len(matrix[i])):
            if matrix[i][j] == vertex:
                count = count + 1
    return count


def setSuccessorsOrder(matrix):  # If you want to test the function: set_successors_order(getConsTable(n))
    listSucc = []
    for cle in ranklist.keys():
        newline = []
        for i in range(len(matrix)):  # getAdjacencyMatrix(getConsTable(11))))
            if int(cle) == matrix[i][0]:
                for l in range(len(matrix)):
                    for m in range(2, len(matrix[l])):
                        if matrix[l][m] == int(cle):
                            newline.append(matrix[l][0])
                listSucc.append(newline)
    return listSucc


def latestBySuccessors(n, listEarliest):    # If you want to test the function: latestBySuccessors(n,earliestByPredecessorsUsingBellman(
                                            # getAdjacencyMatrix(getConsTable(n)),globalDurations(getConsTable(n))))
    listTempo1 = []
    listTempo2 = {}
    listTempo3 = []
    listLateSuccFINAL = []
    departurePoint = listEarliest[len(listEarliest) - 1]
    for i in range(len(rankl) - 1, -1, -1):
        if hasSuccessorsState(getConsTable(n), rankl[i]) == 0:
            listTempo2.update({rankl[i]: departurePoint - getDurationByVertex(getConsTable(n), rankl[i])})
        else:
            Succ = getSuccessors(getConsTable(n), rankl[i])
            for j in range(len(Succ)):
                for cle, valeur in listTempo2.items():
                    if cle == Succ[j]:
                        temp = valeur - getDurationByVertex(getConsTable(n), rankl[i])
                        listTempo1.append(temp)
            listTempo1.sort()
            print("listtempo", listTempo1)
            final = listTempo1[0]
            listTempo1 = []
            listTempo2.update({rankl[i]: final})
    for valeur in listTempo2.values():
        listLateSuccFINAL.append(valeur)
     for i in range(len(listTempo3)-1,-1,-1):
        listLateSuccFINAL.append(listTempo3[i])
    return listLateSuccFINAL


def display_latest(n, matrix):
    listRank = []
    listVertex = []
    for valeur in matrix.values():
        listRank.append(valeur)
    for cle in matrix.keys():
        listVertex.append(cle)

    listSucc = setSuccessorsOrder(getConsTable(n))
    listLateSuccINIT = setDurationOrder(n, listSucc)
    listLateSuccFINAL = latestBySuccessors(n, earliestByPredecessorsUsingBellman(getAdjacencyMatrix(getConsTable((n))),
                                                                                globalDurations(getConsTable(n))))

    print("|", listRank, "|")
    print("|", listVertex, "|")
    print("|", listSucc, "|")
    print("|", listLateSuccINIT, "|")
    print("|", listLateSuccFINAL, "|")


display_latest(11, ranklist)
