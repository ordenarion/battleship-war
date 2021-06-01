import pygame
from tkinter import *
from tkinter import messagebox, font
import random
import operator
import time


def right_coordinates(x, y):
    return x > -1 and x < 10 and y > -1 and y < 10

state0 = 0
state1 = 1

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


def sea_battle(user_ships):
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (120, 171, 235)
    BG = (110, 131, 156)
    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 40
    HEIGHT = 40

    # This sets the margin between each cell
    MARGIN = 5

    cpu_pos = [[x, y] for x in range(10) for y in range(10)]

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
    sample = optimal_start_position()[0]

    grid_cpu = []
    for row in range(10):
        # Add an empty array that will hold each cell
        # in this row
        grid_cpu.append([])
        for column in range(10):
            grid_cpu[row].append(0)  # Append a cell
    # Initialize pygame
    f = user_ships
    grid_cpu_to_attack = f[
        0]  # [[1, 0, 1, 1, 1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 1]]

    curr = []
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [1500, 800]
    screen_person = pygame.display.set_mode(WINDOW_SIZE)
    screen_cpu = pygame.display.set_mode(WINDOW_SIZE)
    # Set title of screen
    pygame.display.set_caption(
        "Основной этап: В левом поле стреляет игрок, В правом поле стреляет компьютер. По центру отображается выбранная пользователем расстановка кораблей")

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

    hp_user = 20
    # -------- Main Program Loop -----------
    while not done:
        score = 10
        hp_cpu = 20
        #        label.configure(text=None)

        if i % 2 == 0:

            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN) - 2
                    row = pos[1] // (HEIGHT + MARGIN) - 2
                    print(pos)
                    if column > 9 or row > 9:
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
                                     [(MARGIN + WIDTH) * column + MARGIN + 100,
                                      (MARGIN + HEIGHT) * row + MARGIN + 100,
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
                grid_cpu[coord[0]][coord[1]] = -1
                next_curr = shot(grid_cpu_to_attack, f[1], coord[0], coord[1])
                if next_curr == "miss":
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
                while grid_cpu_to_attack[coord[0]][coord[1]] < 0:
                    cpu_pos.remove(coord)
                    coord = random.choice(cpu_pos)
                grid_cpu[coord[0]][coord[1]] = -1

                curr = shot(grid_cpu_to_attack, f[1], coord[0], coord[1])
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
                    if grid_cpu[row][column] == -1 and grid_cpu_to_attack[row][column] == -3:
                        color = BLUE
                    #
                    elif grid_cpu[row][column] == -1 and grid_cpu_to_attack[row][column] == -2:
                        color = GREEN
                        # time.sleep(1)
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
                    result = Label(res, text=f"К сожалению, Вы проиграли", font=myFont)
                    text = f"К сожалению, Вы проиграли"
                    quit_butt = Button(res, text="Выход", command=quit, font=myFont)

                    result.pack()
                    quit_butt.pack()
                    res.mainloop()
                    done = True
            elif cpu_miss:
                cpu_miss = False
                i += 1

        if hp_cpu <= 0:
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
    label1 = Label(rule, text ="Морской бой – игра, в которой участвуют 2 игрока, пытающиеся уничтожить корабли друг друга.\nПобеждает игрок, который первый уничтожит все корабли соперника.")
    label2 = Label(rule, text = "Стадии игры:")
    label3 = Label(rule, text = "1.Перед партией каждый игрок размещает 10 кораблей")
    label4 = Label(rule, text = "(1 четырехпалубный, 2 трехпалубных, 3 двухпалубных и 4 однопалубных) на поле 10 на 10. ")
    label5 = Label(rule, text = "N-палубный корабль представляет собой прямую линию из N подряд идущих клеток. ")
    label6 = Label(rule, text = "При расставлении кораблей запрещается, размещать их таким образом,")
    label7 = Label(rule, text = "чтобы части разных кораблей пересекались или касались друг друга, в том числе по диагонали.")
    label8 = Label(rule, text = "2.Помимо поля с собственными кораблями, у каждого игрока есть пустое поле 10 на 10,")
    label9 = Label(rule, text = "по которому будут производится выстрелы по кораблям противника.")
    label10 = Label(rule, text = "Игроки не знают расположение кораблей друг друга, в начале партии.")
    label11 = Label(rule, text = "Игроки по очереди осуществляют выстрелы во вражеские корабли.")
    label12 = Label(rule, text = "Выстрел осуществляется следующим образом:")
    label13 = Label(rule, text = "стреляющий игрок выбирает клетку на поле противника, говорит ее противнику, который отвечает,")
    label14 = Label(rule, text = "есть ли в клетке часть какого-то корабля. Если в выбранной клетке была часть корабля,")
    label15 = Label(rule, text = "то клетка помечается как раненая, а игрок осуществляет повторный выстрел.")
    label16 = Label(rule, text = "Иначе ход переходит к сопернику.")
    label17 = Label(rule, text = "3.Игра заканчивается, когда какой-то из игроков ранил последнюю,")
    label18 = Label(rule, text = "из оставшихся клеток кораблей противника, тем самым уничтожив все корабли.")
    label1.place(x=0,y=0)
    label2.place(x=0,y=30)
    label3.place(x=0,y=60)
    label4.place(x=0,y=80)
    label5.place(x=0,y=100)
    label6.place(x=0,y=120)
    label7.place(x=0,y=140)
    label8.place(x=0,y=170)
    label9.place(x=0,y=190)
    label10.place(x=0,y=210)
    label11.place(x=0,y=230)
    label12.place(x=0,y=250)
    label13.place(x=0,y=270)
    label14.place(x=0,y=290)
    label15.place(x=0,y=310)
    label16.place(x=0,y=330)
    label17.place(x=0,y=360)
    label18.place(x=0,y=380)
    rule.mainloop()


def placing():
    allpairs = []
    pointsforships = []
    toCheck = []
    finalToCheck = []
    grid_for_shot = []
    finalGrid = []
    for row in range(10):
        grid_for_shot.append([])
        for column in range(10):
            grid_for_shot[row].append(0)
        # window = Tk()
    # window.geometry("800x600")
    # window.title("Разместите свои корабли")
    #
    #
    # window.mainloop()
    WIDTH = 55
    HEIGHT = 55
    GREEN = (0, 255, 0)
    SHIPCOL = (106, 90, 205)

    def points(x):
        res = []
        for curr in x:
            if curr[0] == curr[1] and curr[2] == curr[3]:
                res.append([curr[0], curr[2], 1])

            elif curr[0] == curr[1] and curr[2] != curr[3]:
                min_coord = min(curr[2], curr[3])
                max_coord = max(curr[2], curr[3])

                m = [[curr[0], i, 1] for i in range(min_coord, max_coord + 1)]
                res.append(m)

            elif curr[0] != curr[1] and curr[2] == curr[3]:
                min_coord = min(curr[0], curr[1])
                max_coord = max(curr[0], curr[1])

                m = [[i, curr[2], 1] for i in range(min_coord, max_coord + 1)]
                res.append(m)

        return res

    def flatten_lvl_1(x):
        k = []
        for i in x:
            for j in i:
                if isinstance(j, list):
                    k.append(j)
                else:
                    k.append(i)
                    break

        return k

    class ShipASAS(pygame.sprite.Sprite):
        def __init__(self, height, width, n, x, y, asym=1):
            pygame.sprite.Sprite.__init__(self)
            self.h = height
            self.w = width
            self.n = n
            self.x = x
            self.y = y
            if asym == 1:
                self.image = pygame.Surface(((height) * n + (n - 1) * 5, width))
            elif asym == 2:
                self.image = pygame.Surface((width, (height) * n + (n - 1) * 5))
            self.image.fill(SHIPCOL)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

        def rotate(self, x=None, y=None):
            if x == None and y == None:
                x, y = self.x, self.y

            self.image = pygame.transform.rotate(self.image, 90)
            self.rect = self.image.get_rect(center=(x, y))

        def extreme_points(self):
            self.yUp = self.rect.left // (self.w + 5) - 1
            self.yDown = (self.rect.right - 100) // (self.w + 5) - 1
            self.xLeft = (self.rect.top + 100) // (self.w + 5) - 3
            self.xRight = self.rect.bottom // (self.w + 5) - 2
            self.extra = [self.xLeft, self.xRight, self.yUp, self.yDown]
            return self.extra

    # all_sprites = pygame.sprite.Group()
    # ship1 = ShipASAS(HEIGHT,WIDTH,3)
    # all_sprites.add(ship1)

    # image = pygame.image.load("подпись.png")
    color = GREEN

    pygame.init()

    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)

    WINDOW_SIZE = [1500, 800]
    screen_person = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(
        "Начальное размещение кораблей: после размещения нажмите кнопку ""Стрелка вверх"". Если статус бар горит Красным - Вам следует переставить Ваши корабли более корректно, если Зеленым - можете закрывать окно ")

    running = True
    rectangle_draging = False

    # This sets the margin between each cell
    MARGIN = 5
    color1 = RED
    rectangle = pygame.rect.Rect(1, 1, 100, 50)
    ship4 = ShipASAS(HEIGHT, WIDTH, 4, 800, 300, 2)
    # ship4 = ShipASAS(HEIGHT,WIDTH,4,0,0,2)
    # print(ship4.rect.bottomright)
    ship31 = ShipASAS(HEIGHT, WIDTH, 3, 965, 390)
    ship32 = ShipASAS(HEIGHT, WIDTH, 3, 1190, 390)
    ship21 = ShipASAS(HEIGHT, WIDTH, 2, 905, 240, 2)
    ship22 = ShipASAS(HEIGHT, WIDTH, 2, 1020, 240, 2)
    ship23 = ShipASAS(HEIGHT, WIDTH, 2, 1135, 240, 2)
    ship11 = ShipASAS(HEIGHT, WIDTH, 1, 1355, 390)
    ship12 = ShipASAS(HEIGHT, WIDTH, 1, 1355, 270)
    ship13 = ShipASAS(HEIGHT, WIDTH, 1, 1250, 270)
    ship14 = ShipASAS(HEIGHT, WIDTH, 1, 900, 600)

    # rectangle2 = pygame.rect.Rect(176, 164, 30, 30)
    # rectangle3 = pygame.rect.Rect(176, 194, 30, 30)
    ship_sprites = pygame.sprite.Group()
    ship_sprites.add(ship4, ship31, ship32, ship21, ship22, ship23, ship14, ship11, ship13, ship12)
    # s.add(rectangle1)
    # s.add(rectangle2)
    # s.add(rectangle3)
    # screen_person.fill(WHITE)
    # for row in range(10):
    #     for column in range(10):
    #         color = RED
    #         pygame.draw.rect(screen_person,
    #                          color,
    #                          [(MARGIN + WIDTH) * column + MARGIN + 100,
    #                           (MARGIN + HEIGHT) * row + MARGIN + 100,
    #                           WIDTH,
    #                           HEIGHT])
    curr_ship = ship14
    while running:
        # ship1.update()
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(event.pos)
                    for ship in ship_sprites:
                        if ship.rect.collidepoint(event.pos):
                            rectangle_draging = True
                            mouse_x, mouse_y = event.pos
                            mouse_event = tuple(i * (-1) for i in event.pos)
                            offset = tuple(map(operator.add, ship.rect.center, mouse_event))
                            # offset_x = rectangle.x - mouse_x
                            # offset_y = rectangle.y - mouse_y
                            curr_ship = ship

                elif event.button == 3 and curr_ship != None:
                    curr_ship.rotate(mouse_x, mouse_y)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    rectangle_draging = False
                    # print(curr_ship.rect.bottom)
                    # print("Дно ")
                    # print((curr_ship.rect.bottom)//(WIDTH+MARGIN)-2)
                    # print("Верх")
                    # print((curr_ship.rect.top+100)//(HEIGHT+MARGIN)-3)
                    # print("Лево")
                    # print(curr_ship.rect.left//(HEIGHT+MARGIN)-1)
                    # print("Право")
                    # print((curr_ship.rect.right-100)//(WIDTH+MARGIN)-1)
                    ##
                    print(curr_ship.rect.bottom)
                    print("Дно ")
                    print((curr_ship.rect.bottom) // (WIDTH + MARGIN) - 2)
                    print("Верх")
                    print((curr_ship.rect.top + 100) // (HEIGHT + MARGIN) - 3)
                    print("Лево")
                    print(curr_ship.rect.left // (HEIGHT + MARGIN) - 1)
                    print("Право")
                    print((curr_ship.rect.right - 100) // (WIDTH + MARGIN) - 1)
                    print(curr_ship.extreme_points())

            elif event.type == pygame.MOUSEMOTION:
                if rectangle_draging:
                    mouse_x, mouse_y = event.pos
                    # ship1.rect.center = (mouse_x,mouse_y) + offset
                    curr_ship.rect.center = tuple(map(operator.add, event.pos, offset))
                    # curr_ship.rotate(mouse_x,mouse_y)
                    # rectangle.x = mouse_x + offset_x
                    # rectangle.y = mouse_y + offset_y
                    # - draws (without updates) -
                # elif rectangle_draging and event.key == pygame.KEYDOWN:
                #   mouse_x, mouse_y = event.pos
                #  curr_ship.rect.center = tuple(map(operator.add, event.pos, offset))
                # curr_ship.rotate(mouse_x,mouse_y)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    allpairs = []
                    for ship in ship_sprites:
                        allpairs.append(ship.extreme_points())
                    # print(allpairs)
                    pointsforships = points(allpairs)
                    toCheck = flatten_lvl_1(pointsforships)
                    flag2 = False

                    for i in toCheck:
                        if i[0] > 9 or i[1] > 9 or i[0] < 0 or i[1] < 0:
                            flag2 = True
                            break
                    if flag2:
                        finalToCheck = [1]

                    else:
                        finalToCheck = set(tuple(row) for row in toCheck)
                    # print(toCheck)
                    print("-------------------")

                    if len(finalToCheck) < len(toCheck):
                        color1 = RED
                        # pass #Ошибка, поменйте раположение
                        print(finalToCheck)
                        print(toCheck)

                    elif len(finalToCheck) == len(toCheck):
                        # Заполняем сетку 1 где поинты, используем инфу из toCheck
                        for point in toCheck:
                            grid_for_shot[point[0]][point[1]] = 1
                            color1 = GREEN
                        finalGrid = list(map(list, [grid_for_shot] + [pointsforships]))
                    print(finalGrid)
                    print(finalToCheck)
                    print(toCheck)
                    print(len(toCheck))
                    print(len(finalToCheck))
                    # Потом объединяем сетку и pointsforships
                    # print(toCheck)
                    # print(grid_for_shot)

            if event.type == pygame.QUIT and color1 == GREEN:
                running = False
                pygame.quit()
                sea_battle(finalGrid)


            elif event.type == pygame.QUIT and color1 == RED:
                running = False

        screen_person.fill(WHITE)
        pygame.draw.rect(screen_person, color1, (10, 10, 100, 50))
        pygame.draw.rect(screen_person, BLACK, (10, 10, 100, 50), 2)

        for row in range(10):
            for column in range(10):
                color = BLACK
                pygame.draw.rect(screen_person,
                                 BLACK,
                                 [(MARGIN + WIDTH) * column + MARGIN + 100,
                                  (MARGIN + HEIGHT) * row + MARGIN + 100,
                                  WIDTH,
                                  HEIGHT])

        pygame.draw.rect(screen_person, BLACK,
                         pygame.Rect(100, 100, (MARGIN + WIDTH) * 10 + MARGIN, (MARGIN + HEIGHT) * 10 + MARGIN), 2)
        # pygame.draw.rect(screen_person, GREEN, rectangle)
        for ship in ship_sprites:
            screen_person.blit(ship.image, ship.rect)

        # screen_person.blit(ship2.image,ship2.rect)
        # screen_person.blit(ship3.image,ship3.rect)
        # screen_person.blit(ship4.image,ship4.rect)
        # screen_person.blit(ship5.image,ship5.rect)
        pygame.display.flip()

    pygame.display.flip()
    pygame.quit()




def randomUserGrid():
    usergrid = [[0 for i in range(10)] for j in range(10)]
    squares = [(i, j) for i in range(10) for j in range(10)]
    shipnum = 0
    ships = [[] for i in range(10)]

    notplaced = True
    wrongsquares = []
    while notplaced:
        direction = [0, 1, 2, 3]
        sh = random.randint(0, len(squares) - 1)
        (x, y) = squares[sh]
        while notplaced and len(direction) > 0:
            index = random.randint(0, len(direction) - 1)
            if direction[index] == 0:
                if x - 3 >= 0:
                    for i in range(4):

                        ships[0].append([x - i, y, 1])
                        usergrid[x - i][y] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x - i + j1, y + j2) and usergrid[x - i + j1][y + j2] != 1:
                                    usergrid[x - i + j1][y + j2] = -2
                                    if squares.count((x - i + j1, y + j2)) > 0:
                                        squares.remove((x - i + j1, y + j2))
                    notplaced = False
                else:
                    direction.remove(0)

            elif direction[index] == 1:
                if x + 3 <= 9:

                    for i in range(4):

                        ships[0].append([x + i, y, 1])
                        usergrid[x + i][y] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + i + j1, y + j2) and usergrid[x + i + j1][y + j2] != 1:
                                    usergrid[x + i + j1][y + j2] = -2
                                    if squares.count((x + i + j1, y + j2)) > 0:
                                        squares.remove((x + i + j1, y + j2))
                    notplaced = False
                else:
                    direction.remove(1)

            elif direction[index] == 2:
                if y - 3 >= 0:
                    for i in range(4):

                        ships[0].append([x, y - i, 1])
                        usergrid[x][y - i] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + j1, y - i + j2) and usergrid[x + j1][y - i + j2] != 1:
                                    usergrid[x + j1][y - i + j2] = -2
                                    if squares.count((x + j1, y - i + j2)) > 0:
                                        squares.remove((x + j1, y - i + j2))
                    notplaced = False
                else:
                    direction.remove(2)

            elif direction[index] == 3:
                if y + 3 <= 9:
                    for i in range(4):

                        ships[0].append([x, y + i, 1])
                        usergrid[x][y + i] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + j1, y + i + j2) and usergrid[x + j1][y + i + j2] != 1:
                                    usergrid[x + j1][y + i + j2] = -2
                                    if squares.count((x + j1, y + i + j2)) > 0:
                                        squares.remove((x + j1, y + i + j2))
                    notplaced = False
                else:
                    direction.remove(3)

        if notplaced:

            if squares.count((x, y)) > 0:
                squares.remove((x, y))
                wrongsquares.append((x, y))

    notplaced = True
    for i in range(len(wrongsquares)):
        if usergrid[wrongsquares[i][0]][wrongsquares[i][1]] == 0:
            squares.append(wrongsquares[i])
    wrongsquares = []

    while notplaced:
        direction = [0, 1, 2, 3]
        sh = random.randint(0, len(squares) - 1)
        (x, y) = squares[sh]
        while notplaced and len(direction) > 0:
            index = random.randint(0, len(direction) - 1)
            if direction[index] == 0:
                if x - 2 >= 0 and usergrid[x - 1][y] == 0 and usergrid[x - 2][y] == 0:
                    for i in range(3):

                        ships[2].append([x - i, y, 1])
                        usergrid[x - i][y] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x - i + j1, y + j2) and usergrid[x - i + j1][y + j2] != 1:
                                    usergrid[x - i + j1][y + j2] = -2
                                    if squares.count((x - i + j1, y + j2)) > 0:
                                        squares.remove((x - i + j1, y + j2))
                    notplaced = False
                else:
                    direction.remove(0)

            elif direction[index] == 1:
                if x + 2 <= 9 and usergrid[x + 1][y] == 0 and usergrid[x + 2][y] == 0:
                    for i in range(3):

                        ships[2].append([x + i, y, 1])
                        usergrid[x + i][y] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + i + j1, y + j2) and usergrid[x + i + j1][y + j2] != 1:
                                    usergrid[x + i + j1][y + j2] = -2
                                    if squares.count((x + i + j1, y + j2)) > 0:
                                        squares.remove((x + i + j1, y + j2))
                    notplaced = False
                else:
                    direction.remove(1)

            elif direction[index] == 2:
                if y - 2 >= 0 and usergrid[x][y - 1] == 0 and usergrid[x][y - 2] == 0:
                    for i in range(3):

                        ships[2].append([x, y - i, 1])
                        usergrid[x][y - i] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + j1, y - i + j2) and usergrid[x + j1][y - i + j2] != 1:
                                    usergrid[x + j1][y - i + j2] = -2
                                    if squares.count((x + j1, y - i + j2)) > 0:
                                        squares.remove((x + j1, y - i + j2))
                    notplaced = False
                else:
                    direction.remove(2)

            elif direction[index] == 3:
                if y + 2 <= 9 and usergrid[x][y + 1] == 0 and usergrid[x][y + 2] == 0:
                    for i in range(3):

                        ships[2].append([x, y + i, 1])
                        usergrid[x][y + i] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + j1, y + i + j2) and usergrid[x + j1][y + i + j2] != 1:
                                    usergrid[x + j1][y + i + j2] = -2
                                    if squares.count((x + j1, y + i + j2)) > 0:
                                        squares.remove((x + j1, y + i + j2))
                    notplaced = False
                else:
                    direction.remove(3)

        if notplaced:

            if squares.count((x, y)) > 0:
                squares.remove((x, y))
                wrongsquares.append((x, y))

    notplaced = True
    for i in range(len(wrongsquares)):
        if usergrid[wrongsquares[i][0]][wrongsquares[i][1]] == 0:
            squares.append(wrongsquares[i])
    wrongsquares = []

    while notplaced:
        direction = [0, 1, 2, 3]
        sh = random.randint(0, len(squares) - 1)
        (x, y) = squares[sh]
        while notplaced and len(direction) > 0:
            index = random.randint(0, len(direction) - 1)
            if direction[index] == 0:
                if x - 2 >= 0 and usergrid[x - 1][y] == 0 and usergrid[x - 2][y] == 0:
                    for i in range(3):

                        ships[1].append([x - i, y, 1])
                        usergrid[x - i][y] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x - i + j1, y + j2) and usergrid[x - i + j1][y + j2] != 1:
                                    usergrid[x - i + j1][y + j2] = -2
                                    if squares.count((x - i + j1, y + j2)) > 0:
                                        squares.remove((x - i + j1, y + j2))
                    notplaced = False
                else:
                    direction.remove(0)

            elif direction[index] == 1:
                if x + 2 <= 9 and usergrid[x + 1][y] == 0 and usergrid[x + 2][y] == 0:
                    for i in range(3):

                        ships[1].append([x + i, y, 1])
                        usergrid[x + i][y] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + i + j1, y + j2) and usergrid[x + i + j1][y + j2] != 1:
                                    usergrid[x + i + j1][y + j2] = -2
                                    if squares.count((x + i + j1, y + j2)) > 0:
                                        squares.remove((x + i + j1, y + j2))
                    notplaced = False
                else:
                    direction.remove(1)

            elif direction[index] == 2:
                if y - 2 >= 0 and usergrid[x][y - 1] == 0 and usergrid[x][y - 2] == 0:
                    for i in range(3):

                        ships[1].append([x, y - i, 1])
                        usergrid[x][y - i] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + j1, y - i + j2) and usergrid[x + j1][y - i + j2] != 1:
                                    usergrid[x + j1][y - i + j2] = -2
                                    if squares.count((x + j1, y - i + j2)) > 0:
                                        squares.remove((x + j1, y - i + j2))
                    notplaced = False
                else:
                    direction.remove(2)

            elif direction[index] == 3:
                if y + 2 <= 9 and usergrid[x][y + 1] == 0 and usergrid[x][y + 2] == 0:
                    for i in range(3):

                        ships[1].append([x, y + i, 1])
                        usergrid[x][y + i] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + j1, y + i + j2) and usergrid[x + j1][y + i + j2] != 1:
                                    usergrid[x + j1][y + i + j2] = -2
                                    if squares.count((x + j1, y + i + j2)) > 0:
                                        squares.remove((x + j1, y + i + j2))
                    notplaced = False
                else:
                    direction.remove(3)

        if notplaced:

            if squares.count((x, y)) > 0:
                squares.remove((x, y))
                wrongsquares.append((x, y))

    notplaced = True
    for i in range(len(wrongsquares)):
        if usergrid[wrongsquares[i][0]][wrongsquares[i][1]] == 0:
            squares.append(wrongsquares[i])
    wrongsquares = []

    while notplaced:
        direction = [0, 1, 2, 3]
        sh = random.randint(0, len(squares) - 1)
        (x, y) = squares[sh]
        while notplaced and len(direction) > 0:
            index = random.randint(0, len(direction) - 1)
            if direction[index] == 0:
                if x - 1 >= 0 and usergrid[x - 1][y] == 0:
                    for i in range(2):

                        ships[3].append([x - i, y, 1])
                        usergrid[x - i][y] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x - i + j1, y + j2) and usergrid[x - i + j1][y + j2] != 1:
                                    usergrid[x - i + j1][y + j2] = -2
                                    if squares.count((x - i + j1, y + j2)) > 0:
                                        squares.remove((x - i + j1, y + j2))
                    notplaced = False
                else:
                    direction.remove(0)

            elif direction[index] == 1:
                if x + 1 <= 9 and usergrid[x + 1][y] == 0:
                    for i in range(2):

                        ships[3].append([x + i, y, 1])
                        usergrid[x + i][y] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + i + j1, y + j2) and usergrid[x + i + j1][y + j2] != 1:
                                    usergrid[x + i + j1][y + j2] = -2
                                    if squares.count((x + i + j1, y + j2)) > 0:
                                        squares.remove((x + i + j1, y + j2))
                    notplaced = False
                else:
                    direction.remove(1)

            elif direction[index] == 2:
                if y - 1 >= 0 and usergrid[x][y - 1] == 0 == 0:
                    for i in range(2):

                        ships[3].append([x, y - i, 1])
                        usergrid[x][y - i] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + j1, y - i + j2) and usergrid[x + j1][y - i + j2] != 1:
                                    usergrid[x + j1][y - i + j2] = -2
                                    if squares.count((x + j1, y - i + j2)) > 0:
                                        squares.remove((x + j1, y - i + j2))
                    notplaced = False
                else:
                    direction.remove(2)

            elif direction[index] == 3:
                if y + 1 <= 9 and usergrid[x][y + 1] == 0:
                    for i in range(2):

                        ships[3].append([x, y + i, 1])
                        usergrid[x][y + i] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + j1, y + i + j2) and usergrid[x + j1][y + i + j2] != 1:
                                    usergrid[x + j1][y + i + j2] = -2
                                    if squares.count((x + j1, y + i + j2)) > 0:
                                        squares.remove((x + j1, y + i + j2))
                    notplaced = False
                else:
                    direction.remove(3)

        if notplaced:

            if squares.count((x, y)) > 0:
                squares.remove((x, y))
                wrongsquares.append((x, y))

    notplaced = True
    for i in range(len(wrongsquares)):
        if usergrid[wrongsquares[i][0]][wrongsquares[i][1]] == 0:
            squares.append(wrongsquares[i])
    wrongsquares = []

    while notplaced:
        direction = [0, 1, 2, 3]
        sh = random.randint(0, len(squares) - 1)
        (x, y) = squares[sh]
        while notplaced and len(direction) > 0:
            index = random.randint(0, len(direction) - 1)
            if direction[index] == 0:
                if x - 1 >= 0 and usergrid[x - 1][y] == 0:
                    for i in range(2):

                        ships[4].append([x - i, y, 1])
                        usergrid[x - i][y] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x - i + j1, y + j2) and usergrid[x - i + j1][y + j2] != 1:
                                    usergrid[x - i + j1][y + j2] = -2
                                    if squares.count((x - i + j1, y + j2)) > 0:
                                        squares.remove((x - i + j1, y + j2))
                    notplaced = False
                else:
                    direction.remove(0)

            elif direction[index] == 1:
                if x + 1 <= 9 and usergrid[x + 1][y] == 0:
                    for i in range(2):

                        ships[4].append([x + i, y, 1])
                        usergrid[x + i][y] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + i + j1, y + j2) and usergrid[x + i + j1][y + j2] != 1:
                                    usergrid[x + i + j1][y + j2] = -2
                                    if squares.count((x + i + j1, y + j2)) > 0:
                                        squares.remove((x + i + j1, y + j2))
                    notplaced = False
                else:
                    direction.remove(1)

            elif direction[index] == 2:
                if y - 1 >= 0 and usergrid[x][y - 1] == 0 == 0:
                    for i in range(2):

                        ships[4].append([x, y - i, 1])
                        usergrid[x][y - i] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + j1, y - i + j2) and usergrid[x + j1][y - i + j2] != 1:
                                    usergrid[x + j1][y - i + j2] = -2
                                    if squares.count((x + j1, y - i + j2)) > 0:
                                        squares.remove((x + j1, y - i + j2))
                    notplaced = False
                else:
                    direction.remove(2)

            elif direction[index] == 3:
                if y + 1 <= 9 and usergrid[x][y + 1] == 0:
                    for i in range(2):

                        ships[4].append([x, y + i, 1])
                        usergrid[x][y + i] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + j1, y + i + j2) and usergrid[x + j1][y + i + j2] != 1:
                                    usergrid[x + j1][y + i + j2] = -2
                                    if squares.count((x + j1, y + i + j2)) > 0:
                                        squares.remove((x + j1, y + i + j2))
                    notplaced = False
                else:
                    direction.remove(3)

        if notplaced:

            if squares.count((x, y)) > 0:
                squares.remove((x, y))
                wrongsquares.append((x, y))

    notplaced = True
    for i in range(len(wrongsquares)):
        if usergrid[wrongsquares[i][0]][wrongsquares[i][1]] == 0:
            squares.append(wrongsquares[i])
    wrongsquares = []

    while notplaced:
        direction = [0, 1, 2, 3]
        sh = random.randint(0, len(squares) - 1)
        (x, y) = squares[sh]
        while notplaced and len(direction) > 0:
            index = random.randint(0, len(direction) - 1)
            if direction[index] == 0:
                if x - 1 >= 0 and usergrid[x - 1][y] == 0:
                    for i in range(2):

                        ships[5].append([x - i, y, 1])
                        usergrid[x - i][y] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x - i + j1, y + j2) and usergrid[x - i + j1][y + j2] != 1:
                                    usergrid[x - i + j1][y + j2] = -2
                                    if squares.count((x - i + j1, y + j2)) > 0:
                                        squares.remove((x - i + j1, y + j2))
                    notplaced = False
                else:
                    direction.remove(0)

            elif direction[index] == 1:
                if x + 1 <= 9 and usergrid[x + 1][y] == 0:
                    for i in range(2):

                        ships[5].append([x + i, y, 1])
                        usergrid[x + i][y] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + i + j1, y + j2) and usergrid[x + i + j1][y + j2] != 1:
                                    usergrid[x + i + j1][y + j2] = -2
                                    if squares.count((x + i + j1, y + j2)) > 0:
                                        squares.remove((x + i + j1, y + j2))
                    notplaced = False
                else:
                    direction.remove(1)

            elif direction[index] == 2:
                if y - 1 >= 0 and usergrid[x][y - 1] == 0 == 0:
                    for i in range(2):

                        ships[5].append([x, y - i, 1])
                        usergrid[x][y - i] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + j1, y - i + j2) and usergrid[x + j1][y - i + j2] != 1:
                                    usergrid[x + j1][y - i + j2] = -2
                                    if squares.count((x + j1, y - i + j2)) > 0:
                                        squares.remove((x + j1, y - i + j2))
                    notplaced = False
                else:
                    direction.remove(2)

            elif direction[index] == 3:
                if y + 1 <= 9 and usergrid[x][y + 1] == 0:
                    for i in range(2):

                        ships[5].append([x, y + i, 1])
                        usergrid[x][y + i] = 1
                        for j1 in range(-1, 2):
                            for j2 in range(-1, 2):
                                if right_coordinates(x + j1, y + i + j2) and usergrid[x + j1][y + i + j2] != 1:
                                    usergrid[x + j1][y + i + j2] = -2
                                    if squares.count((x + j1, y + i + j2)) > 0:
                                        squares.remove((x + j1, y + i + j2))
                    notplaced = False
                else:
                    direction.remove(3)

        if notplaced:

            if squares.count((x, y)) > 0:
                squares.remove((x, y))
                wrongsquares.append((x, y))

    notplaced = True
    for i in range(len(wrongsquares)):
        if usergrid[wrongsquares[i][0]][wrongsquares[i][1]] == 0:
            squares.append(wrongsquares[i])

    i = 0
    while i < 4:
        sh = random.randint(0, len(squares) - 1)
        (x, y) = squares[sh]
        if usergrid[x][y] != 1:
            i += 1
            usergrid[x][y] = 1
            ships[6 + i - 1].append([x, y, 1])
            for j1 in range(-1, 2):
                for j2 in range(-1, 2):
                    if right_coordinates(x + j1, y + j2) and usergrid[x + j1][y + j2] != 1:
                        usergrid[x + j1][y + j2] = -2
                        if squares.count((x + j1, y + j2)) > 0:
                            squares.remove((x + j1, y + j2))
        else:
            squares.remove((x, y))

    for i in range(10):
        for j in range(10):
            if usergrid[i][j] == -2:
                usergrid[i][j] = 0

    return [usergrid, ships]


def randomShip():
    pygame.init()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    SHIPCOL = (106, 90, 205)
    WIDTH = 55
    HEIGHT = 55
    MARGIN = 5

    WINDOW_SIZE = [800, 800]
    screen_person = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(
        "Случайная расстановка кораблей. Для повторного перевыбора нажмите Стрелку вверх, а после закройте окно")
    running = True
    f = randomUserGrid()
    toDraw = f[0]
    while running:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    f = randomUserGrid()
                    toDraw = f[0]
            elif event.type == pygame.QUIT:
                pygame.quit()
                return f

        screen_person.fill(WHITE)

        for row in range(10):
            for column in range(10):
                if toDraw[row][column] == 0:
                    color = BLACK
                else:
                    color = SHIPCOL
                pygame.draw.rect(screen_person,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN + 100,
                                  (MARGIN + HEIGHT) * row + MARGIN + 100,
                                  WIDTH,
                                  HEIGHT])

        pygame.draw.rect(screen_person, BLACK,
                         pygame.Rect(100, 100, (MARGIN + WIDTH) * 10 + MARGIN, (MARGIN + HEIGHT) * 10 + MARGIN), 2)

        pygame.display.flip()

    pygame.display.flip()
    pygame.quit()

def randomizeShipSelection():
    f = randomShip()
    sea_battle(f)
# for k in range(10):
#         print(pole[k])
#
# for k in range(10):
#         print(korabl[k])
# print(randomUserGrid())

def prepare_to_place():
    window1 = Tk()
    myFont1 = font.Font(family='Helvetica', size=36, weight='bold')
    label1 = Label(window1, font=myFont1, text=" Вам предстоить выбрать, как разместить корабли перед сражением:")
    solo = Button(window1, text="Выбрать самостоятельно", font=myFont1, command=placing, bg='#0052cc',
                  fg='#ffffff', height=5, width=59)
    random = Button(window1, text="Довериться воле случая", font=myFont, command=randomizeShipSelection, bg='#0052cc',
                    fg='#ffffff', height=5, width=59)
    center_window(600, 400, window1)
    solo.place(x=30, y=100)
    # solo.configure(font = myFont1)
    random.place(x=30, y=250)
    label1.place(x=30, y=50)
    window1.title("Сложный выбор")
    # center_window(600, 400, window1)
    # myFont1 = font.Font(size=70)
    # myFont = font.Font(size=42)
    # window1.title("Как расставить корабли?")
    # label1 = Label(window1,font = myFont ,text="    Вам предстоить выбрать,\n как разместить корабли перед сражением:")
    # solo_button = Button(window1,text = "Самостоятельно",font = myFont,bg='#0052cc', fg='#ffffff',command = placing )
    # random_button = Button(window1,text = "Довериться воле случая",font = myFont,bg='#0052cc', fg='#ffffff',command = randomUserGrid )
    # solo_button.place(x=65, y=50)
    # random_button.place(x=350, y=50)
    # label1.place(x=50, y=20)
    window1.mainloop()


window = Tk()
# label = Label(text="adasdas")

myFont = font.Font(family='Helvetica', size=36, weight='bold')

butt = Button(text="Начать играть", font=myFont, command=prepare_to_place, bg='#0052cc', fg='#ffffff')
rules_butt = Button(text="Правила игры", font=myFont, command=start_rules, bg='#0052cc', fg='#ffffff')
center_window(600, 400, window)
butt.place(x=100, y=25)
rules_butt.place(x=100, y=175)
# label.place(x=75, y=800)
window.configure()
window.title("Морской бой")
window.mainloop()
