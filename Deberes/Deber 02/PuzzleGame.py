import pygame
from PIL import Image
import numpy as np
import random
import time
import webbrowser
import easygui
file_path = easygui.fileopenbox()
myvar = easygui.enterbox("Ingrese en nivel de dificultad. (Desde 3 hasta N)")
def cargarImagen(arr):
	global pantalla, inicial
	pantalla = []
	for pieza in arr:
		img = Image.fromarray(np.uint8(pieza))
		mode = img.mode
		size = img.size
		data = img.tobytes()
		pantalla.append(pygame.image.fromstring(data,size,mode))
	inicial = pantalla
def getvacio():
	x = 0
	for pieza in pantalla:
		if pieza == vac:
			break
		x = x + 1
	return x	
def estadoInicial():
	columna = 0
	x = 0
	y = 0
	pantalla[vacio].fill((0,0,0,0))
	global vac
	vac = pantalla[vacio]
	for pieza in pantalla:
		ventana.blit(pieza,(x,y))
		x = x + A
		columna = columna + 1
		if (columna==N):
			y = y + H
			columna = 0
			x = 0
	pygame.display.flip()
	#pygame.image.save(ventana, 'estadoinicial.png')
	time.sleep(5)
def putImages():
	columna = 0
	x = 0
	y = 0
	for pieza in pantalla:
		ventana.blit(pieza,(x,y))
		x = x + A
		columna = columna + 1
		if (columna==N):
			y = y + H
			columna = 0
			x = 0
	pygame.display.flip()
def switchImages(pos):
	x= pos[0]
	y = pos[1]
	saltox = A #256
	saltoy = H #124
	item = 0
	while True:
		if x < saltox:
			if y < saltoy:
				break
			else:
				saltoy = saltoy + H
				item = item + N
		else:
			saltox = saltox + A
			item = item + 1
	swapantalla(item)
def swapantalla(item):
	aux1 = pantalla[item]
	posvac = getvacio()
	pantalla[item] = vac
	pantalla[posvac] = aux1
	putImages()
	compare()
def compare():
	#pygame.image.save(ventana, 'estadofinal.png')
	if(pantalla == init):
		choice = easygui.ynbox('Ha Ganado!\n¿Desea reclamar su premio ahora?', 'Felicitaciones!', ('Sí', 'Sí'))
pygame.init()
N=int(myvar)
image = Image.open(str(file_path))
originalArray = np.asarray(image)
originalIm = Image.fromarray(np.uint8(originalArray))
widthIm,heightIm = image.size
ventana = pygame.display.set_mode(image.size)
pygame.display.set_caption("Puzzle")
H = heightIm//N
A = widthIm//N
piezasad = []
for y in range(0,heightIm,H):
	for x in range(0,widthIm,A):
		fract = originalArray[y:y+H,x:x+A]
		piezasad.append(fract)
numero = N ** 2
piezas = piezasad[:numero]
normal = piezas
vacio = random.randint(0,(N**2)-1)
cargarImagen(piezas)
estadoInicial()
init = list(pantalla)
random.shuffle(pantalla)
putImages()
inicio = True
while inicio:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			inicio = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				pos = pygame.mouse.get_pos()
				switchImages(pos)
pygame.quit()
