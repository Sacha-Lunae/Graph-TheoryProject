from Latest_stables import *
from Earliest_stables import *
from Rank import *

rankDico = {"1": 0, "5": 1, "4": 2, "2": 3, "6": 3, "3": 4, "7": 5, "8": 6}

#getSuccessors
#hasSuccessorsState


def earliestMinusLatest(n, rankList):
    temp_earliest = displayEarliest(n, rankList)
    latest = display_latest(n, rankList)

    #temporary measure as one takes ina ccount alpha/omega and not the other therefore teh 2 arrays returned are of differetn dimensions
    earliest = []
    for i in range(len(temp_earliest)):
        if i != 0 and i != 8:
            earliest.append(temp_earliest[i])


    earliestMinusLatest = []
    for i in range(len(earliest)):
        earliestMinusLatest.append(earliest[i] - latest[i])

    earliestMinusLatest_Dico = rankDico.copy()

    counter = 0
    for i in earliestMinusLatest_Dico:
        earliestMinusLatest_Dico[i] = earliestMinusLatest[counter]
        counter += 1

    #   print("\n\n\n")
    #   print(earliest)
    # print(latest)
    #  print(earliestMinusLatest)
    # print(earliestMinusLatest_Dico)
    # print(rankDico)

    return earliestMinusLatest_Dico

def getNextVertex(n, vertex, rankDico, earliestMinusLatest):
    if getSuccessors(getConsTable(n), int(vertex)) != []:
        Succ = getSuccessors(getConsTable(n), int(vertex))
        minRank = rankDico[str(Succ[0])]
        minRankVertex = 0
        for i in Succ:
            if rankDico[str(i)] <= minRank and earliestMinusLatest[str(i)] == 0:
                minRank = rankDico[str(i)]
                minRankVertex = i

        return str(minRankVertex) + "->" + str(getNextVertex(n, minRankVertex, rankDico, earliestMinusLatest))
    else:
        return "omega"



def criticalPath(n, rankDico):
    earliestMinusLatest_Dico = earliestMinusLatest(11, rankDico)
    Critical_Path = []
    for i in earliestMinusLatest_Dico :
        if rankDico[i] == 0 and earliestMinusLatest_Dico[str(i)] == 0:
            Critical_Path.append(str(i) + "->" + str(getNextVertex(n, i, rankDico, earliestMinusLatest_Dico)))


    print("Critical path(s): ", Critical_Path)

#criticalPath(11, rankDico)
#print(rankDico)
#print("Successors of 2 : ", getSuccessors(getConsTable(11), 5))
#print( "MinRank = ",


criticalPath(11, rankDico)