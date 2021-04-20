import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Title and icon
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("rocket.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX,playerY))

# Game loop
running = True
while running:

    screen.fill((255, 150, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()
