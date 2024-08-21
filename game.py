import pygame

import sys

class Game:
   def __init__(self):

      pygame.init()

      pygame.display.set_caption('ninja game')

      self.screen = pygame.display.set_mode((640, 480))

      self.clock = pygame.time.Clock()

      self.img = pygame.image.load('data/images/clouds/cloud_1.png')
      # Sets on specific color in image to be transparent 
      self.img.set_colorkey((0, 0, 0))

      self.img_pos = [160, 260]
      self.movement = [False, False]

   def run(self):
      while True:
         self.screen.fill((14, 219, 248))
         # Adds 1, -1 or 0 based on what the expression returns
         # Booleans are converted to integers
         self.img_pos[1] += (self.movement[1] - self.movement[0]) *5
         self.screen.blit(self.img, self.img_pos)
         


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
         # Forces game to run at 60fps
         # Effectively just a dynamic sleep, sleeps for however long it needs to to run at 60fps
         self.clock.tick(60)


Game().run()