import random

class Cloud:
     # Initialize cloud with position, image, speed, and depth
     def __init__(self, pos, img, speed, depth):
          self.pos = list(pos)
          self.img = img
          self.speed = speed
          self.depth = depth

     # Move cloud based on its speed
     def update(self):
          self.pos[0]  += self.speed

     def render(self, surf, offset=(0, 0)):
          """
          Renders the cloud on the given surface with an optional offset.
          Args:
               surf (pygame.Surface): The surface to render the cloud on.
               offset (tuple, optional): A tuple representing the x and y offset for rendering. Defaults to (0, 0).
          """
          # Calculate the position to render the cloud, adjusting for the offset and depth
          render_pos = (self.pos[0] - offset[0] * self.depth, self.pos[1] - offset[1] * self.depth)
          # Have a set of clouds that loop around the screen
          # Add size of image to prevent looping at the edge of the screen (adds extra width)
          surf.blit(self.img, (render_pos[0] % (surf.get_width() + self.img.get_width()) - self.img.get_width(), render_pos[1] % (surf.get_height() + self.img.get_height()) - self.img.get_height()))

# Clouds class to manage and create multiple clouds
class Clouds:
     def __init__(self, cloud_images, count=16):
          self.clouds = []

          for i in range(count):
               self.clouds.append(Cloud((random.random() * 9999, random.random() * 9999), random.choice(cloud_images), random.random() * 0.05 + 0.05, random.random() * 0.6 + 0.2))
          
          # Sort clouds based on depth (clouds closer to the screen are rendered first)
          self.clouds.sort(key=lambda cloud: cloud.depth)

     def update(self):
          for cloud in self.clouds:
               cloud.update()
     
     def render(self, surf, offset=(0, 0)):
          for cloud in self.clouds:
               cloud.render(surf, offset=offset)