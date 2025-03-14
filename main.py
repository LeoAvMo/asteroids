# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    ## Intro screen
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #Initializing the game
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    backgroundColor = (0,0,0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(backgroundColor)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        print(f"Delta Time: {dt}")
        
if __name__ == "__main__":
    main()