import random
def right_coordinates(x,y):
        return x>-1 and x<10 and y>-1 and y<10
def randomUserGrid():
    usergrid=[[0 for i in range(10)] for j in range(10)]
    squares=[(i,j) for i in range(10) for j in range(10)]
    shipnum=0
    ships=[[] for i in range(10)]
    
    notplaced=True
    wrongsquares=[]
    while notplaced:
        direction=[0,1,2,3]
        sh=random.randint(0,len(squares)-1)
        (x,y)=squares[sh]
        while notplaced and len(direction)>0:       
            index=random.randint(0,len(direction)-1)
            if direction[index]==0:
                if x-3>=0:               
                    for i in range(4):
                        ships[0].append([x-i,y,1])
                        usergrid[x-i][y]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x-i+j1,y+j2) and usergrid[x-i+j1][y+j2]!=1:
                                    usergrid[x-i+j1][y+j2]=-2
                                    if squares.count((x-i+j1,y+j2))>0:
                                         squares.remove((x-i+j1,y+j2))
                    notplaced=False
                else:
                    direction.remove(0)

            elif direction[index]==1:
                if x+3<=9:
                    
                    for i in range(4):
                        ships[0].append([x+i,y,1])
                        usergrid[x+i][y]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+i+j1,y+j2) and usergrid[x+i+j1][y+j2]!=1:
                                    usergrid[x+i+j1][y+j2]=-2
                                    if squares.count((x+i+j1,y+j2))>0:
                                         squares.remove((x+i+j1,y+j2))
                    notplaced=False
                else:
                    direction.remove(1)

            elif direction[index]==2:
                if y-3>=0:               
                    for i in range(4):
                        ships[0].append([x,y-i,1])
                        usergrid[x][y-i]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+j1,y-i+j2) and usergrid[x+j1][y-i+j2]!=1:
                                    usergrid[x+j1][y-i+j2]=-2
                                    if squares.count((x+j1,y-i+j2))>0:
                                         squares.remove((x+j1,y-i+j2))
                    notplaced=False
                else:
                    direction.remove(2)

            elif direction[index]==3:
                if y+3<=9:               
                    for i in range(4):
                        ships[0].append([x,y+i,1])
                        usergrid[x][y+i]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+j1,y+i+j2) and usergrid[x+j1][y+i+j2]!=1:
                                    usergrid[x+j1][y+i+j2]=-2
                                    if squares.count((x+j1,y+i+j2))>0:
                                         squares.remove((x+j1,y+i+j2))
                    notplaced=False
                else:
                    direction.remove(3)

        if notplaced:
            wrongsquares.append((x,y))
            if squares.count((x,y))>0:
                squares.remove((x,y))
    notplaced=True
    for i in range(len(wrongsquares)):
        if usergrid[wrongsquares[i][0]][wrongsquares[i][1]]==0:
            squares.append(wrongsquares[i])
    wrongsquares=[]


    while notplaced:
        direction=[0,1,2,3]
        sh=random.randint(0,len(squares)-1)
        (x,y)=squares[sh]
        while notplaced and len(direction)>0:       
            index=random.randint(0,len(direction)-1)
            if direction[index]==0:
                if x-2>=0 and usergrid[x-1][y]==0 and usergrid[x-2][y]==0:
                    for i in range(3):
                        ships[2].append([x-i,y,1])
                        usergrid[x-i][y]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x-i+j1,y+j2) and usergrid[x-i+j1][y+j2]!=1:
                                    usergrid[x-i+j1][y+j2]=-2
                                    if squares.count((x-i+j1,y+j2))>0:
                                         squares.remove((x-i+j1,y+j2))
                    notplaced=False
                else:
                    direction.remove(0)

            elif direction[index]==1:
                if x+2<=9 and usergrid[x+1][y]==0 and usergrid[x+2][y]==0:               
                    for i in range(3):
                        ships[2].append([x+i,y,1])
                        usergrid[x+i][y]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+i+j1,y+j2) and usergrid[x+i+j1][y+j2]!=1:
                                    usergrid[x+i+j1][y+j2]=-2
                                    if squares.count((x+i+j1,y+j2))>0:
                                         squares.remove((x+i+j1,y+j2))
                    notplaced=False
                else:
                    direction.remove(1)

            elif direction[index]==2:
                if y-2>=0 and usergrid[x][y-1]==0 and usergrid[x][y-2]==0:               
                    for i in range(3):
                        ships[2].append([x,y-i,1])
                        usergrid[x][y-i]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+j1,y-i+j2) and usergrid[x+j1][y-i+j2]!=1:
                                    usergrid[x+j1][y-i+j2]=-2
                                    if squares.count((x+j1,y-i+j2))>0:
                                         squares.remove((x+j1,y-i+j2))
                    notplaced=False
                else:
                    direction.remove(2)

            elif direction[index]==3:
                if y+2<=9 and usergrid[x][y+1]==0 and usergrid[x][y+2]==0:               
                    for i in range(3):
                        ships[2].append([x,y+i,1])
                        usergrid[x][y+i]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+j1,y+i+j2) and usergrid[x+j1][y+i+j2]!=1:
                                    usergrid[x+j1][y+i+j2]=-2
                                    if squares.count((x+j1,y+i+j2))>0:
                                         squares.remove((x+j1,y+i+j2))
                    notplaced=False
                else:
                    direction.remove(3)

        if notplaced:
            wrongsquares.append((x,y))
            if squares.count((x,y))>0:
                squares.remove((x,y))
                
    notplaced=True
    for i in range(len(wrongsquares)):
        if usergrid[wrongsquares[i][0]][wrongsquares[i][1]]==0:
            squares.append(wrongsquares[i])
    wrongsquares=[]

    while notplaced:
        direction=[0,1,2,3]
        sh=random.randint(0,len(squares)-1)
        (x,y)=squares[sh]
        while notplaced and len(direction)>0:       
            index=random.randint(0,len(direction)-1)
            if direction[index]==0:
                if x-2>=0 and usergrid[x-1][y]==0 and usergrid[x-2][y]==0:
                    for i in range(3):
                        ships[1].append([x-i,y,1])
                        usergrid[x-i][y]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x-i+j1,y+j2) and usergrid[x-i+j1][y+j2]!=1:
                                    usergrid[x-i+j1][y+j2]=-2
                                    if squares.count((x-i+j1,y+j2))>0:
                                         squares.remove((x-i+j1,y+j2))
                    notplaced=False
                else:
                    direction.remove(0)

            elif direction[index]==1:
                if x+2<=9 and usergrid[x+1][y]==0 and usergrid[x+2][y]==0:               
                    for i in range(3):
                        ships[1].append([x+i,y,1])
                        usergrid[x+i][y]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+i+j1,y+j2) and usergrid[x+i+j1][y+j2]!=1:
                                    usergrid[x+i+j1][y+j2]=-2
                                    if squares.count((x+i+j1,y+j2))>0:
                                         squares.remove((x+i+j1,y+j2))
                    notplaced=False
                else:
                    direction.remove(1)

            elif direction[index]==2:
                if y-2>=0 and usergrid[x][y-1]==0 and usergrid[x][y-2]==0:               
                    for i in range(3):
                        ships[1].append([x,y-i,1])
                        usergrid[x][y-i]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+j1,y-i+j2) and usergrid[x+j1][y-i+j2]!=1:
                                    usergrid[x+j1][y-i+j2]=-2
                                    if squares.count((x+j1,y-i+j2))>0:
                                         squares.remove((x+j1,y-i+j2))
                    notplaced=False
                else:
                    direction.remove(2)

            elif direction[index]==3:
                if y+2<=9 and usergrid[x][y+1]==0 and usergrid[x][y+2]==0:               
                    for i in range(3):
                        ships[1].append([x,y+i,1])
                        usergrid[x][y+i]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+j1,y+i+j2) and usergrid[x+j1][y+i+j2]!=1:
                                    usergrid[x+j1][y+i+j2]=-2
                                    if squares.count((x+j1,y+i+j2))>0:
                                         squares.remove((x+j1,y+i+j2))
                    notplaced=False
                else:
                    direction.remove(3)

        if notplaced:
            wrongsquares.append((x,y))
            if squares.count((x,y))>0:
                squares.remove((x,y))
                
    notplaced=True
    for i in range(len(wrongsquares)):
        if usergrid[wrongsquares[i][0]][wrongsquares[i][1]]==0:
            squares.append(wrongsquares[i])
    wrongsquares=[]

    while notplaced:
        direction=[0,1,2,3]
        sh=random.randint(0,len(squares)-1)
        (x,y)=squares[sh]
        while notplaced and len(direction)>0:       
            index=random.randint(0,len(direction)-1)
            if direction[index]==0:
                if x-1>=0 and usergrid[x-1][y]==0:
                    for i in range(2):
                        ships[3].append([x-i,y,1])
                        usergrid[x-i][y]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x-i+j1,y+j2) and usergrid[x-i+j1][y+j2]!=1:
                                    usergrid[x-i+j1][y+j2]=-2
                                    if squares.count((x-i+j1,y+j2))>0:
                                         squares.remove((x-i+j1,y+j2))
                    notplaced=False
                else:
                    direction.remove(0)

            elif direction[index]==1:
                if x+1<=9 and usergrid[x+1][y]==0:               
                    for i in range(2):
                        ships[3].append([x+i,y,1])
                        usergrid[x+i][y]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+i+j1,y+j2) and usergrid[x+i+j1][y+j2]!=1:
                                    usergrid[x+i+j1][y+j2]=-2
                                    if squares.count((x+i+j1,y+j2))>0:
                                         squares.remove((x+i+j1,y+j2))
                    notplaced=False
                else:
                    direction.remove(1)

            elif direction[index]==2:
                if y-1>=0 and usergrid[x][y-1]==0==0:               
                    for i in range(2):
                        ships[3].append([x,y-i,1])
                        usergrid[x][y-i]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+j1,y-i+j2) and usergrid[x+j1][y-i+j2]!=1:
                                    usergrid[x+j1][y-i+j2]=-2
                                    if squares.count((x+j1,y-i+j2))>0:
                                         squares.remove((x+j1,y-i+j2))
                    notplaced=False
                else:
                    direction.remove(2)

            elif direction[index]==3:
                if y+1<=9 and usergrid[x][y+1]==0:               
                    for i in range(2):
                        ships[3].append([x,y+i,1])
                        usergrid[x][y+i]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+j1,y+i+j2) and usergrid[x+j1][y+i+j2]!=1:
                                    usergrid[x+j1][y+i+j2]=-2
                                    if squares.count((x+j1,y+i+j2))>0:
                                         squares.remove((x+j1,y+i+j2))
                    notplaced=False
                else:
                    direction.remove(3)

        if notplaced:
            wrongsquares.append((x,y))
            if squares.count((x,y))>0:
                squares.remove((x,y))
                
    notplaced=True
    for i in range(len(wrongsquares)):
        if usergrid[wrongsquares[i][0]][wrongsquares[i][1]]==0:
            squares.append(wrongsquares[i])
    wrongsquares=[]


    while notplaced:
        direction=[0,1,2,3]
        sh=random.randint(0,len(squares)-1)
        (x,y)=squares[sh]
        while notplaced and len(direction)>0:       
            index=random.randint(0,len(direction)-1)
            if direction[index]==0:
                if x-1>=0 and usergrid[x-1][y]==0:
                    for i in range(2):
                        ships[4].append([x-i,y,1])
                        usergrid[x-i][y]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x-i+j1,y+j2) and usergrid[x-i+j1][y+j2]!=1:
                                    usergrid[x-i+j1][y+j2]=-2
                                    if squares.count((x-i+j1,y+j2))>0:
                                         squares.remove((x-i+j1,y+j2))
                    notplaced=False
                else:
                    direction.remove(0)

            elif direction[index]==1:
                if x+1<=9 and usergrid[x+1][y]==0:               
                    for i in range(2):
                        ships[4].append([x+i,y,1])
                        usergrid[x+i][y]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+i+j1,y+j2) and usergrid[x+i+j1][y+j2]!=1:
                                    usergrid[x+i+j1][y+j2]=-2
                                    if squares.count((x+i+j1,y+j2))>0:
                                         squares.remove((x+i+j1,y+j2))
                    notplaced=False
                else:
                    direction.remove(1)

            elif direction[index]==2:
                if y-1>=0 and usergrid[x][y-1]==0==0:               
                    for i in range(2):
                        ships[4].append([x,y-i,1])
                        usergrid[x][y-i]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+j1,y-i+j2) and usergrid[x+j1][y-i+j2]!=1:
                                    usergrid[x+j1][y-i+j2]=-2
                                    if squares.count((x+j1,y-i+j2))>0:
                                         squares.remove((x+j1,y-i+j2))
                    notplaced=False
                else:
                    direction.remove(2)

            elif direction[index]==3:
                if y+1<=9 and usergrid[x][y+1]==0:               
                    for i in range(2):
                        ships[4].append([x,y+i,1])
                        usergrid[x][y+i]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+j1,y+i+j2) and usergrid[x+j1][y+i+j2]!=1:
                                    usergrid[x+j1][y+i+j2]=-2
                                    if squares.count((x+j1,y+i+j2))>0:
                                         squares.remove((x+j1,y+i+j2))
                    notplaced=False
                else:
                    direction.remove(3)

        if notplaced:
            wrongsquares.append((x,y))
            if squares.count((x,y))>0:
                squares.remove((x,y))
                
    notplaced=True
    for i in range(len(wrongsquares)):
        if usergrid[wrongsquares[i][0]][wrongsquares[i][1]]==0:
            squares.append(wrongsquares[i])
    wrongsquares=[]

    while notplaced:
        direction=[0,1,2,3]
        sh=random.randint(0,len(squares)-1)
        (x,y)=squares[sh]
        while notplaced and len(direction)>0:       
            index=random.randint(0,len(direction)-1)
            if direction[index]==0:
                if x-1>=0 and usergrid[x-1][y]==0:
                    for i in range(2):
                        ships[5].append([x-i,y,1])
                        usergrid[x-i][y]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x-i+j1,y+j2) and usergrid[x-i+j1][y+j2]!=1:
                                    usergrid[x-i+j1][y+j2]=-2
                                    if squares.count((x-i+j1,y+j2))>0:
                                         squares.remove((x-i+j1,y+j2))
                    notplaced=False
                else:
                    direction.remove(0)

            elif direction[index]==1:
                if x+1<=9 and usergrid[x+1][y]==0:               
                    for i in range(2):
                        ships[5].append([x+i,y,1])
                        usergrid[x+i][y]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+i+j1,y+j2) and usergrid[x+i+j1][y+j2]!=1:
                                    usergrid[x+i+j1][y+j2]=-2
                                    if squares.count((x+i+j1,y+j2))>0:
                                         squares.remove((x+i+j1,y+j2))
                    notplaced=False
                else:
                    direction.remove(1)

            elif direction[index]==2:
                if y-1>=0 and usergrid[x][y-1]==0==0:               
                    for i in range(2):
                        ships[5].append([x,y-i,1])
                        usergrid[x][y-i]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+j1,y-i+j2) and usergrid[x+j1][y-i+j2]!=1:
                                    usergrid[x+j1][y-i+j2]=-2
                                    if squares.count((x+j1,y-i+j2))>0:
                                         squares.remove((x+j1,y-i+j2))
                    notplaced=False
                else:
                    direction.remove(2)

            elif direction[index]==3:
                if y+1<=9 and usergrid[x][y+1]==0:               
                    for i in range(2):
                        ships[5].append([x,y+i,1])
                        usergrid[x][y+i]=1
                        for j1 in range(-1,2):
                            for j2 in range(-1,2):
                                if right_coordinates(x+j1,y+i+j2) and usergrid[x+j1][y+i+j2]!=1:
                                    usergrid[x+j1][y+i+j2]=-2
                                    if squares.count((x+j1,y+i+j2))>0:
                                         squares.remove((x+j1,y+i+j2))
                    notplaced=False
                else:
                    direction.remove(3)

        if notplaced:
            wrongsquares.append((x,y))
            if squares.count((x,y))>0:
                squares.remove((x,y))
                
    notplaced=True
    for i in range(len(wrongsquares)):
        if usergrid[wrongsquares[i][0]][wrongsquares[i][1]]==0:
            squares.append(wrongsquares[i])
    wrongsquares=[]

    for i in range(4):
        sh=random.randint(0,len(squares)-1)
        (x,y)=squares[sh]
        usergrid[x][y]=1
        ships[6+i].append([x,y,1])
        squares.remove((x,y))

    for i in range(10):
        for j in range(10):
            if usergrid[i][j]==-2:
                usergrid[i][j]=0
    
    return [usergrid,ships]

pole=randomUserGrid()[0]
korabl=randomUserGrid()[1]
for k in range(10):
        print(pole[k])

for k in range(10):
        print(korabl[k])
