'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

#Relationship Status.

def relationship_status(from_member, to_member, social_graph):
        if from_member in social_graph[to_member]["following"] and to_member in social_graph[from_member]["following"]:
            return("friends")

        elif from_member in social_graph[to_member]["following"]:
            return("followed by")

        elif to_member in social_graph[from_member]["following"]:
            return("follower")

        else:
            return("no relationship")


#Tic Tac Toe.

def tic_tac_toe(board):
    m=0
    o=[]
    x=[]
    while m < len(board):
        o+="O"
        x+="X"
        m+=1
    #HORIZONTALS
    for i in board:
        if i == x:
            return("X")
        elif i == o:
            return("O")
            

    #VERTICALS
    vertboard=[]
    for i in range(0, len(board)):
        vertline=[]
        for j in range(0, len(board)):
            vertline+=([board[j][i]])
            
        vertboard.append(vertline)
    if x in vertboard:
        return("X")
    elif o in vertboard:
        return("O")

    #DIAGONALS
    dialine=[]
    rdialine=[]
    line=[]
    rline=[]
    for i in range(0, len(board)):
        line+=board[i][i]
        dialine.append(line)
    for j in range(0, len(board)):
        rline+=board[j][len(board)-1-j]
        dialine.append(rline)
    diagonals=dialine+rdialine
    if x in diagonals:
        return("X")
    elif o in diagonals:
        return("O")
    else:
        return("NO WINNER")

#ETA.

def eta(first_stop, second_stop, route_map):
    klist=[]
    for key in route_map:
        klist+=(list(key))
    startlist=klist[0::2]
    startdex=startlist.index(first_stop)
    endlist=klist[1::2]
    enddex=endlist.index(second_stop)
    time=0
    if startdex<=enddex:
        for i in range(startdex,enddex+1):
            time+=route_map[startlist[i],endlist[i]]['travel_time_mins']
    elif startdex>enddex:
        for i in range(0,enddex+1):
            time+=route_map[startlist[i],endlist[i]]['travel_time_mins']
        for j in range(startdex,len(route_map)):
            time+=route_map[startlist[j],endlist[j]]['travel_time_mins']
            
    return(time)