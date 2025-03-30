# boss.py
import pygame
from opponent import Opponent
from shot import Shot

class Boss(Opponent):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.lives = 5  # Más vidas que un enemigo normal
        self.speed = 6  # El doble de rápido que un Opponent (3 * 2)
        self.width = 60
        self.height = 60

    def move(self):
        # Movimiento de lado a lado, más rápido
        if self.is_star or not self.is_alive:
            return
        self.x += self.speed * self.direction
        # Cambiar dirección si llega a los bordes
        if self.x <= 0:
            self.direction = 1
        elif self.x >= 800 - self.width:
            self.direction = -1

    def shoot(self):
        # Dispara más frecuentemente que un enemigo normal
        current_time = pygame.time.get_ticks()
        if current_time - self.shoot_timer >= 1000:  # 1 segundo
            self.shoot_timer = current_time
            return Shot(self.x + self.width // 2, self.y + self.height, "bullet", direction=1)
        return None

    def special_attack(self):
        # Ataque especial: dispara dos balas a la vez
        current_time = pygame.time.get_ticks()
        if current_time - self.shoot_timer >= 3000:  # Cada 3 segundos
            self.shoot_timer = current_time
            return [
                Shot(self.x + self.width // 4, self.y + self.height, "bullet", direction=1),
                Shot(self.x + 3 * self.width // 4, self.y + self.height, "bullet", direction=1)
            ]
        return []

    def draw(self, screen):
        if not self.is_alive:
            return
        if self.is_star:
            pygame.draw.circle(screen, (255, 255, 0), (self.x + self.width // 2, self.y + self.height // 2), 15)
        else:
            pygame.draw.rect(screen, (255, 0, 255), (self.x, self.y, self.width, self.height))