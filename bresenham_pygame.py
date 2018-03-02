import sys,pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((800,800))
screen.fill((100,100,100))
pygame.display.flip()

white=(255,255,255)

def bresenham(x1,y1,x2,y2):

        #menentukan length atau jarak
        if x1 > x2:
            x,y = x2,y2
            length = x1
        else:
            x,y = x1,y1
            length = x2

        dx = (x2-x1)
        dy = (y2-y1)
        p = 2*(dy-dx)

        gfxdraw.pixel(screen,x,y,white)

        #perloopingan sampai nilai ketemu
        for i in range(length):
            if p < 0:
                x+=1
                p = p+2*dy
                gfxdraw.pixel;(screen,x,y,white)
            else:
                x+= 1
                y+= 1
                p = p+2*(dy-dx)
                gfxdraw.pixel;(screen,x,y,white)
        pygame.display.flip()

bresenham(1,1,4,1.5) #x1,y1,x2,y2

#display pygame
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
