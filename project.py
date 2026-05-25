import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

caption = pygame.display.set_caption("My first game screen.")

pikachuImage = pygame.image.load("pikachu.png")

pikachuResizedImage = pygame.transform.scale(pikachuImage, (300, 300))
pikachu_rect = pikachuResizedImage.get_rect()
pikachu_rect.center = (250,250)

programIsRunning = True
while programIsRunning:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      programIsRunning = False

    screen.blit(pikachuResizedImage, pikachu_rect)
    pygame.display.flip()
    
pygame.quit()