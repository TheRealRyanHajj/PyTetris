import pygame,sys,random
pygame.init()

window = pygame.display.set_mode((576,704))
pygame.display.set_caption("Tetris - By Ryan Hajj")
clock = pygame.time.Clock()
frame = 0

### Class for the blocks ###
# files
filenames = ["blocks/blue.png", "blocks/cyan.png", "blocks/green.png",
"blocks/pink.png", "blocks/purple.png", "blocks/red.png", "blocks/yellow.png"]
#class
class block:
    #init
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
    #draws the block when run
    def draw(self):
        block = pygame.image.load(filenames[self.color])
        window.blit(block,(self.x*32,self.y*32))

bg = pygame.image.load("bg.png")
bgRect = bg.get_rect()
still = []
falling = []

### DRAW TEXT ###
def displayText(text,size,where):
    font = pygame.font.Font("Pixel_NES.otf", size)
    words = font.render(text, True, (255,255,255))
    wordsRect = words.get_rect()
    wordsRect.center = where
    window.blit(words, wordsRect)

### GAME LOOP ###
while True:
    # Add to frame
    frame += 1
    
    ### EVENT LOOP ###
    for event in pygame.event.get():
        # Exit the program when the Red X is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Move Blocks in Falling
    if frame == 30 or frame >= 60:
        xyDict = {}
        for block in still:
            xyDict[block.y] = block.x

        bol = True 
        for block in falling:
            
            for key in xyDict.keys():
                if block.y -1 == key and block == xyDict[key]:
                    bol = False
            if block.y >= 20:
                bol = False
        if bol == True:
            for block in falling:
                block.y += 1
        else:
            for block in falling:
                still.append(block)
                falling.remove(block)
        
        if frame >= 60:
            frame = 0

    ### SCREEN UPDATE ###
    window.fill((0,0,0))
    window.blit(bg,bgRect)
    for block in still:
            block.draw()
    for block in falling:
            block.draw()
    displayText("FPS: "+str(int(clock.get_fps())),30,(464,56))
    clock.tick(60)
    pygame.display.flip()
