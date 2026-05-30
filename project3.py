import pygame
pygame.init()
width, height = 800, 500
screen = pygame.display.set_mode((width, height))
caption = pygame.display.set_caption("Sprite Frenzy")
spr1_width, spr1_height = 50, 50
spr2_width, spr2_height = 550, 250
spr1_color = pygame.Color("white")
spr2_color = pygame.Color("blue")
x1 = 0
y1 = 0
x2, y2 = 125, 125
play_mode = True
while play_mode:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play_mode = False
    screen.fill((0, 0, 0))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: x1 -= 1
    if pressed[pygame.K_RIGHT]: x1 += 1
    if pressed[pygame.K_UP]: y1 -= 1
    if pressed[pygame.K_DOWN]: y1 += 1
    x1 = min(max(0, x1), width - spr1_width)
    y1 = min(max(0, y1), height - spr1_height)
    rect1 = pygame.Rect(x1, y1, spr1_width, spr1_height)
    rect2 = pygame.Rect(x2, y2, spr2_width, spr2_height)
    if rect1.colliderect(rect2):
        continue
    pygame.draw.rect(screen, spr1_color, rect1)
    pygame.draw.rect(screen, spr2_color, rect2)
    pygame.display.flip()
pygame.quit()