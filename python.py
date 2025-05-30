import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Racing Game")

# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
FUSCIA = (255, 0, 79) 
BLUE = (0, 100, 255) 

# Player car settings
player_width, player_height = 40, 70
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Enemy car settings
enemy_width, enemy_height = 40, 70
enemy_speed = 10 #random speed for cars.
enemy_cars = []

# List of possible enemy colors
ENEMY_COLORS = [
    (0, 100, 255),   # Blue
    (0, 200, 0),     # Green
    (255, 0, 0),     # Red
    (255, 165, 0),   # Orange
    (128, 0, 128),   # Purple
    (255, 255, 0),   # Yellow
]

# Road lines
line_width, line_height = 10, 40
lines = []
for i in range(0, HEIGHT, 80):
    lines.append([WIDTH // 2 - line_width // 2, i])

# Score
score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

def draw_road():
    screen.fill(GRAY)
    for line in lines:
        pygame.draw.rect(screen, YELLOW, (line[0], line[1], line_width, line_height))
def draw_player(x, y):
    pygame.draw.rect(screen, FUSCIA, (x, y, player_width, player_height))

def draw_enemy(x, y, color):
    pygame.draw.rect(screen, color, (x, y, enemy_width, enemy_height))

def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def main():
    global player_x, score
    running = True
    enemy_timer = 0

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 40:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width - 40:
            player_x += player_speed

        # Move road lines
        for line in lines:
            line[1] += enemy_speed
            if line[1] > HEIGHT:
                line[1] = -line_height

        # Spawn enemy cars
        enemy_timer += 1
        if enemy_timer > 40:
            enemy_x = random.randint (1, WIDTH - enemy_width)
            enemy_color = random.choice(ENEMY_COLORS)
            enemy_cars.append([enemy_x, -enemy_height, enemy_color])
            enemy_timer = 0

        # Move enemy cars
        for enemy in enemy_cars:
            enemy[1] += enemy_speed

        # Remove off-screen enemies and update score
        enemy_cars[:] = [e for e in enemy_cars if e[1] < HEIGHT]
        for enemy in enemy_cars:
            if enemy[1] + enemy_height == player_y:
                score += 1

        # Collision detection
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        for enemy in enemy_cars:
            enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_width, enemy_height)
            if player_rect.colliderect(enemy_rect):
                running = False

        # Draw everything
        draw_road()
        draw_player(player_x, player_y)
        for enemy in enemy_cars:
            draw_enemy(enemy[0], enemy[1], enemy[2])
        show_score(score)
        pygame.display.flip()

    # Game over
    screen.fill(GRAY)
    text = font.render("Game Over!", True, WHITE)
    screen.blit(text, (WIDTH//2 - 80, HEIGHT//2 - 20))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()