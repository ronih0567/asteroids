import pygame
from constants import *
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    flag = True
    while flag == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
        
        # Game logic and rendering would go here
        
        # Example call to log_state (assuming game_objects and screen_size are defined)
        # log_state(game_objects, (SCREEN_WIDTH, SCREEN_HEIGHT))
        log_state()
        screen.fill("black")      
        
        pygame.display.flip()


if __name__ == "__main__":
    main()
