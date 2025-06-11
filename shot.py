import pygame
from circleshape import CircleShape
from constants import WHITE


class Shot(CircleShape):
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt