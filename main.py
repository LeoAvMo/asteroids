# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    ## Intro screen
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #Initializing the game
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
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
        player.update(dt)
        
        screen.fill(backgroundColor)
        player.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60)/1000
        print(f"Delta Time: {dt}")
        
if __name__ == "__main__":
    main()