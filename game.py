import sys
import random
import pygame

resolution = (640, 480)
fps = 60

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("UtopiaLite!")
        self.window = pygame.display.set_mode(resolution)

        self.clock = pygame.time.Clock()

        self.img_pos = [160,260]
        self.movement = [False,False]
        self.base_player_image = pygame.image.load('./data/images/player/player-1.png').convert_alpha()

    def generate_player(self):
        player_image = self.base_player_image.copy()
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        player_image.fill(random_color + (0,), special_flags=pygame.BLEND_RGBA_ADD)
        
        return player_image

    def run(self):
        self.img = self.generate_player()

        while True:
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.window.blit(self.img, self.img_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(fps)

game = Game()
game.run()