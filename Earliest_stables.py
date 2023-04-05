from Rank import *

"""rank_dico=find_rank(
    add_column_number(
        getAdjacencyMatrix(
            getConsTable(11))),rank=0,ranklist={})"""

ranklist = {"1": 0, "5": 1, "4": 2, "2": 3, "6": 3, "3": 4, "7": 5, "8": 6}
listPred = [[],[1], [1, 5], [1, 4], [4, 5], [2], [3, 5], [2, 4, 6, 7]]

def nbrValues(matrix):
    counter = 0
    for valeur in matrix:
        counter = counter + 1

    return counter

def findLineState(n,state):
    x = getConsTable(n)
    line1 = -1
    for i in range(nbrValues(x)):
        line1=line1+1
        if x[i][0]==state:
            return line1

def get_duration_line(n, line):
    x = getConsTable(n)
    duration = x[line][1]  # WI index out of range
    return duration

def get_duration_state(n, state):
    x=getConsTable(n)
    for i in range(len(x)):
        if x[i][0]==state:
            duration=x[i][1]
            print(duration)
            return duration


def hasPredecessors(n, line):
    count = 0
    x = getConsTable(n)
    for i in range(2,nbrValues(x[line])):
        count = count + 1
        print(count)
    return count
#hasPredecessors(11,7)

#BELLMAN ALGORITHM

import math

def bellman_ford_max_weight(graph, source):
    n = len(graph)
    dist = [-math.inf] * n
    dist[source-1] = 0

    for i in range(n-1):
        for u in range(n):
            for v in range(2, len(graph[u])):
                A=graph[u]
                B=dist[u]
                C=graph[u][1]
                D=dist[graph[u][v]-1]
                if dist[u] > -math.inf and dist[graph[u][v]-1] < dist[u] + graph[u][1]:
                    dist[graph[u][v]-1] = dist[u] + graph[u][1]
    print("Dist", dist)
    return dist


def bellman_ford_min_weight(graph, source):
    n = len(graph)
    dist = [math.inf] * n
    dist[source-1] = 0

    for i in range(n-1):
        for u in range(n):
            for v in range(2, len(graph[u])):
                if dist[u] < math.inf and dist[graph[u][v]-1] > dist[u] + graph[u][1]:
                    dist[graph[u][v]-1] = dist[u] + graph[u][1]

    return dist

def get_index_of_state(n, valueState):
    x = getConsTable(n)
    counter = 0
    for i in range(nbrValues(x)):
        if x[i][0] == valueState:
            return counter
        counter = counter + 1


def set_predecessors_order(n, matrix):
    listPred = []
    x = getConsTable(n)
    for cle in ranklist.keys():
        for i in range(nbrValues(x)):  # getAdjacencyMatrix(getConsTable(11))))
            if int(cle) == x[i][0]:
                listPred.append(x[i][2:])
    return listPred




def set_duration_order(n, listPred):
    listEarlPred = []
    for i in range(nbrValues(listPred)):
        newline=[]
        if listPred[i] == 0:
            newline.append(0)
            listEarlPred.append(newline)
        for j in range(nbrValues(listPred[i])):
            dur = get_duration_line(n, get_index_of_state(n, listPred[i][j]))
            newline.append(dur)
        listEarlPred.append(newline)
    return listEarlPred
#set_duration_order(11,listPred)


def display_earliest(n, matrix):
    listRank = []
    listVertex = []  # Comment on appelle les états en anglais ?
    listEarlPredFINAL=[]
    for valeur in matrix.values():
        listRank.append(valeur)
    for cle in matrix.keys():
        listVertex.append(cle)

    listPred = set_predecessors_order(n, matrix)
    listEarlPredINIT = set_duration_order(n, listPred)

    print("|", listRank, "|")
    print("|", listVertex, "|")
    print("|", listPred, "|")
    print("|", listEarlPredINIT, "|")

    """
    for i in range(nbrValues(listPred)):
        if hasPredecessors(n, i) == None:
            listEarlPredFINAL.append(get_duration(n, i))
        for j in range(nbrValues(listPred[i])):
            for k in range(hasPredecessors(n, listPred[i][j])):
                durationPred = listEarlPredINIT[i][j] + get_duration(n, (get_predecessors(n, listPred[i][j])))
            listEarlPredFINAL.append(durationPred)
    """
"""
    for i in range(nbrValues(listPred)):
        if listPred[i]==[]:
            FirstState=listPred[i]
            listEarlPredFINAL.append(get_duration(n,i))
        if listPred[i]==FirstState:
            listEarlPredFINAL.append(get_duration(n,i))
        for j in range(nbrValues(listPred[i])):
            durationActualState=listEarlPredINIT[i][j]
            print("Duration Actual State",durationActualState)
            for k in range(nbrValues(x)):  # getAdjacencyMatrix(getConsTable(11))))
                if listPred[i][j] == x[k][0]:
                    predecessors=x[k][2:]
                    print(listPred[i][j],x[k][0])
                    print("pred",predecessors)

                for n in range(nbrValues(predecessors)):
                    for i in range(nbrValues(listPred)):
                        for j in range(nbrValues(listPred[i])):
                            if predecessors[n]==listPred[i][j]:
                                durationTotal=durationActualState+listEarlPredINIT[i][j]
                                print("durationTotal= ",durationActualState," + ",listEarlPredINIT[i][j],"=",durationTotal)
                                listEarlPredFINAL.append(durationTotal)
    print(listEarlPredFINAL)
"""





#display_earliest(11,ranklist)



"""
def earliestByPredecessors(n,matrix):
    for i in range(nbrValues(matrix)):
        print(get_predecessors(n,i,2))
        if 
            #return get_duration(n,i)
"""

"""
    for cle in ranklist.keys():

    dura=get_duration(n,2)+get_duration(n,4)
    duraTest=get_duration(n,2)+get_duration(n,4)

    print("duration",dura)
    print("duration",duraTest)
"""
# earliestByPredecessors(11,ranklist)

# set_predecessors_order(11, ranklist)

"""print(get_duration(1,9))
print(get_duration(11,5))
print(get_predecessors(11,5))"""

# display_earliest(11,ranklist)

# nbrValues(getAdjacencyMatrix(getConsTable(11)))
"""
AZERTY = getConsTable(11)
earliestByPredecessors(11,AZERTY)
"""

# if duration(1) = duration(2) ?

# disp maximum

listPred = set_predecessors_order(11, ranklist)
listEarlPredINIT = set_duration_order(11, listPred)
bellman_ford_max_weight(getConsTable(11),0)
