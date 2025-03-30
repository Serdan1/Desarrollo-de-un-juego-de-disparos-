# shot.py
import pygame
from entity import Entity

class Shot(Entity):
    def __init__(self, x, y, image, direction):
        super().__init__(x, y, image)
        self.speed = 7
        self.direction = direction  # -1 para arriba (jugador), 1 para abajo (enemigo)

    def move(self):
        self.y += self.speed * self.direction
        # Eliminar el disparo si sale de la pantalla
        if self.y < 0 or self.y > 600:
            return False
        return True

    def hit_target(self):
        pass  # La lógica de colisión se maneja en las clases Character

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 5)