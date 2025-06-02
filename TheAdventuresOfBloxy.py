import pygame
import sys
import random
pygame.init() 

#Screen Dimensions
WIDTH, HEIGHT = 600, 800
clock = pygame.time.Clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Colors
Fuscia = (255, 0, 79)
Blue = (0, 255, 0)

# Side Block Colors
SIDE_COLORS = [Fuscia]

# Bloxy Sizing
bloxy_size = 40
bloxy_x = WIDTH // 2 - bloxy_size // 2
bloxy_y = HEIGHT - bloxy_size - 10
bloxy_speed = 3

#Boxel Sizing
max_boxel_height = 40
boxel_width = random.randint (max_boxel_height, 20)
boxel_height = 40 
boxel_x = random.randint (0, HEIGHT - boxel_height)
boxel_y = 0
boxel_speed = random.randint (5, 15)
score = 0
font = pygame.font.get_default_font(0, 80)

#Game Time
running = True
while running:
    pygame.event.pump
    keys = pygame.key.get_pressed()
    if keys [pygame.K_w] :
        bloxy_height = bloxy_height -bloxy_speed
    if keys [pygame.K_s] :
        bloxy_height = bloxy_height +bloxy_speed
    if keys [pygame.K_a] :
        bloxy_x = bloxy_x -bloxy_speed
    if keys [pygame.K_d] :
        bloxy_x = bloxy_x +bloxy_speed
    if keys [pygame.K_ESCAPE] :
        running = False
    
    
