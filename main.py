import pygame
import sys
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0) #     set position of the window to right corner of the screen


pygame.init()

window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
w = 800
h = 600

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((e.w, e.h), pygame.RESIZABLE)
            
    w, h = window.get_size()
    pygame.display.update()
    pygame.display.set_caption(str(w) + "x" + str(h))