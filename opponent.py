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
        if self.x <= 0 or self.x >= 800 - self.width:
            self.direction *= -1

    def shoot(self):
        # Dispara hacia abajo cada cierto tiempo
        current_time = pygame.time.get_ticks()
        if current_time - self.shoot_timer >= 2000 and self.is_alive and not self.is_star:
            self.shoot_timer = current_time
            return Shot(self.x + self.width // 2, self.y + self.height, "bullet", direction=1)
        return None

    def collide(self, shots, game):
        if not self.is_alive or self.is_star:
            return
        # Verifica colisiones con disparos del jugador
        for shot in shots:
            if shot.direction == -1:  # Disparos del jugador van hacia arriba
                shot_rect = pygame.Rect(shot.x, shot.y, 10, 10)
                opponent_rect = pygame.Rect(self.x, self.y, self.width, self.height)
                if shot_rect.colliderect(opponent_rect):
                    self.lives -= 1
                    if self.lives <= 0:
                        self.is_alive = False
                        self.is_star = True
                        game.score += 1  # Incrementa la puntuación
                    shots.remove(shot)
                    break

    def draw(self, screen):
        if self.is_alive and not self.is_star:
            pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        elif self.is_star:
            # Representa una estrella con un color diferente
            pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, self.width, self.height))