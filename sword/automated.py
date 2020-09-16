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

def dialogue(char,text): 
    icon = char.get_speech_icon()
    icon = pygame.transform.scale(icon, (scalesize*2,scalesize*2))
    gameDisplay.blit(icon,(0,display_height-128)) #paste the 64x64 image onto the bottom left of the screen
    font = 'freesansbold.ttf'
    font = pygame.font.Font(font,30)
    blackBarRectPos = (128,display_height-128)  #position of the black bar at the bottom of the screen, to the right of the icon
    blackBarRectSize = (display_width-128,128)  #size of the black bar
    pygame.draw.rect(gameDisplay,(0,0,0),pygame.Rect(blackBarRectPos,blackBarRectSize)) #draw the black bar onto the screen
    textSurf = font.render(text,1,(255,255,255),(0,0,0))  #render the text (replace fontObject with whatever you called the font you're using for ingame text)
    gameDisplay.blit(textSurf,(140,display_height-99))  #put it onto the screen


def intro():

   gameExit = False
   frame_counter = 0

   phase = 1

   spritesheet = SpriteSheet('tiles/sheet.png')
   ground1 = spritesheet.image_at( (0,0,ts,ts) )
   ground2 = spritesheet.image_at( (ts,0,ts,ts) )
   ground3 = spritesheet.image_at( (ts*2,0,ts,ts) )
   fence   = spritesheet.image_at( (0,ts*22,ts,ts), -1 )
   path1   = spritesheet.image_at( (ts*5,0,ts,ts) )
   tree2   = spritesheet.image_at( (ts*2,ts,ts*2,ts*2),-1 )
   log     = spritesheet.image_at( (ts*6,ts*5,ts*2,ts),-1 )
   skull   = spritesheet.image_at( (ts*6,ts*131,ts,ts),-1 )
   heart   = pygame.image.load('tiles/heart.png')

   morgan = Character('morgan', -20, 50)
   martin = Character('martin', 800+64+20, 50)

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

      # This is the non-interactive .. thing. Each phase is an 'act' of the animation.
      # I'm sure there are better ways of doing this.. this is what I came up with,
      # while drinking a cup of tea.

      # Morgan walks in to the right
      if phase == 1:
         if morgan.move_right(360):
            phase = 2

      # Martin walks in from the left
      if phase == 2:
         if martin.move_left(420):
            phase = 3

      # A heart appears above us for a few frames
      if phase == 3:
         frame_counter = frame_counter + 1
         if frame_counter < 50:
            gameDisplay.blit(heart, (406, 30))
         else:
            frame_counter = 0
            phase = 4

      # We walk down together
      if phase == 4:
         t1 = morgan.move_down(350)
         t2 = martin.move_down(350)
         if t1 and t2:
            phase = 5

      # A speech bubble of some sort
      if phase == 5:
         frame_counter = frame_counter + 1
         if frame_counter < 260:
            dialogue(morgan,'Hello everybody!')
         else:
            frame_counter = 0
            phase = 6

      gameDisplay.blit(morgan.get_image(), morgan.get_location())
      gameDisplay.blit(martin.get_image(), martin.get_location())

      pygame.display.update()
      clock.tick(60)

intro()
pygame.quit()
quit()
