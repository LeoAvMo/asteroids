import pygame

#Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y ,radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        # Set iniria position, velocity and radius
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius
        
    # Subclasses will override this methods
    def draw(self, screen):
        pass
    
    def update(self, dt):
        pass