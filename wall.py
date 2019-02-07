# Wall class file
# - Draws walls
import pygame


class Wall:
	def __init__(self, top_left_corner, width, height):
		self.shape = pygame.Rect(top_left_corner, (width, height))
		self.colour = pygame.Color("#AAAAAA")

	def draw(self, screen):
		pygame.draw.rect(screen, self.colour, self.shape)