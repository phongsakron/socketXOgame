sampletable = [ ["null","null","null"],
                ["null","null","null"],
                ["null","null","null"]]

def chackWin(table):
    cnt = 0
    before = "a"
    for tables in table[0]:
        # print(tables)
        if before == tables:
            before = tables
            cnt+=1
        else:
            before = tables
        if cnt == 2 and before != "null":
            return (before)
    cnt = 0
    before = "a"
    for tables in table[1]:
        # print(tables)
        if before == tables:
            before = tables
            cnt+=1
        else:
            before = tables
        if cnt == 2 and before != "null":
            return (before)
    cnt = 0
    before = "a"
    for tables in table[2]:
        # print(tables)
        if before == tables:
            before = tables
            cnt+=1
        else:
            before = tables
        if cnt == 2 and before != "null":
            return (before)

    if table[0][0] == table[1][0] and table[1][0] == table[2][0] and table[0][0]  != "null":
        # print(table[0][0],table[1][0],table[2][0])
        return(table[0][0])
    if table[0][1] == table[1][1] and table[1][1] == table[2][1] and table[0][1] != "null":
        # print(table[0][1],table[1][1],table[2][1])
        return(table[0][1])
    if table[0][2] == table[1][2] and table[1][2] == table[2][2] and table[0][2] != "null":
        # print(table[0][2],table[1][2],table[2][2])
        return(table[0][2])
    if table[0][0] == table[1][1] and table[1][1] == table[2][2] and table[0][0]  != "null":
        # print(table[0][0],table[1][1],table[2][2])
        return(table[0][0])
    if table[0][2] == table[1][1] and table[1][1] == table[2][0] and table[0][2] != "null":
        # print(able[0][2],table[1][1],table[2][0])
        return(table[0][2])
    # print(table)
    return("no winner")


def editTable(x,y,player):
    global sampletable
    if sampletable[x][y] in "xo":
        return False
    msg = "editTable [{}][{}] from : {} to : {}"
    print(msg.format(x,y,sampletable[x][y],player))
    sampletable[x][y] = player


def showTable():
    for value in sampletable:
        print(value)


def reset():
    global sampletable
    sampletable.clear()
    sampletable = [ ["null","null","null"],
                    ["null","null","null"],
                    ["null","null","null"]]
