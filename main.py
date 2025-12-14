import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from logger import log_state, log_event

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    
    asteroid_field = AsteroidField()
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
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
                flag = False
        for object in drawable: 
            object.draw(screen)
        player.draw(screen)    
        
        pygame.display.flip()
        dt = pygame.time.Clock().tick(60)/1000  # Limit to 60 FPS
        # print(f"dt: {dt}")


if __name__ == "__main__":
    main()
