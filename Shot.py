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
        
        if right_coordinates(x,y-1) and list[x][y-1]>-2:
            positions.append([x,y-1])
            
        if right_coordinates(x,y+1) and list[x][y+1]>-2:
            positions.append([x,y+1])
            
        if right_coordinates(x-1,y) and list[x-1][y]>-2:
            positions.append([x-1,y])
            
        if right_coordinates(x+1,y) and list[x+1][y]>-2:
            positions.append([x+1,y])
            
            
        sh=0
        while not [x,y,state1] in ships[sh]:
            sh+=1
        ships[sh][ships[sh].index([x,y,state1])][2]=-2
        sum=0
        for c in range(len(ships[sh])):
            sum+=ships[sh][c][2]
            
        destroyed=sum==-2*len(ships[sh])    
        
        if destroyed:
                for i in range(len(positions)):
                        list[positions[i][0]][positions[i][1]]=-3

                return "destroyed"     
        else:
            return positions
