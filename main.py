import pygame
import sys
import os
import data.engine as e

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0) #     set position of the window to right corner of the screen
pygame.init()

w = 800
h = 600
window = pygame.display.set_mode((w, h), pygame.RESIZABLE)

e.load_animations("data/graphics/")
player = e.entity(0, 0, 16, 16, "player")
player.set_action("idle")
player.scale_size(10)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((e.w, e.h), pygame.RESIZABLE)

    player.display(window, [0, 0])
    w, h = window.get_size()
    pygame.display.update()
    pygame.display.set_caption(str(w) + "x" + str(h))