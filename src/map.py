import pygame
import pytmx

class Map:
    def __init__(self, file):
        self.src_file = file
        self.gameMap = pytmx.load_pygame(self.src_file)

    def draw(self, screen):
        for i in range(self.gameMap.width):
            for j in range(self.gameMap.height):
                image = self.gameMap.get_tile_image(i, j, 0)
                screen.blit(image, (self.gameMap.tilewidth*i, self.gameMap.tileheight*j))