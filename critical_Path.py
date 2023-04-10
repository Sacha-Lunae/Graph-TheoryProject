from Latest_stables import *
from Earliest_stables import *
from Rank import *
from question3 import *


#temporary measure since i need a dictionnary of ranks
rankDico = {"1": 0, "5": 1, "4": 2, "2": 3, "6": 3, "3": 4, "7": 5, "8": 6}

#This function computew and returns a dictionnary containing all the latest  - earliest dates which will be used to determine the critical path
def earliestMinusLatest(n, rankDico):
    #prepare the 2 lists that contains latest and earliest dates
    matrix = getAdjacencyMatrix(n)
    rankList = rankDicoInlist(find_rank(add_column_number(del_omega(matrix)), rank=0, ranklist={}))

    temp_earliest = earliestByPredecessors(n, rankList)

    temp_latest = latestBySuccessors(n, temp_earliest,rankList)

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
def getNextVertex(n, vertex, rankDico, earliestMinusLatest, Critical_Path, index):
    if getSuccessors(getConsTable(n), int(vertex)) != []:

        Successors = getSuccessors(getConsTable(n), int(vertex))
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

                getNextVertex(n, ArrayVertex[i], rankDico, earliestMinusLatest, Critical_Path, len(Critical_Path) - 1)

        Critical_Path[index] += str(minRankVertex) + "->"
        getNextVertex(n, minRankVertex, rankDico, earliestMinusLatest, Critical_Path, index)
    else:
        Critical_Path[index] += "Omega" # only triggers at the end of the path when there is no more successors


#this function will be the one called to find the final path(s) of a graphe, calling all the others
def criticalPath(n):
    try:
        if remove_zeros(getAdjacencyMatrix(n)) == False:

            matrix = getAdjacencyMatrix(n)
            Critical_Path = [] # Array to store if necessary the several critical paths
            temp_rankDico = find_rank(add_column_number(del_omega(matrix)), rank=0, ranklist={})
            # creates a temporary dictionnary

            rankDico = {} #replaces the previous dictionnary with another one that does not take in account alpha and omega for simplicity reasons
            for i in temp_rankDico:
                if i != "alpha" and i != "omega":
                    rankDico[str(i)] = temp_rankDico[i] - 1

            earliestMinusLatest_Dico = earliestMinusLatest(n, rankDico)

            for i in earliestMinusLatest_Dico : #for loop in case there are several starting points

                if rankDico[str(i)] == 0 and earliestMinusLatest_Dico[str(i)] == 0: #initialises the algorithm only for starting points that belong to a critical path

                    Critical_Path.append("Alpha->" + str(i) + "->") #Critical path is filled one vertice by one  for easier copy when needed
                    getNextVertex(n, i, rankDico, earliestMinusLatest_Dico, Critical_Path, len(Critical_Path) - 1) #call the function to keep going

            for i in range(len(Critical_Path)): #displays all the critical path

                print("Critical path", i + 1, ": ", Critical_Path[i])

        else:
            print("Cycle detected, impossible to compute a critical path")
    except FileNotFoundError:
        print("File not found")
    except NameError:
        print("Invalid Name")

criticalPath(12)
