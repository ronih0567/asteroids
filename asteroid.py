import pygame
import random
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
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
        
    def split(self):
        # Logic to split the asteroid into smaller asteroids
        self.kill()  # Remove the current asteroid from the game
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Do not split if the asteroid is too small
        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(20, 50)
            
            # Create two smaller asteroids
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = self.velocity.rotate(rand_angle) * 1.2
            asteroid2.velocity = self.velocity.rotate(-rand_angle) * 1.2
            
          