# main.py
import pygame
from game import Game

# Inicializar Pygame sin sonido
pygame.mixer.pre_init(0)  # Desactiva el módulo de sonido
pygame.init()

# Configurar la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Disparos")

# Crear el juego
game = Game()

# Iniciar el juego
game.start()

# Bucle principal
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar el juego
    game.update(screen)

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

# Cerrar Pygame
pygame.quit()