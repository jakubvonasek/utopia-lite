import sys
import random
import pygame

resolution = (640, 480)
fps = 60

from src.utils import load_image
from src.utils import load_images
from src.entities import PhysicsEntity
from src.tilemap import Tilemap


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("UtopiaLite!")
        self.window = pygame.display.set_mode(resolution)
        self.surface = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.movement = [False,False]
        
        self.assets = {
            # 'decor' : load_images('tiles/decor'),
            'grass' : load_images('tiles/grass'),
            # 'large_decor' : load_images('tiles/large_decor'),
            'stone' : load_images('tiles/stone'),
            'player': load_image('entities/player/player.png')
        }

        print(self.assets)

        self.player = PhysicsEntity(self, 'player', (50,50), (32,32))

        self.tilemap = Tilemap(self, tilesize=16)

    def run(self):

        while True:
            self.surface.fill((14, 219, 248))

            self.tilemap.render(self.surface)

            self.player.update((self.movement[1] - self.movement[0],0))
            self.player.render(self.surface)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False


            self.window.blit(pygame.transform.scale(self.surface,self.window.get_size()))
            pygame.display.update()
            self.clock.tick(fps)


game = Game()
game.run()