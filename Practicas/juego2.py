import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configurar la ventana
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Dados")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuente
font = pygame.font.SysFont(None, 100)
text_font = pygame.font.SysFont(None, 40)

# Función para lanzar un dado
def roll_die():
    return random.randint(1, 6)

# Mostrar resultado de los dados
def draw_dice(die1, die2):
    screen.fill(WHITE)
    
    text1 = font.render(str(die1), True, BLACK)
    text2 = font.render(str(die2), True, BLACK)
    
    screen.blit(text1, (WIDTH // 4 - text1.get_width() // 2, HEIGHT // 2 - text1.get_height() // 2))
    screen.blit(text2, (3 * WIDTH // 4 - text2.get_width() // 2, HEIGHT // 2 - text2.get_height() // 2))

    instr = text_font.render("Presiona espacio para tirar", True, (100, 100, 100))
    screen.blit(instr, (WIDTH // 2 - instr.get_width() // 2, 20))
    
    pygame.display.flip()

# Estado inicial
die1, die2 = 1, 1
draw_dice(die1, die2)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Tirar dados con espacio o clic
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                die1 = roll_die()
                die2 = roll_die()
                draw_dice(die1, die2)

        if event.type == pygame.MOUSEBUTTONDOWN:
            die1 = roll_die()
            die2 = roll_die()
            draw_dice(die1, die2)

# Cerrar pygame
pygame.quit()
sys.exit()
