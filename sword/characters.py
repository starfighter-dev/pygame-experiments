import pygame
from spritesheet import SpriteSheet

class Character:

    animation_position = 0
    animation_loop = 0
    direction = 'right'
    x = 0
    y = 0
    step = 5
    is_moving = False
    name = ''

    def __init__(self, name, start_x, start_y):
      self.name = name
      if self.name == 'zander':
         self.step = 15
      self.x = start_x
      self.y = start_y
      spritesheet = SpriteSheet('characters/'+name+'.png')
      self.down = [
         pygame.transform.scale(spritesheet.image_at( (0,0,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (32,0,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (64,0,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (32,0,32,32), -1 ), (64,64)),
      ]
      self.left = [
         pygame.transform.scale(spritesheet.image_at( (0,32,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (32,32,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (64,32,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (32,32,32,32), -1 ), (64,64)),
      ]
      self.right = [
         pygame.transform.scale(spritesheet.image_at( (0,64,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (32,64,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (64,64,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (32,64,32,32), -1 ), (64,64)),
      ]
      self.up = [
         pygame.transform.scale(spritesheet.image_at( (0,96,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (32,96,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (64,96,32,32), -1 ), (64,64)),
         pygame.transform.scale(spritesheet.image_at( (32,96,32,32), -1 ), (64,64)),
      ]

    def get_name(self):
      return self.name

    def get_colour(self):
      val = ( 98, 67, 110 )
      if self.name == 'martin':
         val = ( 2, 99, 168 )
      return val

    def get_location(self):
      return ( self.x, self.y )

    def move_right(self, limit):
      self.x = self.x + self.step
      self.direction = 'right'
      if self.x >= limit:
         return True
      return False

    def move_left(self, limit):
      self.x = self.x - self.step
      self.direction = 'left'
      if self.x <= limit:
         return True
      return False

    def move_up(self, limit):
      self.y = self.y - self.step
      self.direction = 'up'
      if self.y <= limit:
         return True
      return False

    def move_down(self, limit):
      self.y = self.y + self.step
      self.direction = 'down'
      if self.y >= limit:
         return True
      return False

    def get_speech_icon(self):
      return self.down[0];

    def get_image(self):

      # This animation_loop thing is to slow down the changing animations...
      # we don't want to change it on every single frame.
      if self.animation_loop > 30:
         self.animation_loop = 0
         self.animation_position = self.animation_position + 1
         if self.animation_position > 3:
            self.animation_position = 0
      self.animation_loop = self.animation_loop + 1

      if self.direction == 'down':
         return self.down[self.animation_position]
      if self.direction == 'up':
         return self.up[self.animation_position]
      if self.direction == 'left':
         return self.left[self.animation_position]
      if self.direction == 'right':
         return self.right[self.animation_position]
