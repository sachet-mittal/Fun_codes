import pygame, sys, time
from pygame.locals import *
import random
pygame.init()
# set up the window

WINLENGTH = 612
WINWIDTH = 612
BOXSIZE = 200
GAPSIZE = 4
BOARDWIDTH = 3 # number of columns of icons
BOARDHEIGHT = 3 # number of rows of icons
XMARGIN = 0
YMARGIN = 0
# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

BOARDSTATE = []

Ximg = pygame.image.load('X.bmp')
Oimg = pygame.image.load('0.bmp')
WINNER = None
turn = 0

def setupScreen():
	DISPLAYSURF.fill(WHITE)
	global BOARDSTATE 
	global turn
	turn = 0
	BOARDSTATE = []
	pygame.draw.line(DISPLAYSURF, BLACK, (0, WINWIDTH/3), (WINLENGTH, WINWIDTH/3), 4)
	pygame.draw.line(DISPLAYSURF, BLACK, (0, 2*WINWIDTH/3), (WINLENGTH, 2*WINWIDTH/3), 4)
	pygame.draw.line(DISPLAYSURF, BLACK, (WINLENGTH/3, 0), (WINLENGTH/3, WINLENGTH), 4)
	pygame.draw.line(DISPLAYSURF, BLACK, (2*WINLENGTH/3, 0), (2*WINLENGTH/3, WINLENGTH), 4)
	for i in xrange(BOARDWIDTH):
		column = []
		for j in xrange(BOARDHEIGHT):
			column.append("-1")
		BOARDSTATE.append(column)

def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)
	
def getBoxAtPixel(x, y):

    for boxx in range(BOARDWIDTH):

        for boxy in range(BOARDHEIGHT):

            left, top = leftTopCoordsOfBox(boxx, boxy)

            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)

            if boxRect.collidepoint(x, y):

                return (boxx, boxy)

    return (None, None)

def checkSame(lst):
	return ((lst[1:] == lst[:-1]) and ("-1" not in lst))
	
def hasWon():
	lines = [] # All possible combinations to check for checking winnings
	global WINNER
	# filling horizontal lines
	for i in range(BOARDHEIGHT):
		lines.append(BOARDSTATE[i])

	# filling vertical lines
	for j in range(BOARDWIDTH):
		line =[]
		for i in range(BOARDHEIGHT):
			line.append(BOARDSTATE[i][j])
		lines.append(line)
	
	
	# taking 1st diagonal
	line =[]
	for j in range(BOARDWIDTH):
		line.append(BOARDSTATE[j][j])
	lines.append(line)
	
	# taking 2nd diagonal
	line =[]
	for j in range(BOARDWIDTH):
		line.append(BOARDSTATE[-(j+1)][j])
	lines.append(line)
	for line in lines:
		if ((checkSame(line) == True) and ("-1" not in line)):
			WINNER = line[0]
			return True
	return False
	
DISPLAYSURF = pygame.display.set_mode((WINLENGTH, WINWIDTH), 0, 32)
pygame.display.set_caption('Tic Tac Toe (fatte wala)')

setupScreen()


# fontObj = pygame.font.Font('freesansbold.ttf', 32)
# textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
# textRectObj = textSurfaceObj.get_rect()
# print dir(textRectObj)

# textRectObj.topleft = (WINLENGTH/3, WINWIDTH/3)
# print (textRectObj.x,textRectObj.y)
# DISPLAYSURF.blit(textSurfaceObj, textRectObj)



# pixObj = pygame.PixelArray(DISPLAYSURF)
# pixObj[480][380] = BLACK
# pixObj[482][382] = BLACK
# pixObj[484][384] = BLACK
# pixObj[486][386] = RED
# pixObj[488][388] = BLACK
# del pixObj

fontObj = pygame.font.Font('freesansbold.ttf', 32)
# textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
# textRectObj = textSurfaceObj.get_rect()
# textRectObj.center = (200, 150)
# DISPLAYSURF.blit(textSurfaceObj, textRectObj)

# def chooseMove_intelligent (NodeClass, gnode, maxDepth=6) :
    # "Choose bestMove for gnode along w final value"
    # if gnode.depth < maxDepth and not gnode.over() :
        # for move in gnode.moves :
            # nxtGnode = NodeClass(gnode.board,gnode.player,gnode.depth+1)
            # nxtGnode.move(move)
            # chooseMove(NodeClass, nxtGnode,maxDepth)  # recursion here
            # keep = (gnode.next == None)     # 1st of sequence
            # if gnode.maximizing() :
                # if keep or nxtGnode.value > gnode.value :
                    # gnode.value = nxtGnode.value
                    # gnode.next  = nxtGnode
                    # gnode.bestMove = move
            # else : 
                # if keep or nxtGnode.value < gnode.value :
                    # gnode.value = nxtGnode.value
                    # gnode.next  = nxtGnode
                    # gnode.bestMove = move
    # return gnode

def chooseMove():
	pass
	


# run the game loop
while True:

	for event in pygame.event.get():
		hasWon()
		if WINNER!= None:
			textSurfaceObj = fontObj.render(str(WINNER)+"WON!!!!!!!!!!", True, RED, BLUE)
			textRectObj = textSurfaceObj.get_rect()
			textRectObj.center = (WINLENGTH/2, WINWIDTH/2)
			DISPLAYSURF.blit(textSurfaceObj, textRectObj)
			# pygame.display.update()
			# pygame.event.get()
			# mousex, mousey = event.pos
			# if (mousex >= textRectObj.left and mousex <= textRectObj.right and mousey >= textRectObj.top and mousey <= textRectObj.bottom):
				# print "retry"
				# pygame.quit()
			# setupScreen()
		
		if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
			mousex, mousey = event.pos
			
		elif event.type == MOUSEBUTTONUP:
			mousex, mousey = event.pos
			(boxx,boxy) = getBoxAtPixel(mousex, mousey)
			try:
				if WINNER!= None:
					if (mousex >= textRectObj.left and mousex <= textRectObj.right and mousey >= textRectObj.top and mousey <= textRectObj.bottom):	
						setupScreen()
						
						WINNER = None			
				# elif BOARDSTATE[boxy][boxx] == "-1":
					# if turn%2 == 0:
						# DISPLAYSURF.blit(Ximg, leftTopCoordsOfBox(boxx,boxy))
						# BOARDSTATE[boxy][boxx] = "X"
					# else:
						# print "Getting a move for 0"
						# (boxx,boxy) = (random.randrange(0,2),random.randrange(0,2))
						# print (boxx,boxy)
						# while BOARDSTATE[boxy][boxx] != -1:
							# raw_input()
							# (boxx,boxy) = (random.randrange(0,2),random.randrange(0,2))
							
						# DISPLAYSURF.blit(Oimg, leftTopCoordsOfBox(boxx,boxy))
						# BOARDSTATE[boxy][boxx] = "O"
					
					# turn += 1
				elif BOARDSTATE[boxy][boxx] == "-1":
					DISPLAYSURF.blit(Ximg, leftTopCoordsOfBox(boxx,boxy))
					BOARDSTATE[boxy][boxx] = "X"
					pygame.display.update()
					hasWon()
					# Make a Move for 0
					print BOARDSTATE[boxy][boxx]
					
					while BOARDSTATE[boxy][boxx] != "-1":
						print "Getting a move for 0"
						
						time.sleep(1)
						(boxx,boxy) = (random.randrange(0,3),random.randrange(0,3))
						print (boxx,boxy)
						print BOARDSTATE[boxy][boxx]
					DISPLAYSURF.blit(Oimg, leftTopCoordsOfBox(boxx,boxy))
					BOARDSTATE[boxy][boxx] = "O"

				print BOARDSTATE
			except TypeError:
				print "exception found"
				continue
	pygame.display.update()





