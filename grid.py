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
        t1 = False
        t2 = False
        t3 = False
        t4 = False
        if right_coordinates(x, y - 1) and list[x][y - 1] > -2:
            positions.append([x, y - 1])
            t1 = list[x][y - 1] == 1
        if right_coordinates(x, y + 1) and list[x][y + 1] > -2:
            positions.append([x, y + 1])
            t2 = list[x][y + 1] == 1
        if right_coordinates(x - 1, y) and list[x - 1][y] > -2:
            positions.append([x - 1, y])
            t3 = list[x - 1][y] == 1
        if right_coordinates(x + 1, y) and list[x + 1][y] > -2:
            positions.append([x + 1, y])
            t4 = list[x + 1][y] == 1

        sh = 0
        while not [x, y, state1] in ships[sh]:
            sh += 1
        ships[sh][ships[sh].index([x, y, state1])][2] = -2
        sum = 0
        for c in range(len(ships[sh])):
            sum += ships[sh][c][2]

        destroyed = sum == -2 * len(ships[sh])

        if len(positions) == 0 and destroyed:
            return "destroyed"
        elif (t1 or t2 or t3 or t4) == False and destroyed:
            if right_coordinates(x, y - 1) and list[x][y - 1] != -2:
                list[x][y - 1] = -3
            if right_coordinates(x, y + 1) and list[x][y + 1] != -2:
                list[x][y + 1] = -3
            if right_coordinates(x - 1, y) and list[x - 1][y] != -2:
                list[x - 1][y] = -3
            if right_coordinates(x + 1, y) and list[x + 1][y] != -2:
                list[x + 1][y] = -3

            return "destroyed"
        elif len(positions) == 0 or (t1 or t2 or t3 or t4) == False:
            return "alive but no list"

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

    cpu_pos = [[x,y] for x in range(10) for y in range(10)]


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

    hp_cpu = 75274525
    hp_user = 4545754
    score = 100
    # -------- Main Program Loop -----------
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
            print(curr)
            if curr != []:

                coord = random.choice(curr)
                grid_cpu[coord[0]][coord[1]] = -1
                next_curr = shot(grid_cpu_to_attack,f[1],coord[0],coord[1])
                print(next_curr)
                if type(next_curr) == list:
                    curr = curr + next_curr
                elif next_curr == "miss":
                    curr.remove(coord)
                    cpu_pos.remove(coord)
                    cpu_miss = True
                elif next_curr == "destroyed":
                    curr = []
                    cpu_hit = True
                elif next_curr == "alive but no list":
                    curr.remove(coord)
                    cpu_pos.remove(coord)
                    cpu_hit = True

            elif curr == []:
                coord = random.choice(cpu_pos)
                while grid_cpu_to_attack[coord[0]][coord[1]]<0 :
                    cpu_pos.remove(coord)
                    coord = random.choice(cpu_pos)
                grid_cpu[coord[0]][coord[1]] = -1

                curr = shot(grid_cpu_to_attack,f[1],coord[0],coord[1])
                print(curr)
                if curr == "miss":
                    curr = []
                    cpu_miss = True
                elif curr == "destroyed":
                    curr = []
                    cpu_hit = True
                elif type(curr) == list and curr != []:
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
                    if grid_cpu[row][column] == -1 and grid_cpu_to_attack[row][column] == -3 or (grid_cpu[row][column] ==0 and ( grid_cpu_to_attack[row][column] == -1 or grid_cpu_to_attack[row][column] == -3)):
                        color = BLUE
                       #
                    elif grid_cpu[row][column] == -1 and grid_cpu_to_attack[row][column] == -2:
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
                if hp_user == 0:

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
