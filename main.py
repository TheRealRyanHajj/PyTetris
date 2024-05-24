import pygame,sys,random
pygame.init()

window = pygame.display.set_mode((576,704))
pygame.display.set_caption("Tetris - By Ryan Hajj")
clock = pygame.time.Clock()
frame = 0
dropFast = False

### Class for the blocks ###
# files
filenames = ["blocks/blue.png", "blocks/cyan.png", "blocks/green.png",
"blocks/pink.png", "blocks/purple.png", "blocks/red.png", "blocks/yellow.png"]
#class
class square:
    #init
    def __init__(self,x,y,color,origin = False):
        self.x = x
        self.y = y
        self.color = color
        self.origin = origin
    #draws the block when run
    def draw(self):
        surface = pygame.image.load(filenames[self.color])
        window.blit(surface,(self.x*32,self.y*32))

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

# get origin
def getOrigin():
    for each in falling:
        if each.origin == True:
            return each.x,each.y
        
# move all peices in falling by x y
def moveAll(point,positive=True):
    x,y = point
    if not positive:
        x,y = (-1 * x),(-1 * y)
    for each in falling:
        each.x += x
        each.y += y

# rotate all in falling around 0,0
def rotateAll(right=True):
    if right:    
        for each in falling:
            x,y = each.x,each.y
            each.x = y*-1
            each.y = x
    else:
        for each in falling:
            x,y = each.x,each.y
            each.x = y
            each.y = x*-1

# collision checker
def checkCollision():
    for each in falling:
        for each2 in still:
            if each.x == each2.x and each.y == each2.y:
                return True
            if each.x > 10 or each.x < 1:
                return True

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
        #inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                for each in falling:
                    each.x += 1
                if checkCollision():
                    for each in falling:
                        each.x -= 1
            if event.key == pygame.K_LEFT:
                for each in falling:
                    each.x -= 1
                if checkCollision():
                    for each in falling:
                        each.x += 1
            if event.key == pygame.K_DOWN:
                dropFast = True
            if (event.key == pygame.K_x or event.key == pygame.K_z) and num != 1:
                ### Rotate peices in falling around block with origin ###
                Origin = getOrigin() # stores as x,y (so a list)
                moveAll(Origin,False)
                if event.key == pygame.K_x:
                    rotateAll()
                elif event.key == pygame.K_z:
                    rotateAll(False)
                moveAll(Origin)
                if checkCollision():
                    Origin = getOrigin() # stores as x,y (so a list)
                    moveAll(Origin,False)
                    if event.key == pygame.K_z:
                        rotateAll()
                    elif event.key == pygame.K_x:
                        rotateAll(False)
                    moveAll(Origin)

                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                dropFast = False
        
    # Move Blocks in Falling
    if frame == 30 or frame >= 60 or dropFast:
        xyDict = {}
        for each in still:
            xyDict[each.y] = each.x

        bol = True 
        for each in falling:
            for each2 in still:
                if each.y + 1 == each2.y and each.x == each2.x:
                    bol = False
            if each.y >= 20:
                bol = False
        if bol == True:
            for each in falling:
                each.y += 1
        else:
            for each in falling:
                still.append(each)
            falling = []
        
        if frame >= 60:
            frame = 0

    # make new blocks
    if frame == 15 or frame == 45:
        if falling == []:
            num = random.randint(1,9)
            col = random.randint(0,6)
            # O block
            if num == 1:
                falling.append(square(5,2,col,True))
                falling.append(square(5,3,col))
                falling.append(square(6,2,col))
                falling.append(square(6,3,col))
            # I block
            if num == 2 or num == 8 or num == 9:
                falling.append(square(5,2,col))
                falling.append(square(5,3,col,True))
                falling.append(square(5,4,col))
                falling.append(square(5,5,col))
            # S block
            if num == 3:
                falling.append(square(4,2,col))
                falling.append(square(5,2,col,True))
                falling.append(square(5,3,col))
                falling.append(square(6,3,col))
            # Z block
            if num == 4:
                falling.append(square(6,2,col))
                falling.append(square(5,2,col))
                falling.append(square(5,3,col,True))
                falling.append(square(4,3,col))
            # T block
            if num == 5:
                falling.append(square(5,2,col))
                falling.append(square(4,3,col))
                falling.append(square(5,3,col,True))
                falling.append(square(6,3,col))
            # L block
            if num == 6:
                falling.append(square(5,2,col))
                falling.append(square(5,3,col))
                falling.append(square(5,4,col,True))
                falling.append(square(6,4,col))
            # J block
            if num == 7:
                falling.append(square(5,2,col))
                falling.append(square(5,3,col))
                falling.append(square(5,4,col,True))
                falling.append(square(4,4,col))

        # line check
        for i in range(20,1,-1):
            num = 0
            for each in still:
                if each.y == i:
                    num += 1
                if num == 10:
                    stillRemove = []
                    for each2 in still:
                        if each2.y == i:
                            stillRemove.append(each2)
                        if each2.y < i:
                            each2.y += 1
                    for each in stillRemove:
                        still.remove(each)

    ### SCREEN UPDATE ###
    window.fill((0,0,0))
    window.blit(bg,bgRect)
    for each in still:
            each.draw()
    for each in falling:
            each.draw()
    displayText("FPS: "+str(int(clock.get_fps())),30,(464,56))
    clock.tick(60)
    pygame.display.flip()
