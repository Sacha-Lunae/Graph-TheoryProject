from prettytable import PrettyTable

def prettyAdjacency(adjTable) : 

    for i in range (len(adjTable)) : 
        if i == 0 :
            adjTable[i].insert(0,"Alpha")
        else :
            if i == (len(adjTable)-1) :
                adjTable[i].insert(0,"Omega")
            else: 
                adjTable[i].insert(0,i)
    table = PrettyTable()
    fieldNames = []
    fieldNames.append("Vertice")
    fieldNames.append("Alpha")
    for i in range(1,(len(adjTable)-1)) : 
        fieldNames.append(str(i))

    fieldNames.append("Omega")

    table.field_names = fieldNames

    for row in adjTable : 
        table.add_row(row)

    print(table)

def prettyBellman(bellmanArr) :
    table = PrettyTable()
    fieldNames = []
    fieldNames.append("Alpha")
    for i in range(1,(len(bellmanArr)-1)) : 
        fieldNames.append(str(i))

    fieldNames.append("Omega")

    table.field_names = fieldNames

    table.add_row(bellmanArr)

    print(table)