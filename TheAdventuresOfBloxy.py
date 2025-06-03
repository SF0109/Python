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
Yellow = (255, 255, 0)
Aqua = (0, 255, 255)

# Side Block Colors
BOXEL_COLORS = [Fuscia]
SIDE_LEFT_BOXEL_COLOR = Yellow      # Fixed: use tuple, not list
SIDE_RIGHT_BOXEL_COLOR = Aqua       # Fixed: use tuple, not list

# Bloxy Colors
BLOXY_COLORS = [Blue]

# Bloxy Sizing
bloxy_size = 40
bloxy_x = WIDTH // 2 - bloxy_size // 2
bloxy_y = HEIGHT - bloxy_size - 10
bloxy_speed = 3

# Boxel Size
max_boxel_height = 40
boxel_width = random.randint(20, max_boxel_height)
boxel_height = 40 
boxel_x = random.randint(0, WIDTH - 40)
boxel_y = 0
boxel_speed = random.randint(5, 15)

# Side Boxels
max_side_boxel_size = 60
# Left Boxels
side_left_height = random.randint(30, max_side_boxel_size)
side_left_width = random.randint(20, 40)
side_left_x = 0
side_left_y = random.randint(0, HEIGHT - side_left_height)
side_left_speed = random.randint(4, 10)
# Right Boxels
side_right_height = random.randint(30, max_side_boxel_size)
side_right_width = random.randint(20, 40)
side_right_x = WIDTH - side_right_width
side_right_y = random.randint(0, HEIGHT - side_right_height)
side_right_speed = random.randint(4, 10)

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

    # Keep Bloxy within screen bounds
    if bloxy_x < 0:
        bloxy_x = 0
    if bloxy_x + bloxy_size > WIDTH:
        bloxy_x = WIDTH - bloxy_size
    if bloxy_y < 0:
        bloxy_y = 0
    if bloxy_y + bloxy_size > HEIGHT:
        bloxy_y = HEIGHT - bloxy_size

    # Move Basic Boxels
    boxel_y += boxel_speed
    if boxel_y > HEIGHT:
        boxel_height = random.randint(20, max_boxel_height)
        boxel_width = random.randint(20, max_boxel_height)
        boxel_speed = random.randint(4, 8)
        boxel_x = random.randint(0, WIDTH - boxel_width)
        boxel_y = 0
        score += 1
        max_boxel_height += 3

    # Move Advanced Boxel Left-Right
    side_left_x += side_left_speed
    if side_left_x > WIDTH:
        side_left_height = random.randint(30, max_side_boxel_size)
        side_left_width = random.randint(20, 40)
        side_left_x = 0 - side_left_width
        side_left_y = random.randint(0, HEIGHT - side_left_height)
        side_left_speed = random.randint(4, 8)

    # Move Advanced Boxel Right-Left
    side_right_x -= side_right_speed
    if side_right_x + side_right_width < 0:
        side_right_height = random.randint(30, max_side_boxel_size)
        side_right_width = random.randint(20, 40)
        side_right_x = WIDTH
        side_right_y = random.randint(0, HEIGHT - side_right_height)
        side_right_speed = random.randint(4, 8)

    # Game Over
    bloxy_rect = pygame.Rect(bloxy_x, bloxy_y, bloxy_size, bloxy_size)
    boxel_rect = pygame.Rect(boxel_x, boxel_y, boxel_width, boxel_height)
    side_left_rect = pygame.Rect(side_left_x, side_left_y, side_left_width, side_left_height)
    side_right_rect = pygame.Rect(side_right_x, side_right_y, side_right_width, side_right_height)
    if (bloxy_rect.colliderect(boxel_rect) or
        bloxy_rect.colliderect(side_left_rect) or
        bloxy_rect.colliderect(side_right_rect)):
        print("Mission Failed, We'll Get 'Em Next Time!")
        running = False

    # Drawing
    screen.fill(Dark_Red)
    pygame.draw.rect(screen, BLOXY_COLORS[0], (bloxy_x, bloxy_y, bloxy_size, bloxy_size))
    pygame.draw.rect(screen, BOXEL_COLORS[0], (boxel_x, boxel_y, boxel_width, boxel_height))
    pygame.draw.rect(screen, SIDE_LEFT_BOXEL_COLOR, (side_left_x, side_left_y, side_left_width, side_left_height))
    pygame.draw.rect(screen, SIDE_RIGHT_BOXEL_COLOR, (side_right_x, side_right_y, side_right_width, side_right_height))
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (5, 5))
    pygame.display.flip()
    clock.tick(144)
pygame.quit()