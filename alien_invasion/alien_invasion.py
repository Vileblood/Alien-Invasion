import sys  

import pygame    

from settings import Settings
from ship import Ship


class AlienInvasion:    
    """ overall class to manage game assets and behaviour """

    def __init__(self):
        """ Initialise the game, and create game resources """
        pygame.init()
        self.settings = Settings() 

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 


        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # set background colour
        self.bg_color = (230, 230, 230)


def run_game(self):
    """ Start main loop for game """
    
    while True:
            self._check_events()
            self._update_screen()


    def _check_events(self): 
        # watch for keyboard and mouse events.       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right.
                    self.ship.rect.x += 1
                        

    def _update_screen(self):
    # redraw the screen during each pass of the loop (start a new game)
        self.screen.fill(self.settings.bg_color)   
        self.ship.blitme()     



    # make the most recently drawn screen visible.
        pygame.display.flip()



if __name__ == '__main__':
    # make game instance and run game.
    ai = AlienInvasion()
    ai.run_game()


