 def _create_alien_fleet(self):
        """Creates a fleet of aliens."""
        # Make an alien.
        # Spacing betwen each alien is equal to one alien width.

        alien = Alien(self)                 # An instance of an alien is created here.
        self.aliens.add(alien)              # The instance is then appended to the group aliens that was initialized in  __init__().

        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_on_x = available_space_x // (2 *alien_width)
        print(number_aliens_on_x)
        print(available_space_x)