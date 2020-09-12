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

def game_loop():

   x = (display_width * 0.45)
   y = (display_height * 0.8)
   x_change = 0

   gameExit = False

   while not gameExit:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            gameExit = True

         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               x_change = -5
            elif event.key == pygame.K_RIGHT:
               x_change = 5

         if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               x_change = 0

         #debug
         print(event)

      x += x_change

      gameDisplay.fill(white)
      car(x,y)
      pygame.display.update()
      clock.tick(60)

game_loop()
pygame.quit()
quit()
