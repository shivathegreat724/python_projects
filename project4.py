import pygame
pygame.init()
screen_width, screen_height = 700, 400
screen = pygame.display.set_mode((screen_width, screen_height))
caption = pygame.display.set_caption("Sprite Territory")
x = 350
y = 0
x1, y1 = 175, 200
x2, y2 = 525, 200
rect_width, rect_height = 50, 50
Red = pygame.Color("red")
Blue = pygame.Color("blue")
play_mode = True
while play_mode:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play_mode = False
    white_half = pygame.Rect(x, y, 350, 400)
    black_half = pygame.Rect(0, 0, 350, 400)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: x1 -= 1
    if pressed[pygame.K_RIGHT]: x1 += 1
    if pressed[pygame.K_UP]: y1 -= 1
    if pressed[pygame.K_DOWN]: y1 += 1
    if pressed[pygame.K_a]: x2 -= 1
    if pressed[pygame.K_d]: x2 += 1
    if pressed[pygame.K_w]: y2 -= 1
    if pressed[pygame.K_s]: y2 += 1
    if x1 >= 300:
        rect1_color = Red
    else:
        rect1_color = (255, 255, 255)
    if x2 >= 400:
        rect2_color = (0, 0, 0)
    else:
        rect2_color = Blue
    rect1 = pygame.Rect(x1, y1, rect_width, rect_height)
    rect2 = pygame.Rect(x2, y2, rect_width, rect_height)
    rect1.clamp_ip(black_half)
    rect2.clamp_ip(white_half)
    x1, y1 = rect1.topleft
    x2, y2 = rect2.topleft
    pygame.draw.rect(screen, (255, 255, 255), white_half)
    pygame.draw.rect(screen, (0, 0, 0), black_half)
    pygame.draw.rect(screen, rect1_color, rect1)
    pygame.draw.rect(screen, rect2_color, rect2)
    pygame.display.flip()
pygame.quit()