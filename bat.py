"""
This is the file for our Bat class. The bats are the two moving rectangles either side of the screen that are controlled
by the players.
"""
import pygame

class Bat:
    def __init__(self, top_left_corner, width, height, control_scheme):
        self.shape = pygame.Rect(top_left_corner, (width, height))
        self.colour = pygame.Color("#AAAAAA")
        self.control_scheme = control_scheme
        self.move_up = False
        self.move_down = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.shape)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.control_scheme.up:
                self.move_up = True
            if event.key == self.control_scheme.down:
                self.move_down = True
        if event.type == pygame.KEYUP:
            if event.key == self.control_scheme.up:
                self.move_up = False
            if event.key == self.control_scheme.down:
                self.move_down = False

    def update(self):
        if self.move_up:
            self.shape.y -= 5

            if self.shape.y < 20:
                self.shape.y = 20

        if self.move_down:
            self.shape.y += 5

            if self.shape.y > 480:
                self.shape.y = 480


class ControlScheme:
    def __init__(self):
        self.up = pygame.K_UP
        self.down = pygame.K_DOWN