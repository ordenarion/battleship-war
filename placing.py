import operator
from tkinter import *
from tkinter import messagebox, font
import pygame


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
SHIPCOL = (106,90,205)

def points(x):
  res=[]
  for curr in x:
    if curr[0]==curr[1] and curr[2]==curr[3]:
      res.append([curr[0],curr[2],1])

    elif curr[0] == curr[1] and curr[2]!=curr[3]:
      min_coord = min(curr[2],curr[3])
      max_coord = max(curr[2],curr[3])

      m=[[curr[0],i,1] for i in range(min_coord,max_coord+1)]
      res.append(m)

    elif curr[0] != curr[1] and curr[2]==curr[3]:
      min_coord = min(curr[0],curr[1])
      max_coord = max(curr[0],curr[1])

      m=[[i,curr[2],1] for i in range(min_coord,max_coord+1)]
      res.append(m)

  return res

def flatten_lvl_1(x):
  k=[]
  for i in x:
    for j in i:
      if isinstance(j,list):
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
BLACK = (0,0,0)

WINDOW_SIZE = [1500, 800]
screen_person = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("battleship war")

running = True
rectangle_draging = False

# This sets the margin between each cell
MARGIN = 5
color1 = RED
rectangle = pygame.rect.Rect(1,1,100,50)
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

while running:
    # ship1.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
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
                #print(allpairs)
                pointsforships = points(allpairs)
                toCheck = flatten_lvl_1(pointsforships)
                flag2 = False

                for i in toCheck:
                    if i[0] >9 or i[1]>9 or i[0]<0 or i[1]<0:
                        flag2 = True
                        break
                if flag2:
                    finalToCheck = [1]

                else:
                    finalToCheck = set(tuple(row) for row in toCheck)
                #print(toCheck)
                print("-------------------")

                if len(finalToCheck) < len(toCheck):
                    color1 = RED
                    #pass #Ошибка, поменйте раположение
                    print(finalToCheck)
                    print(toCheck)

                elif len(finalToCheck) == len(toCheck):
                #Заполняем сетку 1 где поинты, используем инфу из toCheck
                    for point in toCheck:
                        grid_for_shot[point[0]][point[1]] = 1
                        color1 = GREEN
                    finalGrid = list(map(list,[grid_for_shot]+[pointsforships]))
                print(finalGrid)
                print(finalToCheck)
                print(toCheck)
                print(len(toCheck))
                print(len(finalToCheck))
                    #Потом объединяем сетку и pointsforships
                #print(toCheck)
                #print(grid_for_shot)


    screen_person.fill(WHITE)
    pygame.draw.rect(screen_person, color1, (10, 10, 100, 50))

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
    #pygame.draw.rect(screen_person, GREEN, rectangle)
    for ship in ship_sprites:
        screen_person.blit(ship.image, ship.rect)

    # screen_person.blit(ship2.image,ship2.rect)
    # screen_person.blit(ship3.image,ship3.rect)
    # screen_person.blit(ship4.image,ship4.rect)
    # screen_person.blit(ship5.image,ship5.rect)
    pygame.display.flip()



pygame.display.flip()
pygame.quit()
