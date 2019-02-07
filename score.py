# File for score class
# - Increases player score 
# - Draws scores
import pygame


class Score:
    def __init__(self, font):
        self.player_scores = [0, 0]
        self.font = font
        self.score_text_render = None
        self.update_score_text()

    def update_score_text(self):
        score_string = str(self.player_scores[0]) + " - " + str(self.player_scores[1])
        self.score_text_render = self.font.render(score_string, True, pygame.Color("#CCCCCC"))

    def draw(self, screen):
        screen.blit(self.score_text_render, self.score_text_render.get_rect(centerx=400, centery=50))

    def increase_player_score(self, player):
        self.player_scores[player-1] += 1
        self.update_score_text() 