import pygame
import random

class Land():
    def __init__(self):
        self.surf = pygame.surface.Surface(((64 * 50),(64 * 50)))
        self.tile = pygame.rect.Rect(0, 0, 64, 64)

        for i in range(50):
            for j in range(50):
                self.tile = pygame.rect.Rect(i*64, j*64, 64, 64)
                pygame.draw.rect(self.surf, (random.randint(0,50),random.randint(200,255),random.randint(0,50)), self.tile)

    def draw(self):
        return self.surf