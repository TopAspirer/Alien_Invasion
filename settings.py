## This is the settings class. Each time new functionality is introduced to the game, we'll typically create some new settings as well.
## Instead of writing settings throughout the code, let's write a settings module that contians a class that stores all these values in one place. 
## This makes it easier to modify the game's appearance and behavikour as teh project grows.\


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        
        # Set the backgournd color. 
        # A black screen is boring. Colours in pygame range from 0-225, and are RGB. 
        # (225,0,0) is red, (0,225,0) is green (0,0,225) is blue.
        # Up to 16 million colors can be created.
        self.bg_color = (230,250,250)

        # The ship settings.
        self.ship_speed = 1.5

        # Alien ship settings
        self.alien_speed = 1.0
        # Creating the settings for fleet direction.
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1 

        # The bullet settings. In pixels
        # NOTE You can alter the bullets here for better test of the game.
        # Don't forget to restore the settings though
        self.bullet_speed = 1.0
        self.bullet_width = 3.0
        self.bullet_height = 15
        self.bullet_color = (250,60,60)
        self.bullets_allowed = 3