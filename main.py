import pygame,sys,random
pygame.init()

window = pygame.display.set_mode((576,704))
clock = pygame.time.Clock()

Filenames = ["blocks/blue.png", "blocks/cyan.png", "blocks/green.png", "blocks/pink.png", "blocks/purple.png", "blocks/red.png", "blocks/yellow.png"]
bg = pygame.image.load("bg.png")
bgRect = bg.get_rect()

class block:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self):
        pass

while True:
    for event in pygame.event.get():
        # Exit the program when the Red X is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    window.blit(bg,bgRect)
    clock.tick(60)
    pygame.display.flip()