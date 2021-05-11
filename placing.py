from tkinter import *
from tkinter import messagebox, font
import pygame

# window = Tk()
# window.geometry("800x600")
# window.title("Разместите свои корабли")
#
#
# window.mainloop()
pygame.init()

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WINDOW_SIZE = [1500, 800]
screen_person = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("battleship war")

running = True
rectangle_draging = False



WIDTH = 40
HEIGHT = 40

# This sets the margin between each cell
MARGIN = 5
л

rectangle = pygame.rect.Rect(176, 134, 30, 30)
# rectangle2 = pygame.rect.Rect(176, 164, 30, 30)
# rectangle3 = pygame.rect.Rect(176, 194, 30, 30)

# s = pygame.sprite.Group()
# s.add(rectangle1)
# s.add(rectangle2)
# s.add(rectangle3)
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

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rectangle.collidepoint(event.pos):
                    rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle.x - mouse_x
                    offset_y = rectangle.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                rectangle_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                mouse_x, mouse_y = event.pos
                rectangle.x = mouse_x + offset_x
                rectangle.y = mouse_y + offset_y
            # - draws (without updates) -

    screen_person.fill(WHITE)
    pygame.draw.rect(screen_person, RED, rectangle)
    pygame.display.flip()




pygame.display.flip()
pygame.quit()