import pygame
import random

pygame.init()

# ------------------------
# SETTINGS
# ------------------------
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ultimate Boss Level")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Colors
BLACK = (20, 20, 20)
WHITE = (255, 255, 255)
GREEN = (0, 220, 0)
RED = (220, 0, 0)
BLUE = (0, 120, 255)
YELLOW = (255, 255, 0)
PURPLE = (180, 0, 180)
CYAN = (0, 255, 255)
ORANGE = (255, 150, 0)

# ------------------------
# PLAYER
# ------------------------
player = pygame.Rect(50, 500, 40, 60)

player_speed = 6
jump_power = -15
gravity = 0.8
velocity_y = 0
on_ground = False

health = 100
coins = 0
has_key = False

# ------------------------
# PLATFORMS
# ------------------------
platforms = [
    pygame.Rect(0, 650, 1200, 50),
    pygame.Rect(150, 550, 150, 20),
    pygame.Rect(400, 500, 200, 20),
    pygame.Rect(700, 430, 180, 20),
    pygame.Rect(980, 350, 180, 20),
    pygame.Rect(800, 250, 150, 20),
    pygame.Rect(500, 180, 180, 20),
]

# ------------------------
# ITEMS
# ------------------------
coins_list = [
    pygame.Rect(200, 510, 20, 20),
    pygame.Rect(500, 460, 20, 20),
    pygame.Rect(760, 390, 20, 20),
    pygame.Rect(1040, 310, 20, 20),
]

health_pack = pygame.Rect(840, 210, 25, 25)
key = pygame.Rect(580, 140, 25, 25)

# ------------------------
# BOSS
# ------------------------
boss = pygame.Rect(1020, 120, 100, 100)
boss_health = 3
boss_direction = 4

boss_projectiles = []

# ------------------------
# PLAYER ATTACKS
# ------------------------
player_bullets = []

# ------------------------
# PORTAL
# ------------------------
portal = pygame.Rect(1080, 580, 60, 70)

# ------------------------
# GAME LOOP
# ------------------------
running = True
win = False

while running:
    clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and on_ground:
                velocity_y = jump_power

            if event.key == pygame.K_f:
                bullet = pygame.Rect(
                    player.centerx,
                    player.centery,
                    20,
                    8
                )
                player_bullets.append(bullet)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player.x -= player_speed

    if keys[pygame.K_d]:
        player.x += player_speed

    # ------------------------
    # GRAVITY
    # ------------------------
    velocity_y += gravity
    player.y += velocity_y

    on_ground = False

    for platform in platforms:
        if player.colliderect(platform) and velocity_y > 0:
            player.bottom = platform.top
            velocity_y = 0
            on_ground = True

    # ------------------------
    # COINS
    # ------------------------
    for coin in coins_list[:]:
        if player.colliderect(coin):
            coins += 1
            coins_list.remove(coin)

    # Health pack
    if player.colliderect(health_pack):
        health = min(100, health + 30)
        health_pack.x = -100

    # Key
    if player.colliderect(key):
        has_key = True
        key.x = -100

    # ------------------------
    # BOSS MOVEMENT
    # ------------------------
    if boss_health > 0:
        boss.x += boss_direction

        if boss.left < 900:
            boss_direction = 4

        if boss.right > 1180:
            boss_direction = -4

    # ------------------------
    # BOSS ATTACKS
    # ------------------------
    if random.randint(1, 40) == 1 and boss_health > 0:
        shot = pygame.Rect(
            boss.centerx,
            boss.centery,
            18,
            18
        )
        boss_projectiles.append(shot)

    for shot in boss_projectiles[:]:
        if player.centerx < shot.x:
            shot.x -= 7
        else:
            shot.x += 7

        if player.centery < shot.y:
            shot.y -= 3
        else:
            shot.y += 3

        if player.colliderect(shot):
            health -= 10
            boss_projectiles.remove(shot)

        elif shot.x < -50 or shot.x > WIDTH + 50:
            boss_projectiles.remove(shot)

    # ------------------------
    # PLAYER BULLETS
    # ------------------------
    for bullet in player_bullets[:]:
        bullet.x += 12

        if boss.colliderect(bullet) and boss_health > 0:
            boss_health -= 10
            player_bullets.remove(bullet)

        elif bullet.x > WIDTH:
            player_bullets.remove(bullet)

    # ------------------------
    # WIN CONDITION
    # ------------------------
    if has_key and boss_health <= 0:
        if player.colliderect(portal):
            win = True

    # ------------------------
    # LOSE CONDITION
    # ------------------------
    if health <= 0:
        running = False

    # ------------------------
    # DRAW
    # ------------------------
    screen.fill(BLACK)

    # Platforms
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)

    # Portal
    if boss_health <= 0:
        pygame.draw.rect(screen, CYAN, portal)
    for coin in coins_list:
        pygame.draw.rect(screen, YELLOW, coin)
    pygame.draw.rect(screen, ORANGE, health_pack)
    pygame.draw.rect(screen, WHITE, key)
    pygame.draw.rect(screen, BLUE, player)
    if boss_health > 0:
        pygame.draw.rect(screen, RED, boss)
    for shot in boss_projectiles:
        pygame.draw.rect(screen, PURPLE, shot)
    for bullet in player_bullets:
        pygame.draw.rect(screen, WHITE, bullet)
    health_text = font.render(f"Health: {health}", True, WHITE)
    coin_text = font.render(f"Coins: {coins}", True, WHITE)
    boss_text = font.render(f"Boss HP: {max(0,boss_health)}", True, WHITE)
    screen.blit(health_text, (20, 20))
    screen.blit(coin_text, (20, 60))
    screen.blit(boss_text, (20, 100))

    if has_key:
        key_text = font.render("KEY ACQUIRED", True, YELLOW)
        screen.blit(key_text, (20, 140))

    if win:
        win_text = font.render(
            "ULTIMATE BOSS DEFEATED! YOU WIN!",
            True,
            CYAN
        )
        screen.blit(win_text, (320, 40))

    pygame.display.flip()

pygame.quit()