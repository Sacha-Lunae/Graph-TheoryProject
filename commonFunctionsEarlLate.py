from Rank import *


# This file contains small functions that we use in both Earliest_tables and Latest_tables

def hasSuccessorsVertex(n,vertex):
    table = getConsTable(n)
    count = 0
    for i in range(len(table)):
        for j in range(2, len(table[i])):  # for elements in the file txt after third column (predecessor columns)
            if table[i][j] == vertex:  # if the vertex is a predecessor for others vertexes
                count = count + 1  # thus, that means that he has successors and count increases
    return count


def rankDicoInlist(n):
    rankDico = find_rank(add_column_number(del_omega(getAdjacencyMatrix(n))),rank=0,ranklist={})  # dictionary containing vertex and their rank
    rankl = []
    for cle in rankDico.keys():
        rankl.append(int(cle))  # transformation of a dictionary containing vertexes and their ranks to a simple list containing vertexes
    return rankl


def getDurationByVertex(n, vertex):
    table = getConsTable(n)
    for i in range(len(table)):
        if table[i][0] == vertex:  # if the number in the column of vertexes of table is equal to vertex
            duration = table[i][1]  # thus, its duration is at position table[i][1]
            return duration



