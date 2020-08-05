import pygame
import random
from good_side.good_side import GoodSide
from good_side.good import Good

pygame.init()

FPS = 60
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


font = pygame.font.Font(None, 30)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

goods = GoodSide()

goods.good_arr.append(Good())

goods.good_arr.append(Good(200, 450))

running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    goods.update(screen)
    fps = font.render(str(int(clock.get_fps())), True, pygame.Color('gray'))
    screen.blit(fps, (50, 50))
    pygame.display.update()
    
pygame.quit()