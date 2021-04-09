def right_coordinates(x,y):    
        return x>-1 and x<10 and y>-1 and y<10
    

def shot(list,x,y):
    if list[x][y]!=1:
        list[x][y]=-1
        return "miss"
    else:
        list[x][y]=-2
        if right_coordinates(x-1,y-1):
            list[x-1][y-1]=-1
        if right_coordinates(x-1,y+1):
            list[x-1][y+1]=-1
        if right_coordinates(x+1,y-1):
            list[x+1][y-1]=-1
        if right_coordinates(x+1,y+1):
            list[x+1][y+1]=-1
        positions=[]
        t1=False
        t2=False
        t3=False
        t4=False
        if right_coordinates(x,y-1) and list[x][y-1]>-1:            
            positions.append([x,y-1])
            t1=list[x][y-1]==1
        if right_coordinates(x,y+1) and list[x][y+1]>-1:            
            positions.append([x,y+1])
            t2=list[x][y+1]==1
        if right_coordinates(x-1,y) and list[x-1][y]>-1:
            positions.append([x-1,y])
            t3=list[x-1][y]==1                
        if right_coordinates(x+1,y) and list[x+1][y]>-1:
            positions.append([x+1,y])
            t4=list[x+1][y]==1              
        if len(positions)==0:
            return "destroyed"
        elif (t1 or t2 or t3 or t4)==False:
            if list[x][y-1]!=-2:
                list[x][y-1]=-1
            if list[x][y+1]!=-2:
                list[x][y+1]=-1
            if list[x-1][y]!=-2:
                list[x-1][y]=-1
            if list[x+1][y]!=-2:
                list[x+1][y]=-1
            
            return "destroyed"
        else:
            return positions
