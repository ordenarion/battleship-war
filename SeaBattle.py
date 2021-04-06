import random
state0=0
state1=1
def optimal_position1(x):
    for i in range(4):
        x[i][0]=state1
    for i in range(2):
        x[i+5][0]=state1
    for i in range(2):
        x[i+8][0]=state1
    for i in range(3):
        x[i][2]=state1
    for i in range(3):
        x[i+4][2]=state1
    for i in range(2):
        x[i+8][2]=state1
    for i in range(4):
        x[2*i][random.randint(4,9)]=state1
    return x

def optimal_position2(x):
    for i in range(4):
        x[i][0]=state1
    for i in range(3):
        x[i+5][0]=state1
    for i in range(2):
        x[9][i]=state1
    for i in range(3):
        x[0][i+2]=state1
    for i in range(2):
        x[0][i+6]=state1
    for i in range(2):
        x[i][9]=state1
    for i in range(4):
        x[2*i+3][random.randint(3,9)]=state1
    return x

def optimal_position3(x):
    for i in range(4):
        x[i][0]=state1
    for i in range(2):
        x[i+5][0]=state1
    for i in range(2):
        x[i+8][0]=state1
    for i in range(3):
        x[i][9]=state1
    for i in range(2):
        x[i+4][9]=state1
    for i in range(3):
        x[i+7][9]=state1
    for i in range(4):
        x[2*i][random.randint(2,7)]=state1
    return x

def optimal_start_position():
    x=[[state0 for i in range(10)] for j in range(10)]
    num=random.randint(1,3)
    if num==1:
        return optimal_position1(x)
    elif num==2:
        return optimal_position2(x)
    else:
        return optimal_position3(x)
    
print(optimal_start_position())
