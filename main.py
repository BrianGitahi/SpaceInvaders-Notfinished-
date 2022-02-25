import pygame
import random
import math

# Initialize pygame
pygame.init()

# Create game screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("background.png")

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
player_x = 370
player_y = 480
player_move = 0

# Enemy
enemyImg = pygame.image.load("enemy.png")
enemy_x = random.randint(0, 720)
enemy_y = random.randint(50, 150)
enemy_x_move = 2
enemy_y_move = 20

# Bullet

# Ready - bullet is unseen
# Fire - bullet is moving
bulletImg = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 480
bullet_x_move = 0
bullet_y_move = 3
bullet_state = "ready"

score = 0

# Allows a player to appear on screen
def player(x, y):
    screen.blit(playerImg, (x, y))


# Allows the enemy to appear on screen
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB values
    screen.fill((255, 255, 255))
    # Background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If Keystroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_move = -5

            if event.key == pygame.K_RIGHT:
                player_move = 5

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        # This loop allows the game to know what to do when a key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                player_move = 0
    # Checking for player boundary to prevent out of bounds movement
    player_x += player_move

    if player_x <= 16:
        player_x = 16
    elif player_x >= 720:
        player_x = 720

    # Enemy Movement
    enemy_x += enemy_x_move

    if enemy_x <= 16:
        enemy_x_move = 2
        enemy_y += enemy_y_move
    elif enemy_x >= 720:
        enemy_x_move = -2
        enemy_y += enemy_y_move

    # Bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_move

    # Collision
    collision = isCollision(enemy_x, enemy_y, bullet_x, bullet_y)
    if collision:
        bullet_y = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemy_x = random.randint(0, 800)
        enemy_y = random.randint(50, 150)

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update()
