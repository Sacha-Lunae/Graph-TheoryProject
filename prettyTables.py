from prettytable import PrettyTable

def prettyAdjacency(adjTable) : 
    table = PrettyTable()
    fieldNames = []
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