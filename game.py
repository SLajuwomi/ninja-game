import pygame

import sys

from scripts.utils import load_image
from scripts.entities import PhysicsEntity

class Game:
   def __init__(self):

      pygame.init()

      pygame.display.set_caption('ninja game')

      self.screen = pygame.display.set_mode((640, 480))
      # Surface generates a black image at specifed dimension
      self.display = pygame.Surface((320, 240))

      self.clock = pygame.time.Clock()

      self.movement = [False, False]

      self.assets = {
         'player': load_image('entities/player.png')
      }

      #                                            Pos       Size                             
      self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

   def run(self):
      while True:
         self.screen.fill((14, 219, 248))


         self.player.update((self.movement[1] - self.movement[0], 0))
         self.player.render(self.screen)
         


         """  
         Only works with arrow keys, because some keyboard layouts don't have WASD or are formatted differently

         One can support both by adding the K_w ... events as well as K_UP...
         """
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
               

         pygame.display.update()
         # Forces game to run at 60fps
         # Effectively just a dynamic sleep, sleeps for however long it needs to to run at 60fps
         self.clock.tick(60)


Game().run()