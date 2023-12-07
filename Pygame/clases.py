import pygame
from pygame.sprite import *
from random import *

from pygame.sprite import _Group
from colores import *

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

class NaveEnemiga(pygame.sprite.Sprite):

    def __init__(self, x, y, escala, velocidad_disparo, cadencia):
        super().__init__()
        #establecimiento del objeto y su imagen
        self.generate = randint(1, 3)
        self.image = pygame.image.load(f"imagenes\\NAVE_ENEMIGO_{str(self.generate)}.png")# imagen de la nave
        #ajuste de tamaño y definicion del hitbox
        ancho = self.image.get_width()
        alto = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(ancho * escala), int(alto * escala)))
        self.rect = self.image.get_rect()
        self.radius = min(self.rect.width, self.rect.height) // 2
        pygame.draw.circle(self.image, BLANCO, self.rect.center, self.radius, 2)
        #generacion
        self.rect.x = randrange(x - self.rect.width)
        self.rect.y = randrange(200 - self.rect.height)
        #aditivos al objeto
        self.velocidad_x = randint(1, 4)
        self.velocidad_y = 0
        #disparo
        self.ultimo_disparo = pygame.time.get_ticks()
        self.cadencia = cadencia
        self.lista_disparos = []
        self.velocidad_disparo = velocidad_disparo

    def movimiento(self, surface: pygame.surface.Surface, nave_enemiga, enemigos_sprites:pygame.sprite.Group, 
                   disparo_enemigo_sprites: pygame.sprite.Group):
        disparo_enemigo_sprites = disparo_enemigo_sprites

        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        if self.rect.right > 750:
            self.velocidad_x -= 2

        if self.rect.left < 0:
            self.velocidad_x += 2

        for x in enemigos_sprites:
            tiempo_enemigo = pygame.time.get_ticks()
            if tiempo_enemigo - x.ultimo_disparo > x.cadencia:
                x_1, y_1 = x.rect.center        

                proyectil = x.disparo(x_1, y_1)

                x.lista_disparos.append(proyectil)

                x.ultimo_disparo = tiempo_enemigo

                disparo_enemigo_sprites.add(proyectil)

        if len(disparo_enemigo_sprites) > 0:
            for x in disparo_enemigo_sprites:
                x.trayectoria()

                x.dibujar(surface)
                if x.rect.top > 640:
                    x.remove()

        return disparo_enemigo_sprites

    def disparo(self, x, y):
        self.proyectil_enemigo = ProyectilEnemigo(x, y,self.velocidad_disparo)

        self.lista_disparos.append(self.proyectil_enemigo)

        return self.proyectil_enemigo

class NaveJugador(pygame.sprite.Sprite):

    def __init__(self, x, y, escala):
        super().__init__()
        self.image = pygame.image.load("imagenes\\NAVE_JUEGO.png")# imagen de la nave
        #ajuste de tamaña y definicion del hitbox
        ancho = self.image.get_width()
        alto = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(ancho * escala), int(alto * escala)))
        self.rect = self.image.get_rect()
        self.radius = min(self.rect.width, self.rect.height) // 2
        pygame.draw.circle(self.image, BLANCO, self.rect.center, self.radius, 2)
        #origen de rect
        self.rect.midbottom = (x, y)
        #adicion de valores a la nave
        self.score = 0
        self.velocidad = 6
        self.vida = 3
        #disparos
        self.lista_disparos = []
        self.cadencia = 800
        self.ultimo_disparo = pygame.time.get_ticks()
        #sonido de salida
        self.sonido_click = pygame.mixer.Sound("sonido\click.mp3")

    def disparo(self, x, y):
        self.proyectil = Proyectil(x, y, 5)

        self.lista_disparos.append(self.proyectil)

        #self.proyectil.sonido.play()
        
        return self.proyectil

    def disparo(self, x, y):
        self.proyectil2 = Proyectil(x, y, 5)

        self.lista_disparos.append(self.proyectil2)

        #self.proyectil2.sonido.play()

        return self.proyectil2

    def movimiento(self, jugador, suma_score: int):
        juego = True

        tecla = pygame.key.get_pressed()

        self.score += suma_score

        if self.rect.x > 0:
            if tecla[pygame.K_a]:
                #self.rect.x -= 5
                self.rect.move_ip(-self.velocidad, 0)

        if self.rect.x < 750:
            if tecla[pygame.K_d]:
                #self.rect.x += 5
                self.rect.move_ip(+self.velocidad, 0)

        if tecla[pygame.K_ESCAPE] == True:
            self.sonido_click.play()
            juego = False

        if len(jugador.lista_disparos) > 0:
            for x in jugador.lista_disparos:
                x.trayectoria()

                if x.rect.bottom < 0:
                    jugador.lista_disparos.remove(x)

        return juego

class Proyectil(pygame.sprite.Sprite):

    def __init__(self, X, Y, velocidad: int):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes\DISPARO_1.png")

        self.rect = self.image.get_rect()

        self.velocidadrect = velocidad

        self.rect.top = Y
        self.rect.left = X

        #self.sonido = pygame.mixer.Sound("sonido\disparo.mp3")

    def trayectoria(self):
        self.rect.top -= self.velocidadrect

class ProyectilEnemigo(pygame.sprite.Sprite):

    def __init__(self, X, Y, velocidad: int):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes\DISPARO_2.png")

        self.rect = self.image.get_rect()

        self.velocidadrect = velocidad

        self.rect.top = Y
        self.rect.left = X

        #self.sonido = pygame.mixer.Sound("sonido\disparo.mp3")

    def trayectoria(self):
        self.rect.y += self.velocidadrect
    
    def dibujar(self, surface: pygame.surface.Surface): 
        surface.blit(self.image, self.rect)

# class Meteorito(pygame.sprite.Sprite):
#     def __init__(self, x, y) -> None:
#         super().__init__()
#         #establecimiento del objeto y su imagen
#         self.generate = randint(1, 3)
#         self.escala = randint(0.5, 1)
#         self.image = pygame.image.load(f"imagenes\\NAVE_ENEMIGO_{str(self.generate)}.png")# imagen de la nave
#         #ajuste de tamaño y definicion del hitbox
#         ancho = self.image.get_width()
#         alto = self.image.get_height()
#         self.image = pygame.transform.scale(self.image, (int(ancho * self.escala), int(alto * self.escala)))
#         self.rect = self.image.get_rect()
#         self.radius = min(self.rect.width, self.rect.height) // 2
#         pygame.draw.circle(self.image, BLANCO, self.rect.center, self.radius, 2)
#         #generacion
#         self.rect.x = randrange(x - self.rect.width)
#         self.rect.y = randrange(200 - self.rect.height)
#         #aditivos al objeto
#         self.velocidad_x = randint(1, 4)
#         self.velocidad_y = 0



