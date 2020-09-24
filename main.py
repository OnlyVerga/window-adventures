import pygame
import sys
import os
import data.engine as e

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0) #     set position of the window to right corner of the screen
pygame.init()

level_width = 64
level_height = 36

screen_res = [e.Monitor.current_w, e.Monitor.current_h]
scaling = int((screen_res[0] / level_width) / 16)
w = 800
h = 600
window = pygame.display.set_mode((w, h), pygame.RESIZABLE)

gravity = 0

e.load_animations("data/graphics/")
player = e.entity(0, 0, 16, 16, "player")
player.scale_size(scaling)
moving_left = False
moving_right = False

while True:
    window.fill(e.purple)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False

        #       moving player
        player_movement = [0, 0]
        if moving_right == True:
            player_movement[0] += 2
        if moving_left == True:
            player_movement[0] -= 2
        player_movement[1] += gravity
        gravity += 0.3
        if gravity > 3:
           gravity = 3

    player.move(player_movement, [])
    player.display(window, [0, 0])
    player.change_frame(1)
    w, h = window.get_size()
    pygame.display.update()
    pygame.display.set_caption(str(w) + "x" + str(h))