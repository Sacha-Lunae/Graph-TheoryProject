

def hasSuccessorsVertex(matrix,
                        vertex):  # If you want to test the function: hasSuccessorsState(getConsTable(n), vertex)
    count = 0
    for i in range(len(matrix)):
        for j in range(2, len(matrix[i])):
            if matrix[i][j] == vertex:
                count = count + 1
    return count


def rankDicoInlist(
        rankDico):  # To test the function: rankDicoInlist(find_rank(add_column_number(del_omega(getAdjacencyMatrix(n))),rank=0,ranklist={}))
    rankl = []
    for cle in rankDico.keys():
        rankl.append(int(cle))
    return rankl


def getDurationByVertex(table, vertex):  # If you want to test the function: getDurationByVertex(getConsTable(n),vertex)
    for i in range(len(table)):
        if not vertex:
            duration = table[i][1]
            return duration
        if table[i][0] == vertex:
            duration = table[i][1]
            return duration