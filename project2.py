import pygame
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game screen.")
rectangle = pygame.Rect(320, 240, 400, 300)
rectangle.center = (WIDTH // 2, HEIGHT // 2)
font = pygame.font.Font(None, 70)
word = font.render("Kapow", True, pygame.Color("black"))
text = word.get_rect(center=rectangle.center)
programIsRunning = True
while programIsRunning:
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (55, 5, 255), rectangle)
    screen.blit(word, text)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programIsRunning = False
    pygame.display.flip()
pygame.quit()