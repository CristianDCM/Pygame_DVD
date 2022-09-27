import pygame
#Definicion de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#Inicializacion de pygame
pygame.init()
#Crear ventana
screen = pygame.display.set_mode((800, 600))
#Control de FPS
clock = pygame.time.Clock()
#Cordenas
cord_x = 50
cord_y = 50
#Velocidad
vel_x = 6
vel_y = 6
#Titulo e icono
pygame.display.set_caption("DVD")
icon = pygame.image.load('ico.png')
pygame.display.set_icon(icon)
#Bucle de ejecucion // Cierre de ventana
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    #Salida de pantalla X y Y
    if cord_x > 750 or cord_x < 0:
        vel_x = -vel_x
    if cord_y > 550 or cord_y < 0:
        vel_y = -vel_y
    #Animacion X y Y
    cord_x += vel_x
    cord_y += vel_y
    #Rellenar pantalla de color Blanco
    screen.fill(WHITE)
    #Zona de Dibujo // Dibujo cuadrado // DVD
    dvd = pygame.image.load('DVD.png')
    dvd = pygame.transform.scale(dvd, (80, 80))
    screen.blit(dvd, (cord_x, cord_y))
    #pygame.draw.rect(screen, RED, [cord_x, cord_y, 50, 50])
    #Actualizar pantalla
    pygame.display.update()
    #FPS
    clock.tick(60)