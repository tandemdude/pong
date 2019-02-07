"""
This is the file for the Ball class.
"""
import math
import random
import pygame

class Ball:
    def __init__(self, start_position):
        self.shape = pygame.Rect(start_position, (10, 10))
        self.colour = pygame.Color("#FFFFFF")
        self.position = [float(start_position[0]), float(start_position[1])]
        self.start_position = [self.position[0], self.position[1]]
        self.velocity = [0.0, 0.0]
        self.speed = 5.0        
        self.collided = False     
        self.create_random_start_vector()

    def reset(self):
        self.position[0] = self.start_position[0]
        self.position[1] = self.start_position[1]
        self.create_random_start_vector()
        self.speed = 5.0

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.shape)

    def update(self, bats, walls):
        self.position[0] += self.velocity[0] * self.speed
        self.position[1] += self.velocity[1] * self.speed

        self.shape.x = int(self.position[0])
        self.shape.y = int(self.position[1])
        
        bat_collided, bat = self.check_bat_collision(bats)
        if bat_collided:
            if not self.collided:
                self.collided = True
                self.velocity[0] = self.velocity[0] * -1  # flip the horizontal velocity to simulate a bat bounce
                self.velocity[1] = -math.sin(self.calculate_bat_bounce_angle(bat))
                self.speed = self.speed * 1.1
        elif self.check_wall_collision(walls):
            if not self.collided:
                self.collided = True
                self.velocity[1] = self.velocity[1] * -1  # flip the vertical velocity to simulate a wall bounce
        else:
            self.collided = False

    def check_bat_collision(self, bats):
        collided = False
        collided_bat = None
        for bat in bats:
            if self.shape.colliderect(bat.shape):
                collided = True
                collided_bat = bat
        return collided, collided_bat

    def check_wall_collision(self, walls):
        collided = False
        for wall in walls:
            if self.shape.colliderect(wall.shape):
                collided = True
        return collided

    def check_should_score(self):
        if self.position[0] < 0.0:
            should_score = True
            self.reset()
            scoring_player = 2
        elif self.position[0] > 800.0:
            should_score = True
            self.reset()
            scoring_player = 1
        else:
            should_score = False
            scoring_player = 0
        return should_score, scoring_player

    def calculate_bat_bounce_angle(self, bat):
        bat_y_centre = bat.shape.y + (bat.shape.height / 2)
        ball_y_centre = self.position[1] + 5
        relative_intersect_y = bat_y_centre - ball_y_centre  # should be in 'bat space' between -50 and +50
        normalized_relative_intersect_y = relative_intersect_y / (bat.shape.height / 2)  # between -1 and 1
        max_bat_bounce_angle = math.pi / 2.4
        bounce_angle = normalized_relative_intersect_y * max_bat_bounce_angle
        return bounce_angle

    def create_random_start_vector(self):
        y_random = random.uniform(-0.5, 0.5)
        x_random = 1.0 - abs(y_random)
        if random.randint(0, 1) == 1:
            x_random = x_random * -1.0
        self.velocity = [x_random, y_random]