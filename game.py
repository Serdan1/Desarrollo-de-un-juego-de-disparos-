# game.py
import pygame
from player import Player
from opponent import Opponent
from boss import Boss

class Game:
    def __init__(self):
        self.score = 0
        self.player = Player(400, 500, "player")
        self.opponents = [Opponent(x, 50, "opponent") for x in range(100, 700, 100)]  # Múltiples enemigos
        self.boss = None
        self.is_running = False
        self.shots = []  # Lista para almacenar todos los disparos
        self.font = pygame.font.SysFont(None, 36)

    def start(self):
        self.is_running = True

    def update(self, screen):
        if not self.is_running:
            return

        # Actualizar el jugador
        self.player.move()
        self.player.respawn()
        if self.player.is_alive:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                shot = self.player.shoot()
                if shot:
                    self.shots.append(shot)

        # Actualizar enemigos o jefe
        if self.boss:
            # Si hay un jefe, actualizar solo al jefe
            self.boss.move()
            shot = self.boss.shoot()
            if shot:
                self.shots.append(shot)
            special_shots = self.boss.special_attack()
            self.shots.extend(special_shots)
            # Verificar colisiones con el jefe
            if self.boss.collide(self.shots):
                self.score += 1
                if not self.boss.is_alive:
                    self.end_game(True)
        else:
            # Si no hay jefe, actualizar enemigos
            all_defeated = True
            for opponent in self.opponents:
                if not opponent.is_star:
                    all_defeated = False
                    opponent.move()
                    shot = opponent.shoot()
                    if shot:
                        self.shots.append(shot)
                    # Verificar colisiones con el enemigo
                    if opponent.collide(self.shots):
                        self.score += 1
            if all_defeated and not self.boss:
                self.remove_opponents()

        # Actualizar disparos
        for shot in self.shots[:]:
            if not shot.move():
                self.shots.remove(shot)

        # Verificar colisiones con el jugador
        self.player.collide(self.shots)
        if not self.player.is_alive and self.player.lives <= 0:
            self.end_game(False)

        # Dibujar todo
        screen.fill((0, 0, 0))
        self.player.draw(screen)
        if self.boss:
            self.boss.draw(screen)
        else:
            for opponent in self.opponents:
                opponent.draw(screen)
        for shot in self.shots:
            shot.draw(screen)
        self.draw_hud(screen)

    def remove_opponents(self):
        # Reemplazar enemigos por el jefe
        self.opponents = []
        self.boss = Boss(400, 50, "boss")

    def draw_hud(self, screen):
        # Mostrar puntuación y vidas
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        lives_text = self.font.render(f"Lives: {self.player.lives}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))

    def end_game(self, victory):
        self.is_running = False
        if victory:
            print("¡Ganaste! Derrotaste al jefe.")
        else:
            print("Game Over. Perdiste todas tus vidas.")