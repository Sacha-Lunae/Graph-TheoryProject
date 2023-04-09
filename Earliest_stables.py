from Rank import *
from commonFunctionsEarlLate import *


def hasPredecessorsVertex(matrix,
                          vertex):  # If you want to test the function: hasSuccessorsState(getConsTable(n), vertex)
    count = 0
    for i in range(len(matrix)):
        # for j in range(2, len(matrix[i])):
        if matrix[i][0] == vertex:
            for j in range(2, len(matrix[i])):
                count = count + 1
    return count


def getPredecessors(matrix, vertex):  # If you want to test the function: getPredecessors(getConsTable(n), vertex)
    temp = []
    pred = []
    for i in range(len(matrix)):
        if matrix[i][0] == vertex:
            temp.append(matrix[i][2:])
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            pred.append(temp[i][j])
    return pred


def getPredecessorsOmega(n,matrix):  # If you want to test the function: getPredecessors(getConsTable(n))
    pred = []

    for k in range(len(matrix)):
        if not hasSuccessorsVertex(getConsTable(n),matrix[k][0]):
            pred.append(matrix[k][0])
    return pred


def earliestByPredecessors(n, rankl):   # If you want to test the function: earliestByPredecessors(n,rankDicoInlist(find_rank(add_column_number(
                                        # del_omega(getAdjacencyMatrix(n))),rank=0,ranklist={})))
    listTempo1 = []
    listTempo2 = {}
    listEarlPredFINAL = []
    for i in range(len(rankl)):
        if rankl[i] == 0:
            listTempo2.update({rankl[i]:0})
        elif rankl[i] == -2:
            Succ = getPredecessorsOmega(n, getConsTable(n))
            for j in range(len(Succ)):
                for cle, valeur in listTempo2.items():
                    if cle == Succ[j]:
                        temp = valeur + getDurationByVertex(getConsTable(n), Succ[j])
                        listTempo1.append(temp)
            listTempo1.sort()
            final = listTempo1[len(listTempo1) - 1]
            listTempo1 = []
            listTempo2.update({rankl[i]: final})

        elif hasPredecessorsVertex(getConsTable(n), rankl[i]) == 0:
            listTempo2.update({rankl[i]: 0})

        else:
            Succ = getPredecessors(getConsTable(n), rankl[i])
            for j in range(len(Succ)):
                for cle, valeur in listTempo2.items():
                    if cle == Succ[j]:
                        temp = valeur + getDurationByVertex(getConsTable(n), Succ[j])
                        listTempo1.append(temp)
            listTempo1.sort()
            final = listTempo1[len(listTempo1)-1]
            listTempo1 = []
            listTempo2.update({rankl[i]: final})
    for valeur in listTempo2.values():
        listEarlPredFINAL.append(valeur)
    return listEarlPredFINAL


def setPredecessorsOrder(table,
                         rankDico):  # If you want to test the function: setPredecessorsOrder(getConsTable(n),find_rank(add_column_number(del_omega(getAdjacencyMatrix(11))),rank=0,ranklist={})))
    listPred = []
    for cle,val in rankDico.items():
        if int(cle) == 0:
            listPred.append([])
        elif int(cle) == -2:
            temp = val
            for key,values in rankDico.items():
                if values==temp-1:
                    listPred.append([key])
        for i in range(len(table)):
            if int(cle) == table[i][0]:
                if hasPredecessorsVertex(table, int(cle)) == 0:
                    listPred.append([0])
                else:
                    listPred.append(table[i][2:])
    return listPred

def setDurationOrder(n,
                     listPredecessors):  # If you want to test the function: setDurationOrder(n, setPredecessorsOrder(find_rank(add_column_number(del_omega(getAdjacencyMatrix(11))),rank=0,ranklist={}))))
    listEarlDura = []
    for i in range(len(listPredecessors)):
        newline = []
        for j in range(len(listPredecessors[i])):
            if listPredecessors[i][j] == 0:
                newline.append(0)
            else:
                dur = getDurationByVertex(getConsTable(n), listPredecessors[i][j])
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

    listPred = setPredecessorsOrder(getConsTable(n),
                                    find_rank(add_column_number(del_omega(getAdjacencyMatrix(n))), rank=0, ranklist={}))
    listEarlPredINIT = setDurationOrder(n, listPred)
    listEarlPredFINAL = earliestByPredecessors(n,rankDicoInlist(find_rank(add_column_number(del_omega(getAdjacencyMatrix(n))),rank=0,ranklist={})))

    print("|", listRank, "|")
    print("|", listVertex, "|")
    print("|", listPred, "|")
    print("|", listEarlPredINIT, "|")
    print("|", listEarlPredFINAL, "|")

#displayEarliest(2, find_rank(add_column_number(del_omega(getAdjacencyMatrix((2)))),rank=0,ranklist={}))
