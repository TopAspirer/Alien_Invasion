import sys
import pygame

# To create an instance of settings in the project.
from settings import Settings
from ship import Ship 
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.display.set_caption("Alien Invasion")
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.bg_color = (self.settings.bg_color)     
        self.ship = Ship(self)

        # An instance of a group of aliens is created 
        self.aliens = pygame.sprite.Group()
        self._create_alien_fleet()  


        # Storing bullets in a group. 
        # This code will store all the live bullets so we can manage the bullets that have been fired.
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start at the main loop for the game."""
        while True:
            # The two lines of code below have been refactored. 
            self.ship.update()
            self._check_events()
            self.bullets.update()     # if you want the bullets to travel slower delete this line. Basically, .update() is called twice so the bullets travel faster.
            self._update_bullets()             
            self._update_screen()
            
            

    # This method checks for keyboard and mouse events. It is a helper and runs in the run_game(self)' method
    def _check_events(self):
        """Checks for key events and mouse events.
           A refractered method for run_game().
           This structure makes futher developments of player inputs simpler.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            # When the player pushes down on Movement Keys
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)              
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)

                           
    def _check_keydown_events(self, event):
        """This is a helper method to _check_events_().
           It responseds to all keydown events.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            if event.key == pygame.K_LEFT:
                 self.ship.moving_left = True 

            # Checking to see if a bullet is fired.
            if event.key == pygame.K_SPACE:
                self._fire_bullet()
            
           
            if event.key == pygame.K_ESCAPE:
                sys.exit
            
    def _update_bullets(self):
        """Create a new bullet and add it to the bullets group."""
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0: 
                self.bullets.remove(bullet)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group.
           Checking how many bullets exist before creating a new bullet.
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self,event):
        """This is a helper method to _check_events_().
           It respondes to all keyup events.
        """
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = False 


    def _create_alien_fleet(self):
        """Creates a fleet of aliens."""
        # Make an alien.
        # Spacing betwen each alien is equal to one alien width.

        alien = Alien(self)                 # An instance of an alien is created here.
        self.aliens.add(alien)              # The instance is then appended to the group aliens that was initialized in  __init__().

        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_on_x = available_space_x // (2 *alien_width)
        
        # Create the first row of alien fleet.
        for alien_index in range(number_aliens_on_x):
            alien = Alien(self)
            alien.x = alien_width + 2  * alien_width * alien_index
            alien.rect.x = alien.x
            self.aliens.add(alien)

        # Left of here on 12/12/2024
    def _create_aliens(self):
        """Creates the aliens.
           Refactored to handle the creation of the aliens that will be put into the fleet.
        """
            

    def _update_screen(self):
        # This is a helper method/function that runs in 'def run_game(self)'
        """Update images on the screen, and flip to the new screen.
           Must stay below all functions in the run_game() while loop.        
        """
        self.screen.fill(self.settings.bg_color)       

        # Drawing the bullet.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)
        self.ship.blitme()
        # This line makes the most recently drawing on the screen visible. Always keep at bottom of the _update_screen() method! 
        pygame.display.flip()

        
if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


