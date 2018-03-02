import sys,pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((800,800))
screen.fill((100,100,100))
pygame.display.flip()

white=(255,255,255)

#fungsi pembulatan
def ROUND(n):
	return int(n+0.5)

def dda(x1,y1,x2,y2):
	x,y = x1,y1

        #menentukan length atau jarak
	length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
	dx = (x2-x1)/float(length)
	dy = (y2-y1)/float(length)
	gfxdraw.pixel(screen,ROUND(x),ROUND(y),white)

        #perloopingan penambahan increment sampai ketemu
	for i in range(length):
		x+= dx
		y+= dy
		gfxdraw.pixel(screen,ROUND(x),ROUND(y),white)
	pygame.display.flip()

dda(100,100,200,150) #x1, y1, x2, y2

#memanggil pygame nya
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
