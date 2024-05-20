import pygame,sys,random
pygame.init()

window = pygame.display.set_mode((576,704))
pygame.display.set_caption("Tetris - By Ryan Hajj")
clock = pygame.time.Clock()

bg = pygame.image.load("bg.png")
bgRect = bg.get_rect()
blocks = []

### DRAW TEXT ###
def displayText(text,size,where):
    font = pygame.font.Font("Pixel_NES.otf", size)
    words = font.render(text, True, (255,255,255))
    wordsRect = words.get_rect()
    wordsRect.center = where
    window.blit(words, wordsRect)


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
        
### GAME LOOP ###
while True:
    ### EVENT LOOP ###
    for event in pygame.event.get():
        # Exit the program when the Red X is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    ### SCREEN UPDATE ###
    window.fill((0,0,0))
    window.blit(bg,bgRect)
    for block in blocks:
        block.draw()
    displayText("FPS: "+str(int(clock.get_fps())),30,(384+32+32+16,32+16+8))
    clock.tick(60)
    pygame.display.flip()