import pygame

class Player():
    def __init__(self):
        self.direction = "N"
        self.surf = pygame.Surface((64,64))
        self.pos = pygame.math.Vector2(0,0)
        self.keymap = pygame.key.get_pressed()
        self.pos_on_window = pygame.math.Vector2((64 * 4.5),(64 * 2.5))

    def draw(self):
        self.surf.fill((255,0,0))

        return self.surf
    
    def update(self):
        self.pos_on_window = ((64 * 5),(64 * 3))
        self.keymap = pygame.key.get_pressed()

        if self.keymap[pygame.K_UP] or self.keymap[pygame.K_w]:
            if self.pos.y != 0:
                self.pos += pygame.math.Vector2(0,1) * 16

            print(self.pos)

        if self.keymap[pygame.K_DOWN] or self.keymap[pygame.K_s]:
            if self.pos.y != 64 * -49:
                self.pos += pygame.math.Vector2(0,-1) * 16
            print(self.pos)

        if self.keymap[pygame.K_RIGHT] or self.keymap[pygame.K_d]:
            if self.pos.x != 64 * -49:
                self.pos += pygame.math.Vector2(-1,0) * 16
            print(self.pos)

        if self.keymap[pygame.K_LEFT] or self.keymap[pygame.K_a]:
            if self.pos.x != 0:
                self.pos += pygame.math.Vector2(1,0) * 16
            print(self.pos)
