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

# I butchered this for dialog: https://www.reddit.com/r/pygame/comments/9w3ymp/how_to_add_dialogue_to_npcs/
def dialogue(char,text):
    charpos = 0
    icon = char.get_speech_icon()
    icon = pygame.transform.scale(icon, (scalesize*2,scalesize*2))
    #font = 'freesansbold.ttf'
    font = 'EightBitDragon-anqx.ttf'
    font = pygame.font.Font(font,20)
    blackBarRectPos = (128,display_height-128)
    blackBarRectSize = (display_width-128,128)
    pygame.draw.rect(gameDisplay,(0,0,0),pygame.Rect(blackBarRectPos,blackBarRectSize))
    pygame.draw.rect(gameDisplay,char.get_colour(),pygame.Rect((0,display_height-128),(128,128)))
    gameDisplay.blit(icon,(0,display_height-128))
    char_pos = 0
    text2 = text[0:char_pos]
    textSurf = font.render(char.get_name(),1,(44,191,245),(0,0,0))
    gameDisplay.blit(textSurf,(150,display_height-115))
    while char_pos <= len(text):
         text2 = text[0:char_pos]
         textSurf = font.render(text2,1,(255,255,255),(0,0,0))
         gameDisplay.blit(textSurf,(170,display_height-80))
         pygame.display.update()
         char_pos = char_pos + 1
         pygame.time.wait(50)
    pygame.time.wait(1000)


def intro():

   gameExit = False
   frame_counter = 0

   phase = 0
   summoning = 0
   summoned  = False

   spritesheet = SpriteSheet('tiles/sheet.png')
   ground1 = spritesheet.image_at( (0,0,ts,ts) )
   ground2 = spritesheet.image_at( (ts,0,ts,ts) )
   ground3 = spritesheet.image_at( (ts*2,0,ts,ts) )
   fence   = spritesheet.image_at( (0,ts*22,ts,ts), -1 )
   path1   = spritesheet.image_at( (ts*5,0,ts,ts) )
   tree2   = spritesheet.image_at( (ts*2,ts,ts*2,ts*2),-1 )
   log     = spritesheet.image_at( (ts*6,ts*5,ts*2,ts),-1 )
   skull   = spritesheet.image_at( (ts*6,ts*131,ts,ts),-1 )
   statue  = spritesheet.image_at( (ts*4,ts*113,ts,ts*2),-1 )
   heart   = pygame.image.load('tiles/heart.png')

   cat1 = Character('cat2', -100, 20)
   cat2 = Character('cat2', 900, 40)
   cat3 = Character('cat3', -100, 60)
   morgan = Character('morgan', -64, 50)
   zander = Character('zander', -64, 100)
   ghost  = Character('ghost', -120, 100)
   alex   = Character('alex', 575, 250)
   geoff = Character('geoff', 450, -80)
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
   statue  = pygame.transform.scale(statue, (scalesize,scalesize*2))

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
      ( "  ", "  ", "  ", "  ", "F1", "  ", "  ", "  ", "  ", "S1", "  ", "  ", "  " ),
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
            if map_x == 'S1':
               if not summoned:
                  statue_x = loc_x
                  statue_y = loc_y
                  if summoning > 0:
                     summoning = summoning + 1
                     statue_x = statue_x + random.randint(-5,5)
                     statue_y = statue_y + random.randint(-5,5)
                     if summoning > 80:
                        # ugh python - ??
                        dim = statue.get_size()
                        lst = list(dim)
                        lst[0] = lst[0] + 100;
                        lst[1] = lst[1] + 100;
                        dim = tuple(lst)
                        statue_x = statue_x - 50 * (summoning-80)
                        statue_y = statue_y - 50 * (summoning-80)
                        statue  = pygame.transform.scale(statue, dim)
                     if summoning > 100:
                        summoned = True
                  gameDisplay.blit(statue,(statue_x,statue_y))
            loc_x = loc_x + scalesize
         loc_y = loc_y + scalesize
         loc_x = 0;


      gameDisplay.blit(morgan.get_image(), morgan.get_location())
      gameDisplay.blit(martin.get_image(), martin.get_location())
      gameDisplay.blit(zander.get_image(), zander.get_location())
      gameDisplay.blit(ghost.get_image(), ghost.get_location())
      gameDisplay.blit(geoff.get_image(), geoff.get_location())
      if summoned:
         gameDisplay.blit(alex.get_image(), alex.get_location())
      gameDisplay.blit(cat1.get_image(), cat1.get_location())
      gameDisplay.blit(cat2.get_image(), cat2.get_location())
      gameDisplay.blit(cat3.get_image(), cat3.get_location())

      # This is the non-interactive .. thing. Each phase is an 'act' of the animation.
      # I'm sure there are better ways of doing this.. this is what I came up with,
      # while drinking a cup of tea.

      # Morgan walks in to the right
      if phase == 0:
         t1 = cat1.move_right(900)
         t2 = cat2.move_left(-100)
         t3 = cat3.move_right(900)
         if t1 and t2 and t3:
            print('done cats')
            phase = 1 

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
         dialogue(morgan,'Hello everybody!')
         phase = 6

      if phase == 6:
         dialogue(martin,'We have brought you here today for some news...')
         phase = 7

      if phase == 7:
         dialogue(martin,'BUT FIRST!')
         phase = 8

      if phase == 8:
         dialogue(morgan,'ZANDER!!!')
         phase = 9

      if phase == 9:
         t1 = zander.move_right(900)
         t2 = ghost.move_right(890)
         if t1 and t2:
            phase = 10

      if phase == 10:
         dialogue(martin,'ZANDER!!!!!!')
         phase = 11 

      if phase == 11:
         if zander.move_left(340):
            phase = 12

      if phase == 12:
         if zander.move_down(270):
            phase = 13

      # Add some frames between z arriving and speaking.
      if phase == 13:
         frame_counter = frame_counter + 1
         if frame_counter > 10:
            frame_counter = 0
            phase = 14

      if phase == 14:
         dialogue(zander,'???')
         phase = 15

      if phase == 15:
         dialogue(martin,'GEOFFFFFF!!!!!!')
         phase = 16 

      if phase == 16:
         if geoff.move_down(270):
            phase = 17

      if phase == 17:
         frame_counter = frame_counter + 1
         if frame_counter > 10:
            frame_counter = 0
            phase = 18

      if phase == 18:
         dialogue(geoff,'** Minecraft ** Mario ** Beano **')
         phase = 19

      if phase == 19:
         dialogue(martin,'We\'re missing one...')
         phase = 20

      if phase == 20:
         dialogue(morgan,'>> SUMMON ALEX <<')
         phase = 21 

      if phase == 21:
         if summoning == 0:
            summoning = 1
         if summoned:
            phase = 22

      if phase == 22:
         frame_counter = frame_counter + 1
         if frame_counter > 10:
            frame_counter = 0
            phase = 23

      if phase == 23:
         dialogue(alex,'HAIL ALEX!')
         phase = 24 

      #cat1 = Character('cat1', -100, 20)
      #cat2 = Character('cat2', 900, 40)
      #cat3 = Character('cat3', -100, 60)

      pygame.display.update()
      clock.tick(60)

intro()
pygame.quit()
quit()
