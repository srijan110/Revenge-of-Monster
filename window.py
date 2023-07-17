import pygame
#import ui
import cam


class Game():
    def __init__(self):
        pygame.init()

        self.win_height = 64 * 7
        self.win_width = 64 * 11

        self.fill_color = pygame.color.Color(255,255,255)

        self.window = pygame.display.set_mode((self.win_width, self.win_height))
        self.clock = pygame.time.Clock()

        self.cam = cam.Camera()

        self.touch = pygame.math.Vector2(0,0)

    def update(self):
        self.mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
        self.cam.update()
        self.clock.tick(24)
 
    def draw(self):
        self.window.fill(self.fill_color)
        self.window.blit(self.cam.draw(), (0,0))

        pygame.display.flip()

    def game_loop(self):
        self.running = True

        while self.running:
            self.update()
            self.draw()
            self.event()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.quit()
                self.running = False

    def quit(self):
        pygame.quit()

    def init(self):
        self.game_loop()

if __name__ == "__main__":
    game = Game()
    game.init()