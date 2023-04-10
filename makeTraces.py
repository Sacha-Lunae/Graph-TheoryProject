from adjacency import *
from criticalPath import *
from earliestTables import *
from latestTables import *
from rank import *
from prettyTables import *



#CE QU'IL FAUT ÉCRIRE DANS CHAQUE TRUC
#ADJACENCY
#RANKS
#EARLIEST, LATEST, FLOATS ?
#CRITICAL PATHS

for n in range(1,13) :
    with open("executionTraces/trace"+str(n)+".txt", "w") as file:
        # call your function, convert the output to a string, and write it to the file

        file.write("ADJACENCY MATRIX : \n\n")
        file.write(str(prettyAdjacency(getAdjacencyMatrix(n))) + "\n\n")
        if remove_zeros(getAdjacencyMatrix(n)) == False:
            file.write("EARLIEST TABLES : \n\n" + returnEarliest(n) + "\n\n")
            file.write("LATEST TABLES : \n\n" + returnLatest(n) + "\n\n")
        else : 
            file.write("The graph contains a cycle. We can't compute the ranks, the earliest/latest tables and the critical paths.")

    #IMPORTANT : the functions for the ranks/critical paths were complicated to put in a "return" form instead of a "print"
    #form, therefore I've added them by hand to each trace file.