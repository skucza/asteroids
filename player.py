import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        # print(f"Player triangle [{a}{b}{c}]")

        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)

    def rotate_left(self, dt):
        self.rotation -= dt * PLAYER_TURN_SPEED

    def rotate_right(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def move_forward(self, dt):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * PLAYER_SPEED * dt

    def move_backward(self, dt):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position -= direction * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move_forward(dt)

        if keys[pygame.K_s]:
            self.move_backward(dt)

        if keys[pygame.K_a]:
            self.rotate_left(dt)

        if keys[pygame.K_d]:
            self.rotate_right(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = direction * PLAYER_SHOOT_SPEED


