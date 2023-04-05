def getFile(n) : 
    fileName = "tables/" + str(n) + ".txt" 
    with open(fileName) as file : 
        return file.readlines()

def getConsTable(n) : 
    consTable = []
    for array in getFile(n):
        #The current array from getFile returns an array of strings, which is unuseable. Let's fix this.
        rightArray = []
        for element in array.split():
            #I only append the integers, which allows me to skip the \n
            rightArray.append(int(element))
        consTable.append(rightArray)
    return consTable

def printConsTable(n) :
    print(getConsTable(n))



def bellman_ford_max(graph, source):
    dist = [float('-inf')] * len(graph)
    dist[source - 1] = graph[source - 1][1]
    for i in range(len(graph) - 1):
        for u in range(len(graph)):
            for v in graph[u][2:]:
                if dist[v - 1] < dist[u] + graph[v - 1][1]:
                    dist[v - 1] = dist[u] + graph[v - 1][1]
    return dist

print(bellman_ford_max(getConsTable(11), 0))
