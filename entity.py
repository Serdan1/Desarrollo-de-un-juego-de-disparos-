# entity.py
import pygame

class Entity:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image  # Podría ser una ruta a una imagen, pero usaremos formas simples

    def move(self):
        pass  # Será implementado por las clases derivadas

    def draw(self, screen):
        pass  # Será implementado por las clases derivadas