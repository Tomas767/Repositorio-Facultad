# import pygame, sys, colores
# from pygame.locals import *
# from colores import *
# from clases import *
# from source import *
# pygame.init()

# TAMAÑO_PANTALLA = (800, 640)

# # pantalla de juego y su resulocion en pixeles
# PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)

# # renderizado de actualizacion de la pantalla
# tiempo_juego = pygame.time.Clock()
# fps = 40

# # icono y pantalla
# icono_ = pygame.image.load("imagenes\ICONO.png")
# pygame.display.set_caption("GALAXY")
# pygame.display.set_icon(icono_)

# # establesco la fuente de texto del menu
# fuente_origen = "fuente\ARCADECLASSIC.TTF"
# fuente = pygame.font.SysFont("fuente\ARCADECLASSIC.TTF", 30)
# fondo_juego__ = pygame.image.load("imagenes\FONDO_JUEGO.png")
# correr_juego = True
# comenzar_menu = False

# #ugador = naveEspacial(400, 600)

# #spygame.draw.rect(PANTALLA, BLANCO,(200, 300, 100, 200))

# while correr_juego:
#     tiempo_juego.tick(fps)

#     PANTALLA.fill(NEGRO)

#     pygame.draw.rect(PANTALLA, BLANCO,(150, 250, 150, 80))
#     pygame.draw.rect(PANTALLA, BLANCO,(450, 250, 20, 30))

#     img = fuente.render("MENU", True, BLANCO, O0033CC)

#     PANTALLA.blit(img, (0, 0))
#     #Galaxy(PANTALLA, fondo_juego__, jugador)

#     for event in pygame.event.get():
#         if event.type == QUIT:

#             pygame.quit()

#             sys.exit()

#     pygame.display.update()

import random
cont = 0
while True:
    for y in range(6):
        generat = random.randint(1,3)
        print(generat)
        cont += 1
    break
