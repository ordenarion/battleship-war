def right_coordinates(x,y):
        return x>-1 and x<10 and y>-1 and y<10


def shot(list,ships,x,y):
    if list[x][y]!=1:
        list[x][y]=-3
        return "miss"
    else:
        list[x][y]=-2
        if right_coordinates(x-1,y-1):
            list[x-1][y-1]=-3
        if right_coordinates(x-1,y+1):
            list[x-1][y+1]=-3
        if right_coordinates(x+1,y-1):
            list[x+1][y-1]=-3
        if right_coordinates(x+1,y+1):
            list[x+1][y+1]=-3
        positions=[]
        t1=False
        t2=False
        t3=False
        t4=False
        if right_coordinates(x,y-1) and list[x][y-1]>-2:
            positions.append([x,y-1])
            t1=list[x][y-1]==1
        if right_coordinates(x,y+1) and list[x][y+1]>-2:
            positions.append([x,y+1])
            t2=list[x][y+1]==1
        if right_coordinates(x-1,y) and list[x-1][y]>-2:
            positions.append([x-1,y])
            t3=list[x-1][y]==1
        if right_coordinates(x+1,y) and list[x+1][y]>-2:
            positions.append([x+1,y])
            t4=list[x+1][y]==1
            
        sh=0
        while not [x,y,state1] in ships[sh]:
            sh+=1
        ships[sh][ships[sh].index([x,y,state1])][2]=-2
        sum=0
        for c in range(len(ships[sh])):
            sum+=ships[sh][c][2]
            
        destroyed=sum==-2*len(ships[sh])    
        
        if len(positions)==0 and destroyed:
            return "destroyed"
        elif (t1 or t2 or t3 or t4)==False and destroyed:
            if list[x][y-1]!=-2:
                list[x][y-1]=-3
            if list[x][y+1]!=-2:
                list[x][y+1]=-3
            if list[x-1][y]!=-2:
                list[x-1][y]=-3
            if list[x+1][y]!=-2:
                list[x+1][y]=-3

            return "destroyed"
        elif len(positions)==0 or (t1 or t2 or t3 or t4)==False: 
            return "alive but no list"
            
        else:
            return positions
