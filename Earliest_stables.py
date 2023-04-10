from Rank import *
from commonFunctionsEarlLate import hasSuccessorsVertex, rankDicoInlist, getDurationByVertex


def hasPredecessorsVertex(n, vertex):
    table = getConsTable(n)
    count = 0
    for i in range(len(table)):
        if table[i][0] == vertex:  # if the number in the column of vertex of table is equal to vertex
            for j in range(2, len(table[i])):  # thus for the same line
                count = count + 1  # count increases as much as there are predecessors
    return count


def getPredecessors(n, vertex):
    table = getConsTable(n)
    temp = []
    pred = []
    for i in range(len(table)):
        if table[i][0] == vertex:  # if the number in the column of vertex of table is equal to vertex
            temp.append(table[i][2:])  # thus for the same line, fill the temp list with predecessors
    # the following part permit to transform the temp (a 2D list) into a 1D list
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            pred.append(temp[i][j])
    return pred


def getPredecessorsOmega(n):
    table = getConsTable(n)
    pred = []
    for k in range(len(table)):
        if not hasSuccessorsVertex(n, table[k][0]):  # if a point has no successor in the file txt
            pred.append(table[k][0])  # thus, that means its successor is omega (here, omega = -2) so pred is filled with predecessors of omega
    return pred


def earliestByPredecessors(n):
    vertexRank = rankDicoInlist(n)  # list of vertex in order of ranks
    listTempo1 = []
    listTempo2 = {}
    listEarlPredFINAL = []
    for i in range(len(vertexRank)):  # for vertex list in rank order

        if vertexRank[i] == 0:  # if the vertex is alpha
            listTempo2.update({vertexRank[i]: 0})  # listTempo2 insert the duration 0 for alpha

        elif vertexRank[i] == -2:  # if the vertex is gamma
            Succ = getPredecessorsOmega(n)  # we get the predecessors of omega
            for j in range(len(Succ)):  # for those predecessors
                for cle, valeur in listTempo2.items():  # for cle and valeur in the dictionary listTempo2
                    if cle == Succ[j]:  # if cle is equal to one of the predecessors of omega
                        temp = valeur + getDurationByVertex(n, Succ[j])  # temp takes the duration at the predecessor + duration of the predecessor
                        listTempo1.append(temp)  # add temp in a temporary list listTempo1
            listTempo1.sort()  # sort the temporary list listTempo1
            final = listTempo1[len(listTempo1) - 1]  # final takes the biggest value in temporary list listTempo1
            listTempo1 = []  # empty the temporary list listTempo1
            listTempo2.update({vertexRank[i]: final})  # listTempo2 insert the final value

        elif hasPredecessorsVertex(n, vertexRank[i]) == 0:  # if the vertex is an entry
            listTempo2.update({vertexRank[i]: 0})  # the duration of the predecessor (alpha) is 0

        else:
            Succ = getPredecessors(n, vertexRank[i])  # we get the predecessors of the actual vertex
            for j in range(len(Succ)):
                for cle, valeur in listTempo2.items():
                    if cle == Succ[j]:
                        temp = valeur + getDurationByVertex(n, Succ[j])  # temp takes the duration at the predecessor + duration of the predecessor
                        listTempo1.append(temp)
            listTempo1.sort()
            final = listTempo1[len(listTempo1) - 1]
            listTempo1 = []
            listTempo2.update({vertexRank[i]: final})
    for valeur in listTempo2.values():  # for all earliest durations calculated
        listEarlPredFINAL.append(valeur)  # add them in a list
    return listEarlPredFINAL


def setDurationOrder(n):
    listPredecessors = setPredecessorsOrder(n)  # list of predecessors in order of ranks
    listEarlDura = []
    for i in range(len(listPredecessors)):
        newline = []
        for j in range(len(listPredecessors[i])):
            if listPredecessors[i][j] == 0:  # if the vertex is alpha
                newline.append(0)  # its duration is of 0
            elif listPredecessors[i][j] == -2:  # if the vertex is gamma
                break  # then go directly insert [] in listEarlDura
            else:
                dur = getDurationByVertex(n, listPredecessors[i][j])
                newline.append(dur)  # insert the duration of the actual vertex
        listEarlDura.append(newline)
    return listEarlDura


def setPredecessorsOrder(n):
    rankDico = find_rank(add_column_number(del_omega(getAdjacencyMatrix(n))), rank=0, ranklist={})  # list of vertex in order of ranks
    table = getConsTable(n)
    listPred = []
    listPredOmega = getPredecessorsOmega(n)
    for cle, val in rankDico.items():  # for cle (vertex) and val (rank) of the rank dictionaries
        if int(cle) == 0:  # if cle is equal to alpha
            listPred.append([])  # thus it has no predecessors so we insert [] in listPred

        elif int(cle) == -2:  # if cle is equal to gamma
            listPred.append(listPredOmega)  # listPred insert predecessors of omega

        for i in range(len(table)):  # for i in length of table
            if int(cle) == table[i][0]:  # if the vertex cle (display in order of ranks) is equal to a vertex in the table
                if hasPredecessorsVertex(n, int(cle)) == 0:  # if the vertex cle has no predecessors then
                    listPred.append([0])  # its predecessor is alpha
                else:
                    listPred.append(table[i][2:])  # insert predecessors of te vertex in the table
    return listPred


def displayEarliest(n):
    rankDico = find_rank(add_column_number(del_omega(getAdjacencyMatrix(n))), rank=0, ranklist={})  # dictionary containing vertex and their rank
    listRank = []
    listVertex = []
    for value in rankDico.values():
        listRank.append(value)  # get a list of ranks
    for key in rankDico.keys():
        listVertex.append(int(key))  # get a list of vertex in order of ranks

    listPred = setPredecessorsOrder(n)
    listEarlPredINIT = setDurationOrder(n)
    listEarlPredFINAL = earliestByPredecessors(n)

    print("Ranks             |", listRank, "|")  # display list of ranks
    print("Vertex            |", listVertex, "|")  # display list of vertex in order of ranks
    print("Predecessors      |", listPred, "|")  # display list of predecessors of vertex in order of ranks
    print("Initial duration  |", listEarlPredINIT, "|")  # display list of duration of each vertex without any calculation in order of ranks
    print("Earliest dates    |", listEarlPredFINAL, "|")  # display final list of duration of each vertex with calculations in order of ranks

