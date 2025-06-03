import pygame
import sys
import random
pygame.init() 

# Screen Dimensions
WIDTH, HEIGHT = 600, 800
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
Fuscia = (255, 0, 79)
Blue = (0, 255, 0)
Black = (0, 0, 0)
White = (255, 255, 255)
Dark_Red = (100, 0, 0)

# Side Block Colors
BOXEL_COLORS = [Fuscia]

# Bloxy Colors
BLOXY_COLORS = [Blue]

# Bloxy Sizing
bloxy_size = 40
bloxy_x = WIDTH // 2 - bloxy_size // 2
bloxy_y = HEIGHT - bloxy_size - 10
bloxy_speed = 3

# Boxel Sizing
max_boxel_height = 40
boxel_width = random.randint(20, max_boxel_height)
boxel_height = 40 
boxel_x = random.randint(0, WIDTH - 40)
boxel_y = 0
boxel_speed = random.randint(5, 15)
score = 0
font = pygame.font.Font(None, 80)

# Game Time
running = True
while running:
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        bloxy_y -= bloxy_speed
    if keys[pygame.K_s]:
        bloxy_y += bloxy_speed
    if keys[pygame.K_a]:
        bloxy_x -= bloxy_speed
    if keys[pygame.K_d]:
        bloxy_x += bloxy_speed
    if keys[pygame.K_ESCAPE]:
        running = False

    boxel_y += boxel_speed
    if boxel_y > HEIGHT:
        boxel_height = random.randint(20, max_boxel_height)
        boxel_width = random.randint(20, max_boxel_height)
        boxel_speed = random.randint(2, 4)
        boxel_x = random.randint(0, WIDTH - boxel_width)
        boxel_y = 0
        score += 1
        max_boxel_height += 3

    # Game Over
    bloxy_rect = pygame.Rect(bloxy_x, bloxy_y, bloxy_size, bloxy_size)
    boxel_rect = pygame.Rect(boxel_x, boxel_y, boxel_width, boxel_height)
    if bloxy_rect.colliderect(boxel_rect):
        print("Mission Failed, We'll Get 'Em Next Time!")
        running = False

    # Putting it on the screen
    screen.fill(Dark_Red)
    pygame.draw.rect(screen, BLOXY_COLORS[0], (bloxy_x, bloxy_y, bloxy_size, bloxy_size))
    pygame.draw.rect(screen, BOXEL_COLORS[0], (boxel_x, boxel_y, boxel_width, boxel_height))
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (5, 5))
    pygame.display.flip()
    clock.tick(144)
pygame.quit()