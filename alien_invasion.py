import sys
import pygame
from explainer import Explainer

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

        # Intitialize the explianing module.
        self.explain = Explainer()
        
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
            self._update_aliens()            
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
            if event.key == pygame.K_ESCAPE:
                sys.exit

            elif event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                 self.ship.moving_left = True 

            # Checking to see if a bullet is fired.
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()
            
           
    def _check_keyup_events(self,event):
        """This is a helper method to _check_events_().
           It respondes to all keyup events.
        """
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False 



    def _update_bullets(self):
        """Create a new bullet and add it to the bullets group.
           Destroys previous bullets when fleet is destoroyed.
        """
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0: 
                self.bullets.remove(bullet)
        self._check_alien_bullet_collisions()

    def _check_alien_bullet_collisions(self):
        """Responsible for dealing with alien & bullet collisions.
            Check's if the alien group is empty. 
            If True, empty the group of bullets and create a new fleet.
            This function is called in _update_bullets()
        """
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        self.explain.explain_collisions
        if not self.aliens:
            # We check whether the alien group is empty. If so, delete all the bullets and create a new fleet
            self.bullets.empty()
            self._create_alien_fleet()
        
                  

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group.
           Checking how many bullets exist before creating a new bullet.
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


        
    def _create_alien(self, alien_number, row_number):
        """Creates the aliens.
           Refactored to handle the creation of the aliens that will be put into the fleet.
        """
        alien = Alien(self)                                 
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width + 2  * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)                             
            
    def _create_alien_fleet(self):
        """Creates a fleet of aliens."""
      
        # Spacing betwen each alien is equal to one alien width.
        alien = Alien(self)                 
        self.aliens.add(alien)              
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_on_x = available_space_x // (2 *alien_width)

        # Determine the number of rows of aliens that fit the screen. 
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height-(3 * alien_height)-ship_height)
        number_rows = available_space_y // (2 * alien_height)

        
        # Create full fleet of aliens. Python uses the code for creating one row and repeats it number_rows times.
        for row_number in range(number_rows):
            # Creates the aliens in a row.
            for alien_number in range(number_aliens_on_x):
                self._create_alien(alien_number,row_number)
    


    def _check_fleet_edges(self):
        """Respondes immediately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1



    def _update_aliens(self):
        """Check if the fleet is at the edge,
        then update the positions of all aliens in the fleet."""
        # _check_fleet_edges is called before updating each alien's positions.
        self._check_fleet_edges()
        self.aliens.update()



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


