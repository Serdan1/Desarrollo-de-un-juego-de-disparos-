# player.py
import pygame
from character import Character
from shot import Shot  

class Player(Character):
    def __init__(self, x, y, image):
        super().__init__(x, y, image, lives=3)
        self.score = 0
        self.width = 50
        self.height = 50
        self.speed = 5
        self.respawn_timer = 0

    def move(self):
        # Movimiento del jugador con teclas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < 800 - self.width:
            self.x += self.speed

    def shoot(self):
        # Crea un disparo hacia arriba
        return Shot(self.x + self.width // 2, self.y, "bullet", direction=-1)

    def collide(self, shots):
        if not self.is_alive:
            return
        # Verifica colisiones con disparos enemigos
        for shot in shots:
            if shot.direction == 1:  # Disparos enemigos van hacia abajo
                shot_rect = pygame.Rect(shot.x, shot.y, 10, 10)
                player_rect = pygame.Rect(self.x, self.y, self.width, self.height)
                if shot_rect.colliderect(player_rect):
                    self.lives -= 1
                    if self.lives <= 0:
                        self.is_alive = False
                    else:
                        self.is_alive = False
                        self.respawn_timer = pygame.time.get_ticks()  # Inicia temporizador para renacer
                    shots.remove(shot)
                    break

    def respawn(self):
        # Renace al jugador después de 2 segundos
        if not self.is_alive and self.lives > 0:
            current_time = pygame.time.get_ticks()
            if current_time - self.respawn_timer >= 2000:  # 2 segundos
                self.is_alive = True
                self.x = 400  # Posición inicial
                self.y = 500
                self.respawn_timer = 0

    def draw(self, screen):
        if self.is_alive:
            pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))