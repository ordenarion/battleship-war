import pygame
from tkinter import *
from tkinter import messagebox, font
import random
import time

def right_coordinates(x, y):
    return x > -1 and x < 10 and y > -1 and y < 10

state1 = 1
def shot(list, ships, x, y):
    if list[x][y] != 1:
        list[x][y] = -3
        return "miss"
    else:
        list[x][y] = -2
        if right_coordinates(x - 1, y - 1):
            list[x - 1][y - 1] = -3
        if right_coordinates(x - 1, y + 1):
            list[x - 1][y + 1] = -3
        if right_coordinates(x + 1, y - 1):
            list[x + 1][y - 1] = -3
        if right_coordinates(x + 1, y + 1):
            list[x + 1][y + 1] = -3
        positions = []
        if right_coordinates(x, y - 1) and list[x][y - 1] > -2:
            positions.append([x, y - 1])

        if right_coordinates(x, y + 1) and list[x][y + 1] > -2:
            positions.append([x, y + 1])

        if right_coordinates(x - 1, y) and list[x - 1][y] > -2:
            positions.append([x - 1, y])

        if right_coordinates(x + 1, y) and list[x + 1][y] > -2:
            positions.append([x + 1, y])


        sh = 0
        while not [x, y, state1] in ships[sh]:
            sh += 1
        ships[sh][ships[sh].index([x, y, state1])][2] = -2
        sum = 0
        for c in range(len(ships[sh])):
            sum += ships[sh][c][2]

        destroyed = sum == -2 * len(ships[sh])

        if destroyed:
            for i in range(len(positions)):
                list[positions[i][0]][positions[i][1]]=-3
            return "destroyed"

        else:
            return positions

def sea_battle():
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (120, 171, 235)
    BG = (110, 131, 156)
    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH =40
    HEIGHT =40

    # This sets the margin between each cell
    MARGIN = 5




    # Create a 2 dimensional array. A two dimensional
    # array is simply a list of lists.
    grid = []
    for row in range(10):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(10):
            grid[row].append(0)  # Append a cell
    # grid = [[1, 0, 1, 1, 1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 1]]
    sample = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    grid_cpu = []
    for row in range(10):
        # Add an empty array that will hold each cell
        # in this row
        grid_cpu.append([])
        for column in range(10):
            grid_cpu[row].append(0)  # Append a cell
    # Initialize pygame
    f = [[[1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]],
         [[[0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1]],
          [[5, 0, 1], [6, 0, 1]],
          [[8, 0, 1], [9, 0, 1]],
          [[0, 9, 1], [1, 9, 1], [2, 9, 1]],
          [[4, 9, 1], [5, 9, 1]],
          [[7, 9, 1], [8, 9, 1], [9, 9, 1]],
          [[0, 5, 1]],
          [[2, 5, 1]],
          [[4, 4, 1]],
          [[6, 3, 1]]]]
    grid_cpu_to_attack =f[0] #[[1, 0, 1, 1, 1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 1]]

    curr = []
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [1500, 800]
    screen_person = pygame.display.set_mode(WINDOW_SIZE)
    screen_cpu = pygame.display.set_mode(WINDOW_SIZE)
    # Set title of screen
    pygame.display.set_caption("Основной этап: В левом поле стреляет игрок, В правом поле стреляет компьютер. По центру отображается выбранная пользователем расстановка кораблей")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()



    screen_person.fill(BLACK)
    pygame.draw.rect(screen_person, WHITE,
                     pygame.Rect(100, 100, (MARGIN + WIDTH) * 10 + MARGIN, (MARGIN + HEIGHT) * 10 + MARGIN), 2)
    pygame.draw.rect(screen_person, WHITE,
                     pygame.Rect(900, 100, (MARGIN + WIDTH) * 10 + MARGIN, (MARGIN + HEIGHT) * 10 + MARGIN), 2)

    i = 2
    user_miss = False
    user_hit = False

    cpu_miss = False
    cpu_hit = False
    # USER
    for row in range(10):
        for column in range(10):
            color = WHITE
            pygame.draw.rect(screen_person,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN + 100,
                              (MARGIN + HEIGHT) * row + MARGIN + 100,
                              WIDTH,
                              HEIGHT])

    # CPU
    for row in range(10):
        for column in range(10):
            color = WHITE
            pygame.draw.rect(screen_person,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN + 900,
                              (MARGIN + HEIGHT) * row + MARGIN + 100,
                              WIDTH,
                              HEIGHT])

    hp_cpu = 10
    hp_user = 100
    score = 100
    # -------- Main Program Loop -----------
    cpu_pos = [[x, y] for x in range(10) for y in range(10)]
    cpu_start=[[0,3],[1,2],[2,1],[3,0],[0,7],[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[7,0],[3,9],[4,8],[5,7],[6,6],[7,5],[8,4],[9,3],[6,9],[7,8],[8,7],[9,6]]
    cpu_add=[[0,1],[1,0],[0,5],[1,4],[2,3],[3,2],[4,1],[5,0],[0,9],[1,8],[2,7],[3,6],[4,5],[5,4],[6,3],[7,2],[8,1],[9,0],[4,9],[5,8],[6,7],[7,6],[8,5],[9,4],[8,9],[9,8]]
    shipdamaged=[]
    t1=True
    t2=True
    while not done:



        label.configure(text=None)




        if i % 2 == 0:

            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)-2
                    row = pos[1] //(HEIGHT + MARGIN)-2
                    print(pos)
                    if column >9 or row >9:
                        pass
                    else:
                        grid[row][column] = -1

                        if sample[row][column] == 1:
                            i += 2
                        else:
                            i += 1

                        print(i)

                        # Set that location to one
                       # grid[row][column] = -1

                    print("Click ", pos, "Grid coordinates: ", row, column)

                # Set the screen background

                # Draw the grid
            for row in range(10):
                for column in range(10):
                    color = WHITE
                    if grid[row][column] == -1 and sample[row][column] != 1:
                        color = BLUE
                        score -= 1
                    elif grid[row][column] == -1 and sample[row][column] == 1:
                        color = RED
                        score += 5
                        hp_cpu -= 1



                    pygame.draw.rect(screen_person,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN+100,
                                          (MARGIN + HEIGHT) * row + MARGIN+100,
                                          WIDTH,
                                          HEIGHT])
            # if user_hit:
            #     i += 2
            #     user_hit = False
            # elif user_miss:
            #     i += 1
            #     user_miss = False
            #


        # pygame.time.wait(10)
        # i = random.randint(0,9)
        # j = random.randint(0,9)
        # print(i,j)
        # grid_cpu[i][j]=-1

        if i % 2 == 1:
            if curr != []:
                coord = random.choice(curr)

                next_curr = shot(grid_cpu_to_attack,f[1],coord[0],coord[1])
                if next_curr == "miss":
                    curr.remove(coord)
                    if t2 and cpu_start.count(coord)>0:
                        cpu_start.remove(coord)
                    cpu_pos.remove(coord)
                    cpu_miss = True
                elif next_curr == "destroyed":
                    curr.remove(coord)
                    if t2 and cpu_start.count(coord)>0:
                        cpu_start.remove(coord)
                    cpu_pos.remove(coord)
                    for i in range(len(curr)):
                        grid_cpu_to_attack[curr[i][0]][curr[i][1]]=-3
                    curr = []
                    shipdamaged=[]
                    cpu_hit = True
                    if t1:
                        notfound=True
                        k=-1
                        while notfound:
                            k+=1
                            if len(f[1][k])==4:
                                notfound=False
                        if f[1][k][0][2]+f[1][k][1][2]+f[1][k][2][2]+f[1][k][3][2]==-8:
                            cpu_start=cpu_start+cpu_add
                            t1=False

                else:
                    shipdamaged.append(coord)
                    if shipdamaged[0][0]==shipdamaged[1][0]:
                        t=True
                        x=shipdamaged[0][0]
                    else:
                        t=False
                        x=shipdamaged[0][1]
                    curr.remove(coord)
                    curr=curr+next_curr
                    if t:
                        for i in range(len(curr)):
                            if curr[i][0]!=x:
                                grid_cpu_to_attack[curr[i][0]][curr[i][1]]=-3
                                curr[i]=0
                    else:
                        for i in range(len(curr)):
                            if curr[i][1]!=x:
                                grid_cpu_to_attack[curr[i][0]][curr[i][1]]=-3
                                curr[i]=0

                    while curr.count(0)>0:
                        curr.remove(0)
                    if t2 and cpu_start.count(coord)>0:
                        cpu_start.remove(coord)
                    cpu_pos.remove(coord)
                    cpu_hit = True

            elif curr == []:
                if len(cpu_start)==0:
                    t2=False
                if t2:
                    coord = random.choice(cpu_start)
                    while grid_cpu_to_attack[coord[0]][coord[1]]<0:
                        if cpu_start.count(coord)>0:
                            cpu_start.remove(coord)
                        if  cpu_pos.count(coord)>0:
                            cpu_pos.remove(coord)
                        if len(cpu_start)>0:
                            coord = random.choice(cpu_start)
                        else:
                            coord = random.choice(cpu_pos)
                    if cpu_start.count(coord)>0:
                        cpu_start.remove(coord)
                    if cpu_pos.count(coord):
                        cpu_pos.remove(coord)
                else:
                    coord = random.choice(cpu_pos)
                    while grid_cpu_to_attack[coord[0]][coord[1]] < 0:
                        cpu_pos.remove(coord)
                        coord = random.choice(cpu_pos)
                    cpu_pos.remove(coord)

                curr = shot(grid_cpu_to_attack,f[1],coord[0],coord[1])
                if curr == "miss":
                    curr=[]
                    cpu_miss = True
                elif curr == "destroyed":
                    curr=[]
                    cpu_hit = True
                else:
                    shipdamaged.append(coord)
                    cpu_hit = True

            # curr_pos = random.choice(cpu_pos)
            # curr_x = curr_pos[0]
            # curr_y = curr_pos[1]
            # grid_cpu[curr_x][curr_y] = -1
            # if grid_cpu_to_attack[curr_x][curr_y] == 1:
            #     cpu_hit = True
            # else:
            #     cpu_miss = True
            # cpu_pos.remove(curr_pos)
            # print(i)

            for row in range(10):
                for column in range(10):
                    color = WHITE
                    if grid_cpu_to_attack[row][column] == -3:
                        color = BLUE
                       #
                    elif grid_cpu_to_attack[row][column] == -2:
                        color = GREEN
                        #time.sleep(1)
                    pygame.draw.rect(screen_person,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN + 900,
                                      (MARGIN + HEIGHT) * row + MARGIN + 100,
                                      WIDTH,
                                      HEIGHT])

            if cpu_hit:
                cpu_hit = False
                i += 2
                hp_user -= 1
                sum=0
                for j in range(10):
                    for h in range(len(f[1][j])):
                        sum+=f[1][j][h][2]
                if hp_user == 0 or sum==-40:

                    res = Tk()
                    center_window(500, 100, res)
                    result = Label(res,text = f"К сожалению, Вы проиграли", font=myFont)
                    text = f"К сожалению, Вы проиграли"
                    quit_butt = Button(res, text="Выход", command=quit, font=myFont)

                    result.pack()
                    quit_butt.pack()
                    res.mainloop()
                    done = True
            elif cpu_miss:
                cpu_miss = False
                i += 1

            if hp_cpu < 0:
                # Tk().wm_withdraw()  # to hide the main window
                # messagebox.showinfo("Конец игры", f"Поздравляю, Вы победили, ваши очки: {score}")
                # label.configure(text=f"{score}")
                res = Tk()
                center_window(500, 100, res)
                result = Label(res, text=f"Поздравляю, Вы победили, Ваши очки: {score}", font=myFont)
                quit_butt = Button(res, text="Выход", command=quit, font=myFont)

                result.pack()
                quit_butt.pack()
                res.mainloop()
                done = True

            print(hp_user)
            print("------------")
            print(hp_cpu)

            # Limit to 60 frames per second
            clock.tick(60)

        for row in range(10):
            for column in range(10):
                color = WHITE
                if grid_cpu_to_attack[row][column] == 1:
                    color = BLUE

                elif grid_cpu_to_attack[row][column] == 0:
                    color = WHITE
                    # time.sleep(1)
                pygame.draw.rect(screen_person,
                                 color,
                                 [(1 + 20) * column + 1 + 620,
                                  (1 + 20) * row + 1 + 500,
                                  20,
                                  20])


        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    pygame.quit()


def center_window(width=300, height=200, window=None):
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


def start_rules():
    rule = Tk()
    center_window(600, 400, rule)
    rule.title("Правила игры")
    rule.mainloop()


window = Tk()
label = Label(text="adasdas")

myFont = font.Font(size=42)

butt = Button(text="Начать играть", font = myFont, command=sea_battle,bg='#0052cc', fg='#ffffff')
rules_butt = Button(text="Правила игры", font = myFont, command=start_rules,bg='#0052cc', fg='#ffffff')
center_window(600, 400, window)
butt.place(x=80, y=25)
rules_butt.place(x=80, y=175)
label.place(x=75, y=800)
window.configure()
window.title("Морской бой")
window.mainloop()