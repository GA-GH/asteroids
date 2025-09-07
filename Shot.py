import pygame
import random
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = PLAYER_SHOT_SPEED
        
    def draw(self, screen):        
        pygame.draw.circle(screen, "red", (self.position.x,self.position.y), self.radius, 1)
        
    def update(self, dt):
        #self.velocity += self.velocity * dt #original
        self.velocity += self.velocity * dt