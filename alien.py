## Like the ship module, this module will manage the behaviours of the aliens

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set it's position."""
        super().__init__()
        self.screen_rect = ai_game.screen.get_rect()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set it's rect attribute.
        self.image = pygame.image.load('images/alien_minion.bmp')
        self.rect = self.image.get_rect()
        

        # Setting the position of the alien at the top of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Movet he alien to the right."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Returns true if an alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            return True







