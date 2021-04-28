import sys

import pygame

class AlienInvasion:
    """Initialize the game assets and behaviour."""

    def __init__(self):
        """Initilize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.dispay.set_mode(1200,800))
        pygame.display.set_caption("Allien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #watch for keyboard and mouse events.
            for events in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #make the most recently drawn screen visible.
            pygame.display.flip()
if __name__ == '__main__':
    #make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()