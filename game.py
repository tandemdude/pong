"""
This is the file for the game class and the file to run to play the game
"""
import pygame
from wall import Wall
from bat import Bat, ControlScheme
from ball import Ball
from score import Score


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("My Pong Game")
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.clock = pygame.time.Clock()
        self.walls = [Wall((10, 10), 780, 10), Wall((10, 580), 780, 10)]
        control_scheme_1 = ControlScheme()
        control_scheme_1.up = pygame.K_w
        control_scheme_1.down = pygame.K_s
        control_scheme_2 = ControlScheme()
        control_scheme_2.up = pygame.K_UP
        control_scheme_2.down = pygame.K_DOWN
        self.bats = [Bat((10, 200), 10, 100, control_scheme_1), Bat((780, 200), 10, 100, control_scheme_2)]
        self.background = pygame.Surface((800, 600))
        self.background.fill(pygame.Color("#000000"))
        self.ball = Ball((400, 300))
        self.font = pygame.font.Font(None, 50) 
        self.score = Score(self.font)

    def run(self):
        while self.running:
            self.screen.blit(self.background, (0, 0))
            self.clock.tick(90)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                for bat in self.bats:
                    bat.handle_input(event)

            for wall in self.walls:
                wall.draw(self.screen)

            for bat in self.bats:
                bat.update()
                bat.draw(self.screen)

            self.ball.update(self.bats, self.walls)
            self.ball.draw(self.screen) 

            should_score, scoring_player = self.ball.check_should_score()
            if should_score:
                self.score.increase_player_score(scoring_player)

            self.score.draw(self.screen)

            pygame.display.flip()

        pygame.quit()


game = Game()
game.run()