import pygame
from player import Player
from constants import *
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    pygame.time.Clock()
    dt = 0
    
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    
    flag = True
    while flag == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # flag = False
                return
        
        # Game logic and rendering go here
        
        log_state()
        screen.fill("black") 
        player.update(dt) 
        player.draw(screen)    
        
        pygame.display.flip()
        dt = pygame.time.Clock().tick(60)/1000  # Limit to 60 FPS
        # print(f"dt: {dt}")


if __name__ == "__main__":
    main()
