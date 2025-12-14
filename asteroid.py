import pygame
from constants import LINE_WIDTH
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Additional initialization for Asteroid can go here

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, LINE_WIDTH)

    def update(self, dt):
        # Update asteroid position based on its velocity
        self.position += self.velocity * dt
        # Add logic for wrapping around screen edges if necessary   