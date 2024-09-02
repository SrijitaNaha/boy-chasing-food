import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the title of the window
pygame.display.set_caption("boy Food Game")

# Load the images for the food and boy
food_image = pygame.image.load('food.png')
boy_image = pygame.image.load('boy.png')

# Set up the food and boy sprites
food = pygame.sprite.Sprite()
food.image = food_image
food.rect = food_image.get_rect()
food.rect.center = (WIDTH // 2, HEIGHT // 2)

boy = pygame.sprite.Sprite()
boy.image = boy_image
boy.rect = boy_image.get_rect()
boy.rect.center = (WIDTH // 2, HEIGHT // 2 + 100)

# Set up the sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(food)
all_sprites.add(boy)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the boy
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        boy.rect.x -= 20
    if keys[pygame.K_RIGHT]:
        boy.rect.x += 20
    if keys[pygame.K_UP]:
        boy.rect.y -= 20
    if keys[pygame.K_DOWN]:
        boy.rect.y += 20

    # Check for collision with food
    if boy.rect.colliderect(food.rect):
        food.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)