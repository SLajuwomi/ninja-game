import pygame

import sys

from scripts.entities import PhysicsEntity

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
      self.movement = [False, False, False, False]

      self.collision_area = (50, 50, 300, 50)
      #                                            Pos       Size                             
      self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

   def run(self):
      while True:
         self.screen.fill((14, 219, 248))
         # Adds 1, -1 or 0 based on what the expression returns
         # Booleans are converted to integers
         self.img_pos[0] += (self.movement[2] - self.movement[3]) *5
         self.img_pos[1] += (self.movement[1] - self.movement[0]) *5
         

         # makes a rectangle that perfectly matches the cloud image
         img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())

         if img_r.colliderect(self.collision_area):
            pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
         else:
            pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)

         self.screen.blit(self.img, self.img_pos)


         """  
         Only works with arrow keys, because some keyboard layouts don't have WASD or are formatted differently

         One can support both by adding the K_w ... events as well as K_UP...
         """
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_UP:
                  self.movement[0] = True
               if event.key == pygame.K_DOWN:
                  self.movement[1] = True
               if event.key == pygame.K_LEFT:
                  self.movement[2] = True
               if event.key == pygame.K_RIGHT:
                  self.movement[3] = True
            if event.type == pygame.KEYUP:
               if event.key == pygame.K_UP:
                  self.movement[0] = False
               if event.key == pygame.K_DOWN:
                  self.movement[1] = False
               if event.key == pygame.K_LEFT:
                  self.movement[2] = False
               if event.key == pygame.K_RIGHT:
                  self.movement[3] = False
            
               

         pygame.display.update()
         # Forces game to run at 60fps
         # Effectively just a dynamic sleep, sleeps for however long it needs to to run at 60fps
         self.clock.tick(60)


Game().run()