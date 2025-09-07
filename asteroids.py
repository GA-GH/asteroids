import pygame
from circleshape import CircleShape
import random

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):        
        pygame.draw.circle(screen, "white", (random.randint(10, 1250),random.randint(10, 700)), self.radius, 2)
        
    def update(self, dt):
        #self.velocity += self.velocity * dt #original
        self.velocity += ((self.velocity * dt) /900)