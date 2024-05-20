import pygame,sys,random
pygame.init()

window = pygame.display.set_mode((576,704))
clock = pygame.time.Clock()

bg = pygame.image.load("bg.png")
bgRect = bg.get_rect()
blocks = []

### Class for the blocks ###
# files
filenames = ["blocks/blue.png", "blocks/cyan.png", "blocks/green.png", "blocks/pink.png", "blocks/purple.png", "blocks/red.png", "blocks/yellow.png"]
#class
class block:
    #init
    def __init__(self,x,y,color):
        self.x = (x * 32)
        self.y = (y * 32)
        self.color = color
    #draws the block when run
    def draw(self):
        pass
        block = pygame.image.load(filenames[self.color])
        #blockRect = block.get_rect(self.x,self.y)
        window.blit(block,(self.x,self.y))

blocks.append(block(5,20,0))
blocks.append(block(5,19,0))
blocks.append(block(5,18,0))
blocks.append(block(5,17,0))

### GAME LOOP ###
while True:
    ### EVENT LOOP ###
    for event in pygame.event.get():
        # Exit the program when the Red X is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    ### SCREEN UPDATE ###
    window.blit(bg,bgRect)
    for block in blocks:
        block.draw()
    clock.tick(60)
    pygame.display.flip()