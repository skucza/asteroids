import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        velocity_1 = self.velocity.rotate(angle)
        velocity_2 = self.velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid_1.velocity = velocity_1 * 1.2

        asteroid_2 = Asteroid(self.position.x, self.position.y, radius)
        asteroid_2.velocity = velocity_2 * 1.2