# An animation. I'm not really sure the best way to do simple animations in
# pygame, so this is my first attempt. I also haven't touched Python in quite
# some time, so please exuse some of the code that follows.
#
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

def fadeout():
    fadeout = pygame.Surface((display_width, display_height))
    fadeout = fadeout.convert()
    fadeout.fill((0,0,0))
    for i in range(255):
        fadeout.set_alpha(i)
        gameDisplay.blit(fadeout, (0, 0))
        pygame.display.update()

def dialogue_all(name,image,text):
    charpos = 0
    icon = pygame.transform.scale(image, (scalesize*2,scalesize*2))
    #font = 'freesansbold.ttf'
    font = 'EightBitDragon-anqx.ttf'
    font = pygame.font.Font(font,20)
    blackBarRectPos = (128,display_height-128)
    blackBarRectSize = (display_width-128,128)
    pygame.draw.rect(gameDisplay,(0,0,0),pygame.Rect(blackBarRectPos,blackBarRectSize))
    pygame.draw.rect(gameDisplay,(255,0,0),pygame.Rect((0,display_height-128),(128,128)))
    gameDisplay.blit(icon,(0,display_height-128))
    char_pos = 0
    text2 = text[0:char_pos]
    textSurf = font.render(name,1,(44,191,245),(0,0,0))
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

   chest = 'closed'
   show_key = False
   show_bear = False
   show_cake = False
   done_hoot = False
   did_fade = False
   cake_x = 290
   cake_y = 5

   hoot_sound = pygame.mixer.Sound("sound/hoot.wav")
   ufo_sound = pygame.mixer.Sound("sound/ufo.wav")
   pop_sound = pygame.mixer.Sound("sound/pop.wav")
   open_sound = pygame.mixer.Sound("sound/unlock.wav")
   pygame.mixer.init()
   pygame.mixer.music.load('sound/lullaby.wav')

   scan = pygame.image.load('pictures/scan.jpg')
   spritesheet = SpriteSheet('tiles/sheet.png')
   pumpkin = spritesheet.image_at( (ts*6,ts*20,ts,ts), -1 )
   seedling = spritesheet.image_at( (ts*7,ts*19,ts,ts), -1 )
   stone1 = spritesheet.image_at( (ts*1,ts*57,ts,ts) )
   stone2 = spritesheet.image_at( (ts*2,ts*57,ts,ts) )
   stone3 = spritesheet.image_at( (0,ts*57,ts,ts) )
   ground1 = spritesheet.image_at( (0,0,ts,ts) )
   ground2 = spritesheet.image_at( (ts,0,ts,ts) )
   ground3 = spritesheet.image_at( (ts*2,0,ts,ts) )
   fence   = spritesheet.image_at( (0,ts*22,ts,ts), -1 )
   path1   = spritesheet.image_at( (ts*5,0,ts,ts) )
   tree2   = spritesheet.image_at( (ts*2,ts,ts*2,ts*2),-1 )
   log     = spritesheet.image_at( (ts*6,ts*5,ts*2,ts),-1 )
   skull   = spritesheet.image_at( (ts*6,ts*131,ts,ts),-1 )
   fountain = spritesheet.image_at( (0,ts*116,ts*3,ts*3),-1 )
   statue  = spritesheet.image_at( (ts*4,ts*113,ts,ts*2),-1 )
   statue2 = spritesheet.image_at( (ts*3,ts*115,ts,ts*2),-1 )
   statue3 = spritesheet.image_at( (ts*4,ts*115,ts,ts*2),-1 )
   grave   = spritesheet.image_at( (ts*3,ts*8,ts,ts),-1 )
   key     = spritesheet.image_at( (ts*7,ts*131,ts,ts),-1 )
   bear    = spritesheet.image_at( (ts*3,ts*128,ts,ts),-1 )
   heart   = pygame.image.load('tiles/heart.png')

   cake_hover = pygame.image.load('tiles/cake.png')
   cake_hover.set_colorkey(cake_hover.get_at((0,0)), pygame.RLEACCEL)
   cake_hover = pygame.transform.scale(cake_hover, (scalesize*4,scalesize*4))

   cat1 = Character('cat2', -100, 20)
   cat2 = Character('cat2', 900, 40)
   cat3 = Character('cat3', -100, 60)
   morgan = Character('morgan', -64, 50)
   zander = Character('zander', -64, 70)
   ghost  = Character('ghost', -120, 70)
   ace   = Character('alex', 575, 188)
   geoff = Character('geoff', 450, -80)
   martin = Character('martin', 800+64+20, 50)

   chest_closed = spritesheet.image_at( (ts*6,ts*107,ts,ts),-1 )
   chest_open   = spritesheet.image_at( (ts*6,ts*108,ts,ts),-1 )

   # scale things..
   chest_closed = pygame.transform.scale(chest_closed, (scalesize,scalesize))
   chest_open   = pygame.transform.scale(chest_open, (scalesize,scalesize))
   pumpkin = pygame.transform.scale(pumpkin, (scalesize,scalesize))
   seedling = pygame.transform.scale(seedling, (scalesize,scalesize))
   ground1 = pygame.transform.scale(ground1, (scalesize,scalesize))
   ground2 = pygame.transform.scale(ground2, (scalesize,scalesize))
   ground3 = pygame.transform.scale(ground3, (scalesize,scalesize))
   grave = pygame.transform.scale(grave, (scalesize,scalesize))
   key = pygame.transform.scale(key, (scalesize,scalesize))
   bear = pygame.transform.scale(bear, (scalesize*2,scalesize*2))
   stone1  = pygame.transform.scale(stone1, (scalesize,scalesize))
   stone2  = pygame.transform.scale(stone2, (scalesize,scalesize))
   stone3  = pygame.transform.scale(stone3, (scalesize,scalesize))
   path1   = pygame.transform.scale(path1, (scalesize,scalesize))
   tree2   = pygame.transform.scale(tree2, (scalesize*2,scalesize*2))
   fence   = pygame.transform.scale(fence, (scalesize,scalesize))
   log     = pygame.transform.scale(log, (scalesize*2,scalesize))
   skull   = pygame.transform.scale(skull, (scalesize,scalesize))
   statue  = pygame.transform.scale(statue, (scalesize,scalesize*2))
   fountain = pygame.transform.scale(fountain, (scalesize*3,scalesize*3))
   statue2 = pygame.transform.scale(statue2, (scalesize,scalesize*2))
   statue3 = pygame.transform.scale(statue3, (scalesize,scalesize*2))

   background = (
      ( "S1", "S1", "S1", "S1", "S2", "P1", "P1", "P1", "S3", "S1", "S1", "S1", "S1" ),
      ( "G2", "G2", "G2", "G2", "G2", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "G2", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "G2", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "G2", "P1", "P1", "P1", "G2", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "P1", "P1", "P1", "P1", "P1", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "P1", "P1", "P1", "P1", "P1", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "G2", "P1", "P1", "P1", "P1", "P1", "G2", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "P1", "P1", "P1", "P1", "P1", "P1", "P1", "G2", "G2", "G2" ),
      ( "G2", "G2", "G2", "P1", "P1", "P1", "P1", "P1", "P1", "P1", "G2", "G2", "G2" ),
   )

   foreground = (
      ( "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  " ),
      ( "  ", "PD", "PD", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "PD", "  ", "  " ),
      ( "F1", "  ", "T2", "  ", "  ", "  ", "  ", "  ", "  ", "A1", "  ", "A2", "  " ),
      ( "F1", "GR", "  ", "T2", "  ", "  ", "  ", "  ", "  ", "  ", "PD", "T2", "  " ),
      ( "F1", "SK", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "PU", "  ", "  " ),
      ( "F1", "T2", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  " ),
      ( "F1", "  ", "A3", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "L1", "  ", "  " ),
      ( "F1", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "T2", "  " ),
      ( "T2", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  " ),
      ( "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  " ),
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
      if did_fade == False:
         for map_y in background:
            for map_x in map_y:
               if map_x == 'S1':
                  gameDisplay.blit(stone1,(loc_x,loc_y))
               if map_x == 'S2':
                  gameDisplay.blit(stone2,(loc_x,loc_y))
               if map_x == 'S3':
                  gameDisplay.blit(stone3,(loc_x,loc_y))
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
      if did_fade == False:
         for map_y in foreground:
            for map_x in map_y:
               if map_x == 'GR':
                  gameDisplay.blit(grave,(loc_x,loc_y))
               if map_x == 'SK':
                  gameDisplay.blit(skull,(loc_x,loc_y))
               if map_x == 'PD':
                  gameDisplay.blit(seedling,(loc_x,loc_y))
               if map_x == 'PU':
                  gameDisplay.blit(pumpkin,(loc_x,loc_y))
               if map_x == 'T2':
                  gameDisplay.blit(tree2,(loc_x,loc_y))
               if map_x == 'F1':
                  gameDisplay.blit(fence,(loc_x,loc_y))
               if map_x == 'L1':
                  gameDisplay.blit(log,(loc_x,loc_y))
               if map_x == 'A2':
                  gameDisplay.blit(statue2,(loc_x,loc_y))
               if map_x == 'A3':
                  gameDisplay.blit(statue3,(loc_x,loc_y))
               if map_x == 'A1':
                  if not summoned:
                     statue_x = loc_x
                     statue_y = loc_y
                     if summoning > 0:
                        if summoning == 1:
                           pygame.mixer.Sound.play(ufo_sound)
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
                           if summoning == 117:
                              pygame.mixer.Sound.play(pop_sound)
                        if summoning > 120:
                           summoned = True
                     gameDisplay.blit(statue,(statue_x,statue_y))
               loc_x = loc_x + scalesize
            loc_y = loc_y + scalesize
            loc_x = 0;

      # Foreground tiles that don't fit into my tile engine
      if chest != 'hidden':
         if chest == 'open':
            gameDisplay.blit(chest_open, (390,380))
         else:
            gameDisplay.blit(chest_closed, (390,380))
      if show_key:
         gameDisplay.blit(key, (390,350))
      if show_bear:
         gameDisplay.blit(bear, (358,353))
      if show_cake:
         gameDisplay.blit(cake_hover, (cake_x,cake_y))


      if did_fade != True:
         gameDisplay.blit(fountain,(327,490))

      gameDisplay.blit(morgan.get_image(), morgan.get_location())
      gameDisplay.blit(martin.get_image(), martin.get_location())
      gameDisplay.blit(zander.get_image(), zander.get_location())
      gameDisplay.blit(ghost.get_image(), ghost.get_location())
      gameDisplay.blit(geoff.get_image(), geoff.get_location())
      if summoned:
         gameDisplay.blit(ace.get_image(), ace.get_location())
      gameDisplay.blit(cat1.get_image(), cat1.get_location())
      gameDisplay.blit(cat2.get_image(), cat2.get_location())
      gameDisplay.blit(cat3.get_image(), cat3.get_location())

      # This is the non-interactive .. thing. Each phase is an 'act' of the animation.
      # I'm sure there are better ways of doing this.. this is what I came up with,
      # while drinking a cup of tea.

      # Morgan walks in to the right
      if phase == 0:
         if done_hoot != True:
            pygame.mixer.Sound.play(hoot_sound)
            done_hoot = True
         t1 = cat1.move_right(900)
         t2 = cat2.move_left(-100)
         t3 = cat3.move_right(900)
         font = 'EightBitDragon-anqx.ttf'
         font = pygame.font.Font(font,30)
         gameDisplay.blit(font.render('England',1,(255,255,255)),(350,140))
         gameDisplay.blit(font.render('2020',1,(255,255,255)),(378,185))
         if t1 and t2 and t3:
            frame_counter = frame_counter + 1
            if frame_counter > 50:
               frame_counter = 0
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
         t1 = morgan.move_down(300)
         t2 = martin.move_down(300)
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
         dialogue(martin,'But first...')
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
         if zander.move_down(220):
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
         if geoff.move_down(220):
            phase = 17

      if phase == 17:
         frame_counter = frame_counter + 1
         if frame_counter > 10:
            frame_counter = 0
            phase = 18

      if phase == 18:
         dialogue(geoff,'Want to see my new Beano?')
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
         dialogue(ace,'HERE!')
         phase = 24

      if phase == 24:
         t1 = ace.move_up(120)
         t2 = ace.move_left(390)
         if t1 and t2:
            phase = 25

      if phase == 25:
         if ace.move_down(215):
            phase = 26

      if phase == 26:
         dialogue(martin,'Now that everybody is here, we just want to say..')
         phase = 27

      if phase == 27:
         show_cake = True
         frame_counter = frame_counter + 1
         if frame_counter > 50:
            frame_counter = 0
            cake = pygame.image.load('tiles/cake.png')
            cake.set_colorkey(cake.get_at((0,0)), pygame.RLEACCEL)
            cake = pygame.transform.scale(cake, (scalesize*2,scalesize*2))
            dialogue_all('everybody', cake,'HAPPY BIRTHDAY GRANDPA!')
            phase = 28

      if phase == 28:
         dialogue(morgan,'We hope you have an amazing day!')
         phase = 29

      if phase == 29:
         frame_counter = frame_counter + 1
         if frame_counter > 100:
            frame_counter = 0
            phase = 30

      if phase == 30:
         show_cake = False
         dialogue(zander,'Wait, what\'s in the chest?')
         phase = 31

      if phase == 31:
         dialogue(ace,'Yeh, I was in the middle of a game!')
         phase = 32

      if phase == 32:
         dialogue(morgan,'Well let\'s open it and find out!')
         show_key = True
         phase = 33

      if phase == 33:
         frame_counter = frame_counter + 1
         if frame_counter == 90:
            pygame.mixer.Sound.play(open_sound)
         if frame_counter > 100:
            frame_counter = 0
            phase = 34

      if phase == 34:
         show_key = False
         chest = 'open'
         frame_counter = frame_counter + 1
         if frame_counter > 100:
            frame_counter = 0
            phase = 35

      if phase == 35:
         chest = 'hidden'
         show_bear = True
         frame_counter = frame_counter + 1
         if frame_counter == 1:
            pygame.mixer.music.play(1)
         if frame_counter > 100:
            frame_counter = 0
            phase = 36

      if phase == 36:
         dialogue(martin,'That\'s interesting...')
         phase = 37

      if phase == 37:
         dialogue(morgan,'That means...')
         phase = 38

      if phase == 38:
         dialogue(geoff,'What does it mean?')
         phase = 39

      if phase == 39:
         dialogue(zander,'Oh no...')
         phase = 40

      if phase == 40:
         dialogue(ace,'Not again...')
         phase = 41

      if phase == 41:
         dialogue(morgan,'Yes, again.')
         phase = 42

      if phase == 42:
         dialogue(morgan,'Arriving April 2021')
         phase = 43

      if phase == 43:
         dialogue(geoff,'I\'m not sharing my Lego.')
         phase = 44

      if phase == 44:
         dialogue(morgan,'Hush all of you!')
         phase = 45

      if phase == 45:
         dialogue(morgan,'Thank you for listening to our news!')
         phase = 46

      if phase == 46:
         dialogue(martin,'We hope you are excited as we are!')
         phase = 47

      if phase == 47:
         frame_counter = frame_counter + 1
         if frame_counter > 100:
            frame_counter = 0
            phase = 48

      if phase == 48:
         did_fade = True
         fadeout()
         phase = 49

      if phase == 49:
         pygame.draw.rect(gameDisplay,(0,0,0),(30,30,740,540))
         font_heading = 'EightBitDragon-anqx.ttf'
         font_heading = pygame.font.Font(font_heading,20)
         font_body = 'EightBitDragon-anqx.ttf'
         font_body = pygame.font.Font(font_body,15)
         gameDisplay.blit(font_heading.render('Sound Credits',1,(255,255,255)),(320,60))
         gameDisplay.blit(font_body.render('https://freesound.org/people/BeezleFM (unlock)',1,(193,193,193)),(140,100))
         gameDisplay.blit(font_body.render('https://freesound.org/people/erkanozan/ (ufo)',1,(193,193,193)),(140,120))
         gameDisplay.blit(font_body.render('https://freesound.org/people/Breviceps/ (owl)',1,(193,193,193)),(140,140))
         gameDisplay.blit(font_heading.render('Lullaby Music',1,(255,255,255)),(330,180))
         gameDisplay.blit(font_body.render('David Vitas @davidvitas',1,(193,193,193)),(290,220))
         gameDisplay.blit(scan, (150,280))
         frame_counter = frame_counter + 1
         if frame_counter > 300:
            frame_counter = 0
            fadeout()
            phase = 50

      if phase == 50:
         pygame.draw.rect(gameDisplay,(0,0,0),(30,30,740,540))
         font_heading = 'EightBitDragon-anqx.ttf'
         font_heading = pygame.font.Font(font_heading,20)
         font_body = 'EightBitDragon-anqx.ttf'
         font_body = pygame.font.Font(font_body,15)
         gameDisplay.blit(font_heading.render('Graphics',1,(255,255,255)),(355,60))
         gameDisplay.blit(font_body.render('https://pipoya.itch.io/pipoya-rpg-tileset-32x32 (tiles)',1,(193,193,193)),(140,100))
         gameDisplay.blit(font_body.render('Character sprites from ???',1,(193,193,193)),(140,120))
         gameDisplay.blit(font_heading.render('Thanks for watching :-)',1,(255,255,255)),(270,170))
         gameDisplay.blit(font_body.render('www.starfighter.dev',1,(193,193,193)),(310,230))
         gameDisplay.blit(scan, (150,280))


      #cat1 = Character('cat1', -100, 20)
      #cat2 = Character('cat2', 900, 40)
      #cat3 = Character('cat3', -100, 60)

      pygame.display.update()
      clock.tick(60)

intro()
pygame.quit()
quit()
