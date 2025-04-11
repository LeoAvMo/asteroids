'''
Activate virtual environment commands:
python3 -m venv venv
source venv/bin/activate
'''
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    ## Intro screen
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #Initializing the game
    # Creating groups
    drawable = pygame.sprite.Group() 
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Adding players to groups
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids,updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    backgroundColor = (0,0,0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    # Main loop
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        
        # Update game state
        updatable.update(dt)
        
        for aster in asteroids:
            if aster.collision(player):
                print("Game over!")
                sys.exit()
        
        for aster in asteroids:
            for shot in shots:
                if aster.collision(shot):
                    shot.kill()
                    aster.kill()
                    
        screen.fill(backgroundColor)
        #Draw group that is drawable
        
        # Drawing all objects in the group
        for thing in drawable:
            thing.draw(screen)
    
        
        pygame.display.flip()
        
        dt = clock.tick(60)/1000
        # print(f"Delta Time: {dt}")
        
if __name__ == "__main__":
    main()