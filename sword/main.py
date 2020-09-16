import pygame, time, random
from spritesheet import SpriteSheet
from characters import Character 

pygame.init()

display_width = 800
display_height = 600

ts = 32;
scalesize = 64;


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Sword')
clock = pygame.time.Clock()


def intro():

   gameExit = False

   spritesheet = SpriteSheet('tiles/sheet.png')
   ground1 = spritesheet.image_at( (0,0,ts,ts) )
   ground2 = spritesheet.image_at( (ts,0,ts,ts) )
   ground3 = spritesheet.image_at( (ts*2,0,ts,ts) )
   fence   = spritesheet.image_at( (0,ts*22,ts,ts), -1 )
   path1   = spritesheet.image_at( (ts*5,0,ts,ts) )
   tree2   = spritesheet.image_at( (ts*2,ts,ts*2,ts*2),-1 )
   log     = spritesheet.image_at( (ts*6,ts*5,ts*2,ts),-1 )
   skull   = spritesheet.image_at( (ts*6,ts*131,ts,ts),-1 )

   morgan = Character('morgan', 20, 20)

   # scale things..
   ground1 = pygame.transform.scale(ground1, (scalesize,scalesize))
   ground2 = pygame.transform.scale(ground2, (scalesize,scalesize))
   ground3 = pygame.transform.scale(ground3, (scalesize,scalesize))
   path1   = pygame.transform.scale(path1, (scalesize,scalesize))
   tree2   = pygame.transform.scale(tree2, (scalesize*2,scalesize*2))
   fence   = pygame.transform.scale(fence, (scalesize,scalesize))
   log     = pygame.transform.scale(log, (scalesize*2,scalesize))
   skull   = pygame.transform.scale(skull, (scalesize,scalesize))

   background = (
      ( "G2", "G2", "G2", "G2", "G2", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "G2", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "G2", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "G2", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "G2", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "G2", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "G2", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "G2", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "G2", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "G2", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
   )

   foreground = (
      ( "  ", "  ", "  ", "  ", "F1", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  " ),
      ( "  ", "T2", "  ", "  ", "F1", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  " ),
      ( "  ", "  ", "T2", "  ", "F1", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  " ),
      ( "  ", "  ", "  ", "  ", "F1", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  " ),
      ( "  ", "  ", "T2", "  ", "F1", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  " ),
      ( "  ", "  ", "  ", "  ", "F1", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  " ),
      ( "  ", "  ", "  ", "  ", "F1", "  ", "  ", "  ", "  ", "L1", "  ", "  ", "  " ),
      ( "  ", "  ", "T2", "  ", "F1", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  " ),
      ( "T2", "  ", "  ", "  ", "F1", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  " ),
      ( "  ", "  ", "  ", "  ", "F1", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  " ),
   )

   drawn = 0;

   is_shaking = 0

   while not gameExit:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            quit()

         #debug
         #print(event)

      if not drawn:
         loc_x = 0;
         loc_y = 0;
         for map_y in background:
            for map_x in map_y:
               if map_x == 'G1':
                  gameDisplay.blit(ground1,(loc_x,loc_y))
               if map_x == 'G2':
                  gameDisplay.blit(ground2,(loc_x,loc_y))
               if map_x == 'G3':
                  gameDisplay.blit(ground3,(loc_x,loc_y))
               if map_x == 'P1':
                  gameDisplay.blit(path1,(loc_x,loc_y))
               loc_x = loc_x + scalesize
            loc_y = loc_y + scalesize
            loc_x = 0;

         loc_x = 0;
         loc_y = 0;
         for map_y in foreground:
            for map_x in map_y:
               if map_x == 'T2':
                  gameDisplay.blit(tree2,(loc_x,loc_y))
               if map_x == 'F1':
                  gameDisplay.blit(fence,(loc_x,loc_y))
               if map_x == 'L1':
                  gameDisplay.blit(log,(loc_x,loc_y))
               loc_x = loc_x + scalesize
            loc_y = loc_y + scalesize
            loc_x = 0;
      drawn = 0 #force redraw, or not

      key_input = pygame.key.get_pressed()
      if not is_shaking:
         if key_input[pygame.K_LEFT]:
            morgan.move_left()
         if key_input[pygame.K_UP]:
            morgan.move_up()
         if key_input[pygame.K_RIGHT]:
            morgan.move_right()
         if key_input[pygame.K_DOWN]:
            morgan.move_down()

      gameDisplay.blit(morgan.get_image(), morgan.get_location())

      pygame.display.update()
      clock.tick(60)

intro()
pygame.quit()
quit()
