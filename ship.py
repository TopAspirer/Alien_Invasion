## This is the ship module that will display the ship.

import pygame

## One of my goals is to be able to use different ships in this game. 
class Ship:
    """A class to manage a ship."""
    def __init__ (self, ai_game):
        """Initialize the ship and set its position."""
        self.screen = ai_game.screen
        # Here we access the ship's rect attribute. It allows the ship to be placed in the correct on screen location.
        self.screen_rect = ai_game.screen.get_rect()    
        self.settings = ai_game.settings

        # Load the ship image and get its rectangle. In pygame, the objects are set as recatangles, that have 'boundaries'.
        self.image = pygame.image.load('images\ship_02.bmp')  # We call pygame and load the image of the ship of our ship image.
        self.rect = self.image.get_rect()  

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False 
        self.moving_down = False

        # Storing a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)    

    def update(self):
        """Update the ship's position based on movement flags.
        This has been modified to limit the ship's range. No disappearing off the edges.
        """
        # Updating the ship's x value and not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x 
        self.rect.x = self.x
