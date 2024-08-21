import pygame

import sys

pygame.init()

pygame.display.set_caption('ninja game')

screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock() 

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
      

  pygame.display.update()
  # Forces game to run at 60fps
  # Effectively just a dynamic sleep, sleeps for however long it needs to to run at 60fps
  clock.tick(60)