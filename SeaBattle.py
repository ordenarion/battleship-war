import random
state0=0
state1=1
def optimal_position1(x,ships):
    for i in range(4):
        x[i][0]=state1
        ships[0].append([i,0,state1])
    for i in range(2):
        x[i+5][0]=state1
        ships[1].append([i+5,0,state1])
    for i in range(2):
        x[i+8][0]=state1
        ships[2].append([i+8,0,state1])
    for i in range(3):
        x[i][2]=state1
        ships[3].append([i, 2, state1])
    for i in range(3):
        x[i+4][2]=state1
        ships[4].append([i + 4, 2, state1])
    for i in range(2):
        x[i+8][2]=state1
        ships[5].append([i + 8, 2, state1])
    for i in range(4):
        j=random.randint(4,9)
        x[2*i][j]=state1
        ships[6+i].append([2*i,j,state1])
    return [x,ships]

def optimal_position2(x,ships):
    for i in range(4):
        x[i][0]=state1
        ships[0].append( [i, 0, state1])
    for i in range(3):
        x[i+5][0]=state1
        ships[1].append([i+5,0,state1])
    for i in range(2):
        x[9][i]=state1
        ships[2].append([9,i,state1])
    for i in range(3):
        x[0][i+2]=state1
        ships[3].append([0,i+2,state1])
    for i in range(2):
        x[0][i+6]=state1
        ships[4].append([0,i+6,state1])
    for i in range(2):
        x[i][9]=state1
        ships[5].append([i,9,state1])
    for i in range(4):
        j=random.randint(3,9)
        x[2*i+3][j]=state1
        ships[6+i].append([2*i+3,j,state1])
    return [x,ships]

def optimal_position3(x,ships):
    for i in range(4):
        x[i][0]=state1
        ships[0].append([i,0,state1])
    for i in range(2):
        x[i+5][0]=state1
        ships[1].append([i+5,0,state1])
    for i in range(2):
        x[i+8][0]=state1
        ships[2].append([i+8,0,state1])
    for i in range(3):
        x[i][9]=state1
        ships[3].append([i,9,state1])
    for i in range(2):
        x[i+4][9]=state1
        ships[4].append([i+4,9,state1])
    for i in range(3):
        x[i+7][9]=state1
        ships[5].append([i+7,9,state1])
    for i in range(4):
        j=random.randint(2,7)
        x[2*i][j]=state1
        ships[6+i].append([2*i,j,state1])
    return [x,ships]

def optimal_start_position():
    x=[[state0 for i in range(10)] for j in range(10)]
    ships=[[] for i in range(10)]
    num=random.randint(1,3)
    if num==1:
        return optimal_position1(x,ships)
    elif num==2:
        return optimal_position2(x,ships)
    else:
        return optimal_position3(x,ships)

