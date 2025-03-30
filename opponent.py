# opponent.py
import pygame
from character import Character
from shot import Shot

class Opponent(Character):
    def __init__(self, x, y, image):
        super().__init__(x, y, image, lives=1)
        self.is_star = False
        self.width = 40
        self.height = 40
        self.speed = 3
        self.direction = 1  # 1 para derecha, -1 para izquierda
        self.shoot_timer = 0

    def move(self):
        # Movimiento de lado a lado
        if self.is_star or not self.is_alive:
            return
        self.x += self.speed * self.direction
        # Cambiar dirección si llega a los bordes
        if self.x <= 0:
            self.direction = 1
        elif self.x >= 800 - self.width:
            self.direction = -1

    def shoot(self):
        # Dispara hacia abajo cada 2 segundos
        current_time = pygame.time.get_ticks()
        if current_time - self.shoot_timer >= 2000:  # 2 segundos
            self.shoot_timer = current_time
            return Shot(self.x + self.width // 2, self.y + self.height, "bullet", direction=1)
        return None

    def collide(self, shots):
        if self.is_star or not self.is_alive:
            return False
        # Verifica colisiones con disparos del jugador
        for i in range(len(shots) - 1, -1, -1):  # Iteramos en orden inverso para evitar problemas al eliminar
            shot = shots[i]
            if shot.direction == -1:  # Disparos del jugador van hacia arriba
                shot_rect = pygame.Rect(shot.x, shot.y, 10, 10)
                opponent_rect = pygame.Rect(self.x, self.y, self.width, self.height)
                if shot_rect.colliderect(opponent_rect):
                    self.lives -= 1
                    if self.lives <= 0:
                        self.is_alive = False
                        self.is_star = True
                    shots.pop(i)  # Usamos pop() en lugar de remove() para eliminar por índice
                    return True
        return False

    def draw(self, screen):
        if not self.is_alive:
            return
        if self.is_star:
            pygame.draw.circle(screen, (255, 255, 0), (self.x + self.width // 2, self.y + self.height // 2), 10)
        else:
            pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
            