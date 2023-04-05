from Earliest_stables import *
ranklist = {"1": 0, "5": 1, "4": 2, "2": 3, "6": 3, "3": 4, "7": 5, "8": 6}
listPred = [[],[1], [1, 5], [1, 4], [4, 5], [2], [3, 5], [2, 4, 6, 7]]


def set_successors_order(n):
    listPred = []
    x = getConsTable(n)
    for cle in ranklist.keys():
        newline=[]
        for i in range(nbrValues(x)):  # getAdjacencyMatrix(getConsTable(11))))
            if int(cle) == x[i][0]:
                for l in range(nbrValues(x)):
                    for m in range(2,nbrValues(x[l])):
                        if x[l][m] == int(cle):
                            newline.append(x[l][0])
                listPred.append(newline)
    return listPred


def display_latest(n, matrix):
    listRank = []
    listVertex = []  # Comment on appelle les états en anglais ?
    listEarlPredFINAL=[]
    for valeur in matrix.values():
        listRank.append(valeur)
    for cle in matrix.keys():
        listVertex.append(cle)

    listSucc = set_successors_order(n)
    listEarlSuccINIT = set_duration_order(n, listSucc)





    print("|", listRank, "|")
    print("|", listVertex, "|")
    print("|", listSucc, "|")
    print("|", listEarlSuccINIT, "|")

display_latest(11,ranklist)