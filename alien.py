## Like the ship module, this module will manage the behaviours of the aliens

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set it's position."""
        super().__init__()
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.screen = ai_game.screen

        # Load the alien image and set it's rect attribute.
        self.image = pygame.image.load('images/alien_minion.bmp')
        self.rect = self.image.get_rect()
        

        # Setting the position of the alien at the top of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact horizontal position
        self.x = float(self.rect.x)





