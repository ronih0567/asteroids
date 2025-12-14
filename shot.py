import pygame
from constants import LINE_WIDTH, SHOT_RADIUS
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, LINE_WIDTH)

    def update(self, dt):
        # Update shot position based on its velocity
        self.position += self.velocity * dt