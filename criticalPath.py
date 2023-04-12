from Latest_stables import *
from Earliest_stables import *
from Rank import *
from question3 import *


#This function computew and returns a dictionnary containing all the latest  - earliest dates which will be used to determine the critical path
def earliestMinusLatest(n, rankDico):
    #prepare the 2 lists that contains latest and earliest dates
    temp_earliest = earliestByPredecessors(n)

    temp_latest = latestBySuccessors(n)

    #computes the earliest minus latest list
    earliestMinusLatest = []
    for i in range(len(temp_earliest)):
        earliestMinusLatest.append(temp_earliest[i] - temp_latest[i])

    #transform the list previously obtained into a dictionnary to facilitate calculations
    earliestMinusLatest_Dico = rankDico.copy()

    counter = 0
    for i in earliestMinusLatest_Dico:
        earliestMinusLatest_Dico[i] = earliestMinusLatest[counter]
        counter += 1

    return earliestMinusLatest_Dico


#this function fills the Critical  path array with the next vertex in the critical path
def getNextVertex(n, vertex, rankDico, earliestMinusLatest, Critical_Path, Durations, index):
    if getSuccessors(n, int(vertex)) != []:

        Successors = getSuccessors(n, int(vertex))
        minRank = rankDico[str(Successors[0])]
        minRankVertex = 0
        ArrayVertex = [] # An array to store in case there are more than one critical path possible from a given vertex


        for i in Successors: #First loop to set the minimum rank among the successors and the associated vertex
            if rankDico[str(i)] <= minRank and earliestMinusLatest[str(i)] == 0:
                minRank = rankDico[str(i)]
                minRankVertex = i

        for i in Successors: #Second loop in case some vertex have the same rank as the minimum and part of a critical path therefore making another critical path, they are stored in ArrayVertex
            if rankDico[str(i)] == minRank and earliestMinusLatest[str(i)] == 0 and i != minRankVertex:
                ArrayVertex.append(i)


        # if ArrayVertex is not null it means there are several critical path diverging, they are added to the Critical_Path array and computed before  continuing the initial one
        if len(ArrayVertex) >= 1:
            for i in range(len(ArrayVertex)):
                Critical_Path.append(Critical_Path[index] + str(ArrayVertex[i]) + "->") #the new critical path is the same as the one we were working on until now therefore it is copied in the next
                Durations.append(Durations[index] + getDurationByVertex(n, int(ArrayVertex[i])))

                getNextVertex(n, ArrayVertex[i], rankDico, earliestMinusLatest, Critical_Path, Durations, len(Critical_Path) - 1)


        Critical_Path[index] += str(minRankVertex) + "->"
        Durations[index] += getDurationByVertex(n, int(minRankVertex))
        getNextVertex(n, minRankVertex, rankDico, earliestMinusLatest, Critical_Path, Durations, index)
    else:
        Critical_Path[index] += "Omega" # only triggers at the end of the path when there is no more successors


#this function will be the one called to find the final path(s) of a graphe, calling all the others
def criticalPath(n, temp_rankDico):

        if remove_zeros(getAdjacencyMatrix(n)) == False:

            Critical_Path = []  # Array to store if necessary the several critical paths
            Durations = []
            # creates a temporary dictionnary

            rankDico = {} #replaces the previous dictionnary with another one that does not take in account alpha and omega for simplicity reasons
            for i in temp_rankDico:
                if i != "alpha" and i != "omega":
                    rankDico[str(i)] = temp_rankDico[i] - 1

            earliestMinusLatest_Dico = earliestMinusLatest(n, rankDico)

            for i in earliestMinusLatest_Dico : #for loop in case there are several starting points

                if rankDico[str(i)] == 0 and earliestMinusLatest_Dico[str(i)] == 0: #initialises the algorithm only for starting points that belong to a critical path

                    Critical_Path.append("Alpha->" + str(i) + "->") #Critical path is filled one vertice by one  for easier copy when needed
                    Durations.append(getDurationByVertex(n, int(i)))
                    getNextVertex(n, i, rankDico, earliestMinusLatest_Dico, Critical_Path, Durations, len(Critical_Path) - 1) #call the function to keep going

            maxDuration = 0
            for i in Durations:
                if i > maxDuration:
                    maxDuration = i

            final_Critical_Path =  []
            for i in range(len(Critical_Path)): #displays all the critical path
                if Durations[i] == maxDuration:
                    final_Critical_Path.append(Critical_Path[i])

            for i in range(len(final_Critical_Path)):
                print("Critical path", i + 1, ": ", final_Critical_Path[i])
            print("Duration = ", maxDuration)
        else:
            print("Cycle detected, impossible to compute a critical path")


matrix = getAdjacencyMatrix(6)
temp_rankDico = find_rank(add_column_number(del_omega(matrix)), rank=0, ranklist={})
criticalPath(6, temp_rankDico)
