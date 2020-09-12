#https://www.youtube.com/watch?v=ujOTNg17LjI

import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')

# my image is too big.. scale it
carImg = pygame.transform.scale(carImg, (64, 84))

def car(x,y):
   gameDisplay.blit(carImg,(x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)

crashed = False

while not crashed:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         crashed = True





      #debug
      print(event)

   gameDisplay.fill(white)
   car(x,y)
   pygame.display.update()
   clock.tick(60)

pygame.quit()
quit()
