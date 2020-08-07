import pygame
import random
from good_side.good_side import GoodSide
from good_side.good import Good

from bad_side.bad_side import BadSide
from bad_side.bad import Bad

import pytmx

pygame.init()

FPS = 60
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640


font = pygame.font.Font(None, 30)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

goods = GoodSide()

goods.good_arr.append(Good())

goods.good_arr.append(Good(200, 450))

bads = BadSide()

bads.bad_arr.append(Bad(500, 400))

bads.bad_arr.append(Bad(100, 280))

gameMap = pytmx.load_pygame('./map/map_2.tmx')
width_gameMap = gameMap.tilewidth*gameMap.width
height_gameMap = gameMap.tileheight*gameMap.height

empty_surface = pygame.Surface((width_gameMap, height_gameMap))
running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #screen.fill((190, 237, 194))
    
    for i in range(gameMap.width):
        for j in range(gameMap.height):
            image = gameMap.get_tile_image(i, j, 0)
            screen.blit(image, (gameMap.tilewidth*i, gameMap.tileheight*j))

    goods.update(screen)
    bads.update(screen, goods.good_arr)
    fps = font.render(str(int(clock.get_fps())), True, pygame.Color('gray'))
    screen.blit(fps, (50, 50))
    '''for layer in gameMap.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = gameMap.get_tile_image_by_gid(gid)
                if tile:
                    empty_surface.blit(tile, (x * gameMap.tilewidth, y * gameMap.tileheight))'''
    pygame.display.update()
    
pygame.quit()