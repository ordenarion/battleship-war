import pygame
from tkinter import *
from tkinter import messagebox


def sea_battle():
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (120, 171, 235)
    BG = (110, 131, 156)
    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 20
    HEIGHT = 20

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
    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [255, 255]
    screen_person = pygame.display.set_mode(WINDOW_SIZE)
    screen_cpu = pygame.display.set_mode(WINDOW_SIZE)
    # Set title of screen
    pygame.display.set_caption("battleship war")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        label.configure(text=None)
        hp = 3
        score = 0
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                grid[row][column] = -1
                # print("Click ", pos, "Grid coordinates: ", row, column)

        # Set the screen background
        screen_person.fill(BLACK)

        # Draw the grid
        for row in range(10):
            for column in range(10):
                color = WHITE
                if grid[row][column] == -1 and sample[row][column] != 1:
                    color = BLUE
                    score -= 1
                elif grid[row][column] == -1 and sample[row][column] == 1:
                    color = RED
                    score += 1
                    hp -= 1

                    if hp == 0:
                        # Tk().wm_withdraw()  # to hide the main window
                        # messagebox.showinfo("Конец игры", f"Поздравляю, Вы победили, ваши очки: {score}")
                        label.configure(text=f"{score}")
                        done = True
                pygame.draw.rect(screen_person,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        # Limit to 60 frames per second
        clock.tick(60)

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
    center_window(600, 900, rule)
    rule.title("Правила игры")
    rule.mainloop()


window = Tk()
window.geometry("800x600")

label = Label(text="adasdas")

butt = Button(text="Начать играть", height=5, font="1", width=50, command=sea_battle)
rules_butt = Button(text="Правила игры", height=5, font="1", width=50, command=start_rules)
center_window(600, 900, window)
butt.place(x=75, y=25)
rules_butt.place(x=75, y=175)
label.place(x=75, y=800)
window.configure()
window.title("Морской boy")
window.mainloop()
