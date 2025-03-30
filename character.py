# character.py
from entity import Entity

class Character(Entity):
    def __init__(self, x, y, image, lives):
        super().__init__(x, y, image)
        self.lives = lives
        self.is_alive = True

    def move(self):
        pass  # Será implementado por las clases derivadas

    def shoot(self):
        pass  # Será implementado por las clases derivadas

    def collide(self, shots):
        pass  # Será implementado por las clases derivadas