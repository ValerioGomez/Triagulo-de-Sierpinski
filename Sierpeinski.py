#Importamos las Librerias pygame y sys
import sys
import pygame
#Importamos el modulo de constantes
from pygame.locals import *
#Creamos una Funcion que devuelve el punto medio de la linea
def PuntoMedio(p1, p2):
    #retornamos la tupla promedio del primer punto y segundo en X,Y
    return((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
#Inicializamos el Temporalizador
clock = pygame.time.Clock()
#Iniciamos la Pantalla de 640 x 480 pixeles
screen = pygame.display.set_mode((600, 600))
#Asignamos Nombre a la Pantalla
pygame.display.set_caption('Triángulo de Sierpinki Por Valerio Gomez')
#Yo le pondre icono personalisado con la insignea de la escuela
#creamos una variable icono cargando la imagen
fondo = pygame.image.load("imagen/logo2.png")
icono = pygame.image.load("imagen/logo.png")
#pasamos como parametro la variable icono
pygame.display.set_icon(icono)
#realizamos lo mismo para el fondo
screen.blit(fondo,(10,15))
#Asignamos el Nivel a donde queremos que llegue el triangulo
nivel =5
#Funcion del Bucle Principal
def Triangulo_Sierpinski():
    while 1:
        #Dibujamos el triangulo con las coordenadas halladas (color blanco,P1,P2,P3)
        pygame.draw.polygon(screen, (255,255,255),((100,450),(500,450),(300,104)))
        #declaramos el array con los puntos, para iniciar
        Puntos = [[(100,450),(500,450),(300,104)]]
        #Actualizamos la pantalla
        pygame.display.update()
        #Actualizamos el Reloj a la velocidad por fotograma por 1 milisegundo
        clock.tick(1)
        #Incializamos el Bucle
        for k in range(1,nivel,1):
            #Iniciamos el bucle en el evento de la cola
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            #creamos el array que contendra las lineas nuevas de la pantalla
            array = []
            for Punto_Lado in Puntos:
                #declaramos un array para que se almacenen los nuevos valores
                l = []
                for i in range(0,3,1):
                    #Hallamos Los puntos donde se trazaran los Puntos
                    X = PuntoMedio(Punto_Lado[i-1],Punto_Lado[i])
                    Y = PuntoMedio(Punto_Lado[i],Punto_Lado[(i+1)%3])
                    #Dibujamos la Linea con la tupla (x,y), pasandole un grosor de 2
                    pygame.draw.line(screen,(0,0,0),X,Y,2)
                    #Incrementamos  el nuevo triangulo
                    l = l + [[X,Punto_Lado[i],Y]]
                #Añadimos cada tupla dentro del array
                array = array + l
            #Asignamos los Puntos al Array
            Puntos = array
            #Actualizamos la pantalla para el siguiente nivel
            pygame.display.update()
            #Actualizamos el reloj para el siguiente nivel
            clock.tick(1)
# Si el archivo fuente se ejecuta como el programa principal 
if __name__ == '__main__': 
    #Inicializamos la funcion
    Triangulo_Sierpinski()