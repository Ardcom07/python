import pygame
import random
import math

# Inicialización
pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doom-like Shooter")

# Colores
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Recursos
PLAYER_IMG = pygame.Surface((40, 40))
PLAYER_IMG.fill(GREEN)
ENEMY_IMG = pygame.Surface((40, 40))
ENEMY_IMG.fill(RED)
BULLET_IMG = pygame.Surface((10, 10))
BULLET_IMG.fill(WHITE)


# Jugador
player_pos = [WIDTH//2, HEIGHT//2]
player_speed = 20
player_health = 1

# Balas y enemigos
bullets = []
enemies = []

clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 30)

def spawn_enemy():
    x = random.choice([0, WIDTH])
    y = random.randint(0, HEIGHT)
    enemies.append({"pos": [x, y], "speed": 15})

def draw_window():
    WIN.fill(BLACK)
    WIN.blit(PLAYER_IMG, player_pos)

    for bullet in bullets:
        WIN.blit(BULLET_IMG, bullet["pos"])

    for enemy in enemies:
        WIN.blit(ENEMY_IMG, enemy["pos"])

    health_text = font.render(f"Health: {player_health}", True, WHITE)
    WIN.blit(health_text, (10, 10))
    pygame.display.update()

def handle_bullets():
    global enemies
    for bullet in bullets[:]:
        bullet["pos"][0] += bullet["dir"][0] * 10
        bullet["pos"][1] += bullet["dir"][1] * 10

        if not (0 < bullet["pos"][0] < WIDTH and 0 < bullet["pos"][1] < HEIGHT):
            bullets.remove(bullet)

    for enemy in enemies[:]:
        ex, ey = enemy["pos"]
        for bullet in bullets[:]:
            bx, by = bullet["pos"]
            if abs(ex - bx) < 30 and abs(ey - by) < 30:
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

def handle_enemies():
    global player_health
    for enemy in enemies:
        dx = player_pos[0] - enemy["pos"][0]
        dy = player_pos[1] - enemy["pos"][1]
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx /= dist
            dy /= dist
        enemy["pos"][0] += dx * enemy["speed"]
        enemy["pos"][1] += dy * enemy["speed"]

        if abs(enemy["pos"][0] - player_pos[0]) < 30 and abs(enemy["pos"][1] - player_pos[1]) < 30:
            player_health -= 1

def main():
    global player_health
    run = True
    spawn_timer = 0

    while run:
        clock.tick(60)
        spawn_timer += 1
        if spawn_timer > 60:
            spawn_enemy()
            spawn_timer = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Movimiento jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: player_pos[1] -= player_speed
        if keys[pygame.K_s]: player_pos[1] += player_speed
        if keys[pygame.K_a]: player_pos[0] -= player_speed
        if keys[pygame.K_d]: player_pos[0] += player_speed

        # Disparo
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            dx, dy = mx - player_pos[0], my - player_pos[1]
            dist = math.hypot(dx, dy)
            if dist == 0: dist = 1
            dir_x, dir_y = dx/dist, dy/dist
            bullets.append({
                "pos": player_pos.copy(),
                "dir": [dir_x, dir_y]
            })

        handle_bullets()
        handle_enemies()
        draw_window()

        if player_health <= 0:
            print("¡GAME OVER!")
            run = False

    pygame.quit()

if __name__ == "__main__":
    main()
