import pygame
import land
import player
import random

class Camera():
    def __init__(self):
        self.surf = pygame.surface.Surface(((64 * 11),(64 * 7)))
        self.land = land.Land()

        self.fill_color = (random.randint(0,50),random.randint(0,50),random.randint(100,255))

        self.player = player.Player()

    def draw(self):
        self.surf.fill(self.fill_color)

        self.surf.blit(self.land.draw(), self.player.pos + self.player.pos_on_window)
        self.surf.blit(self.player.draw(), self.player.pos_on_window)

        return self.surf
    
    def update(self):
        self.player.update()