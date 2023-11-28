import pygame, sonido, imagenes
from sonido import *
from imagenes import *
# establecimiento de objeto boton
class Botton():
    def __init__(self, x, y, imagen, escala):
        #obtiene el valor del rectangulo del boton
        ancho = imagen.get_width()
        alto = imagen.get_height()
        self.imagen = pygame.transform.scale(imagen, (int(ancho * escala), int(alto * escala)))
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.topleft = (x, y) 
        self.press = False
        self.sonido_click = pygame.mixer.Sound("sonido\click.mp3")

    def dibujar(self, superficie):
        accion = False
        #obtener pocision del mouse

        posicion = pygame.mouse.get_pos()

        if self.rectangulo.collidepoint(posicion):
            if pygame.mouse.get_pressed()[0] == 1 and self.press == False:
                self.sonido_click.play()
                self.press = True
                accion = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.press = False

        # dibujado del boton en la pantalla
        superficie.blit(self.imagen, (self.rectangulo.x, self.rectangulo.y))

        return accion




class naveEspacial(pygame.sprite.Sprite):

    def __init__(self, x, y, escala):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave = pygame.image.load("imagenes\\NAVE_JUEGO.png")# imagen de la nave
        #ajuste de tamaña y definicion del hitbox
        ancho = self.imagenNave.get_width()
        alto = self.imagenNave.get_height()
        self.imagenNave = pygame.transform.scale(self.imagenNave, (int(ancho * escala), int(alto * escala)))
        self.rectangulo = self.imagenNave.get_rect()
        #origen de rectangulo
        self.rectangulo.midbottom = (x, y)
        #adicion de valores a la nave
        self.lista_disparos = []
        self.vida = True
        # sonido de salida
        self.sonido_click = pygame.mixer.Sound("sonido\click.mp3")


    def dispara():
        pass
        
    def movimiento(self):
        juego = True

        tecla = pygame.key.get_pressed()

        if self.rectangulo.x > -3:
            if tecla[pygame.K_a]:
                #tecla_press = False
                #self.rectangulo.x -= 5
                self.rectangulo.move_ip(-6, 0)
        
        if self.rectangulo.x < 750:
            if tecla[pygame.K_d]:
                #tecla_press = False
                #self.rectangulo.x += 5
                self.rectangulo.move_ip(+6, 0)

        if tecla[pygame.K_ESCAPE] == True:
            self.sonido_click.play()
            juego = False

        return juego


    def dibujar(self, surface):
        surface.blit(self.imagenNave, self.rectangulo)

