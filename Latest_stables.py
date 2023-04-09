from Earliest_stables import *

def singleentrypoint(n):
    adj_matrix = getAdjacencyMatrix(n)
    positionsingle=[]
    countsigle=0
    for i in range(len(adj_matrix[0])):
        countsigle += adj_matrix[0][i]
        if adj_matrix[0][i] == 1:
            positionsingle.append(i)
    return positionsingle


def getSuccessors(matrix, vertex):  # If you want to test the function: getSuccessors(getConsTable(n), vertex)
    succ = []
    for i in range(len(matrix)):
        for j in range(2, len(matrix[i])):
            if matrix[i][j] == vertex:
                succ.append(matrix[i][0])
    return succ


def setSuccessorsOrder(n,matrix, rankDico):   # If you want to test the function: set_successors_order(n, getConsTable(n),
                                            # find_rank(add_column_number(del_omega(getAdjacencyMatrix(n))),rank=0,ranklist={})
    listSucc = []
    for cle in rankDico.keys():
        newline = []
        if int(cle) == -2:
            newline.append([])
            listSucc.append(newline)
        elif int(cle)== 0:
            listSucc.append(singleentrypoint(n))
        for i in range(len(matrix)):
            if int(cle) == matrix[i][0]:
                for l in range(len(matrix)):
                    for m in range(2, len(matrix[l])):
                        if matrix[l][m] == int(cle):
                            newline.append(matrix[l][0])
                listSucc.append(newline)
    return listSucc


def latestBySuccessors(n, listEarliest,
                       rankl):  # latestBySuccessors(n, earliestByPredecessors(n,rankDicoInlist(find_rank(add_column_number(del_omega(getAdjacencyMatrix(n))),rank=0,ranklist={}))),
                                # rankDicoInlist(find_rank(add_column_number(del_omega(getAdjacencyMatrix(n))),rank=0,ranklist={})))
    listTempo1 = []
    listTempo2 = {}
    listTempo3 = []
    listLateSuccFINAL = []
    departurePoint = listEarliest[len(listEarliest) - 1]
    for i in range(len(rankl) - 1, -1, -1):
        if rankl[i] == 0:
            listTempo2.update({rankl[i]:0})

        elif rankl[i] == -2:
            listTempo2.update({rankl[i]: departurePoint})

        elif hasSuccessorsVertex(getConsTable(n), rankl[i]) == 0:
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
        listTempo3.append(valeur)
    for i in range(len(listTempo3) - 1, -1, -1):
        listLateSuccFINAL.append(listTempo3[i])
    return listLateSuccFINAL


def display_latest(n, matrix):
    listRank = []
    listVertex = []
    for valeur in matrix.values():
        listRank.append(valeur)
    for cle in matrix.keys():
        listVertex.append(cle)

    listSucc = setSuccessorsOrder(n,getConsTable(n), find_rank(add_column_number(del_omega(getAdjacencyMatrix(n))),rank=0,ranklist={}))
    listLateSuccINIT = setDurationOrder(n, listSucc)
    listLateSuccFINAL = latestBySuccessors(n, earliestByPredecessors(n,rankDicoInlist(find_rank(add_column_number(del_omega(getAdjacencyMatrix(n))),rank=0,ranklist={}))),
                                           rankDicoInlist(find_rank(add_column_number(del_omega(getAdjacencyMatrix(n))),rank=0,ranklist={})))

    print("|", listRank, "|")
    print("|", listVertex, "|")
    print("|", listSucc, "|")
    print("|", listLateSuccINIT, "|")
    print("|", listLateSuccFINAL, "|")


#display_latest(2, find_rank(add_column_number(del_omega(getAdjacencyMatrix(2))),rank=0,ranklist={}))
