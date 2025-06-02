import pygame
import random
import time

# Initialize Pygame
pygame.init() 

# Screen dimensions
WIDTH, HEIGHT = 840, 480
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHTBLUE = (0, 225, 255)

# Player properties
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 3

#Randint getting bigger
max_enemy_width= 30

# Enemy properties
enemy_width= random.randint(30, max_enemy_width)
enemy_height= 30
enemy_x = random.randint(0, WIDTH - enemy_width)
enemy_y = 0
enemy_speed = random.randint(15, 20)
score =0
font = pygame.font.Font(None, 80)

# Game loop
running = True
while running:
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x = player_x -player_speed
    if keys[pygame.K_RIGHT]:
        player_x = player_x +player_speed
    if keys[pygame.K_ESCAPE]:
        running = False
   
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_width= random.randint(30, max_enemy_width)
        enemy_speed = random.randint(2, 4)
        enemy_x = random.randint(0, WIDTH - enemy_width)
        enemy_y = 0
        score +=1
        max_enemy_width +=3

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    if player_rect.colliderect(enemy_rect):
        print("Game Over!")
        running = False # ends the game loop

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, LIGHTBLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))
    score_text = font.render (f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))  
    pygame.display.flip()
    clock.tick(144)
pygame.quit()