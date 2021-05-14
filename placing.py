import operator
from tkinter import *
from tkinter import messagebox, font
import pygame

# window = Tk()
# window.geometry("800x600")
# window.title("Разместите свои корабли")
#
#
# window.mainloop()
WIDTH = 55
HEIGHT = 55
GREEN = (0, 255, 0)

class ShipASAS(pygame.sprite.Sprite):
    def __init__(self,height,width,n,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.h = height
        self.w = width
        self.n = n
        self.x=x
        self.y=y
        self.image = pygame.Surface(((height+5)*n,width))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def rotate(self):
        self.image = pygame.transform.rotate(self.image,90)
        self.rect = self.image.get_rect(center = (self.x,self.y))


# all_sprites = pygame.sprite.Group()
# ship1 = ShipASAS(HEIGHT,WIDTH,3)
# all_sprites.add(ship1)





pygame.init()

WHITE = (255, 255, 255)

RED = (255, 0, 0)

WINDOW_SIZE = [1500, 800]
screen_person = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("battleship war")

running = True
rectangle_draging = False




# This sets the margin between each cell
MARGIN = 5


rectangle = pygame.rect.Rect(300, 000, WIDTH,HEIGHT)
ship1 = ShipASAS(HEIGHT,WIDTH,4,900,200)
ship2 = ShipASAS(HEIGHT,WIDTH,3,900,300)
ship3 = ShipASAS(HEIGHT,WIDTH,3,900,400)
ship4 = ShipASAS(HEIGHT,WIDTH,2,900,500)
ship5 = ShipASAS(HEIGHT,WIDTH,1,900,600)
ship6 = ShipASAS(HEIGHT,WIDTH,1,900,600)

# rectangle2 = pygame.rect.Rect(176, 164, 30, 30)
# rectangle3 = pygame.rect.Rect(176, 194, 30, 30)
ship_sprites = pygame.sprite.Group()
ship_sprites.add(ship1,ship2,ship3,ship4,ship5)
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
    ship1.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                for ship in ship_sprites:
                    if ship.rect.collidepoint(event.pos):
                        rectangle_draging = True
                        mouse_x, mouse_y = event.pos
                        mouse_event = tuple(i * (-1) for i in event.pos)
                        offset = tuple(map(operator.add,ship.rect.center ,mouse_event))
                            # offset_x = rectangle.x - mouse_x
                            # offset_y = rectangle.y - mouse_y
                        curr_ship = ship

            else:
                ship1.update()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                rectangle_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                mouse_x, mouse_y = event.pos
                    # ship1.rect.center = (mouse_x,mouse_y) + offset
                curr_ship.rect.center = tuple(map(operator.add,event.pos, offset))
                    # rectangle.x = mouse_x + offset_x
                    # rectangle.y = mouse_y + offset_y
                # - draws (without updates) -
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ship1.rotate()

    screen_person.fill(WHITE)

    for row in range(10):
        for column in range(10):
            color = RED
            pygame.draw.rect(screen_person,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN + 100,
                              (MARGIN + HEIGHT) * row + MARGIN + 100,
                              WIDTH,
                              HEIGHT])

    pygame.draw.rect(screen_person, GREEN, rectangle)
    for ship in ship_sprites:
        screen_person.blit(ship.image,ship.rect)
    # screen_person.blit(ship2.image,ship2.rect)
    # screen_person.blit(ship3.image,ship3.rect)
    # screen_person.blit(ship4.image,ship4.rect)
    # screen_person.blit(ship5.image,ship5.rect)
    pygame.display.flip()






pygame.display.flip()
pygame.quit()