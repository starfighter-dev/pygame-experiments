import pygame
from spritesheet import SpriteSheet

class Character:

    animation_position = 0
    animation_loop = 0
    direction = 'right'

    def __init__(self, name):
      print(name)
      spritesheet = SpriteSheet('characters/'+name+'.png')
      self.forward = [
         pygame.transform.scale(spritesheet.image_at( (0,0,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (32,0,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (64,0,32,32), -1 ), (64,64)),
      ]
      self.left = [
         pygame.transform.scale(spritesheet.image_at( (0,32,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (32,32,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (64,32,32,32), -1 ), (64,64)),
      ]
      self.right = [
         pygame.transform.scale(spritesheet.image_at( (0,64,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (32,64,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (64,64,32,32), -1 ), (64,64)),
      ]
      self.back = [
         pygame.transform.scale(spritesheet.image_at( (0,96,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (32,96,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (64,86,32,32), -1 ), (64,64)),
      ]

    def get_image(self, direction):
      self.direction = direction

      # This animation_loop thing is to slow down the changing animations...
      # we don't want to change it on every single frame.
      if self.animation_loop > 30:
         self.animation_loop = 0
         self.animation_position = self.animation_position + 1
         if self.animation_position > 2:
            self.animation_position = 0
      self.animation_loop = self.animation_loop + 1

      if self.direction == 'forward':
         return self.forward[self.animation_position]
      if self.direction == 'back':
         return self.back[self.animation_position]
      if self.direction == 'left':
         return self.left[self.animation_position]
      if self.direction == 'right':
         return self.right[self.animation_position]
