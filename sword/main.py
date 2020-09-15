import pygame, time
from spritesheet import SpriteSheet

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

   map1 = (
      ( "G2", "G2", "G2", "G2", "F1", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "F1", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "F1", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "F1", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "F1", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "F1", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "F1", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "F1", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "F1", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "F1", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
   )

   ground1 = pygame.transform.scale(ground1, (scalesize,scalesize))
   ground2 = pygame.transform.scale(ground2, (scalesize,scalesize))
   ground3 = pygame.transform.scale(ground3, (scalesize,scalesize))
   path1   = pygame.transform.scale(path1, (scalesize,scalesize))
   tree2   = pygame.transform.scale(tree2, (scalesize*2,scalesize*2))
   fence   = pygame.transform.scale(fence, (scalesize,scalesize))

   while not gameExit:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            quit()

         #debug
         #print(event)

      loc_x = 0;
      loc_y = 0;
      for map_y in map1:
         for map_x in map_y:
            if map_x == 'G1':
               gameDisplay.blit(ground1,(loc_x,loc_y))
            if map_x == 'G2':
               gameDisplay.blit(ground2,(loc_x,loc_y))
            if map_x == 'G3':
               gameDisplay.blit(ground3,(loc_x,loc_y))
            if map_x == 'P1':
               gameDisplay.blit(path1,(loc_x,loc_y))
            if map_x == 'T2':
               gameDisplay.blit(tree2,(loc_x,loc_y))
            if map_x == 'F1':
               gameDisplay.blit(ground2,(loc_x,loc_y))
               gameDisplay.blit(fence,(loc_x,loc_y))
            loc_x = loc_x + scalesize
         loc_y = loc_y + scalesize
         loc_x = 0;

      gameDisplay.blit(tree2,(ts*3, ts*2))
      gameDisplay.blit(tree2,(ts*2, ts*8))
      gameDisplay.blit(tree2,(ts*20, ts*4))
      gameDisplay.blit(tree2,(ts*18, ts*12))

      pygame.display.update()
      clock.tick(60)

intro()
pygame.quit()
quit()
