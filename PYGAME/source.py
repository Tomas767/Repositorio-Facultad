import pygame, sys, clases
from colores import *
from clases import *
from pygame.locals import *

def dibujado_de_texto(PANTALLA: pygame.surface.Surface, texto: str, fuente: pygame.font.Font, color_del_texto, color_fondo, x, y, marco = False):
    img = fuente.render(texto, True, color_del_texto, color_fondo)

    PANTALLA.blit(img, (x, y))

def iniciar__juego__():
    TAMAÑO_PANTALLA = (800, 640)

    # pantalla de juego y su resulocion en pixeles
    PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)

    # renderizado de actualizacion de la pantalla
    tiempo_juego = pygame.USEREVENT + 0
    pygame.time.set_timer(tiempo_juego,40)

    # icono y pantalla
    icono = pygame.image.load("imagenes/ICONO.png")
    pygame.display.set_caption("GALAXY")
    pygame.display.set_icon(icono)

    menu_principal(PANTALLA, tiempo_juego)

def menu_principal(PANTALLA: pygame.surface.Surface, tiempo_juego: int):
    # banderas de acceso o seguimiento del juego
    correr_juego = True    

    niveles = False

    juego = False

    opciones = False

    # imagenes y botones
    start__ = pygame.image.load("imagenes\START.png").convert_alpha()
    exit__ = pygame.image.load("imagenes\SALIR.png").convert_alpha()
    opciones__ = pygame.image.load("imagenes\OPCIONES.png").convert_alpha()
    back__ = pygame.image.load("imagenes\ATRAS.png").convert_alpha()
    nivel_I = pygame.image.load("imagenes\\1.png").convert_alpha()
    nivel_II = pygame.image.load("imagenes\\2.png").convert_alpha()
    nivel_III = pygame.image.load("imagenes\\3.png").convert_alpha()
    volumen1__ = pygame.image.load("imagenes\VOLUMEN+.png").convert_alpha()
    volumen2__ = pygame.image.load("imagenes\VOLUMEN-.png").convert_alpha()

    fondo__ = pygame.image.load("imagenes\FONDO.png")
    fondo_juego__ = pygame.image.load("imagenes\\FONDO_JUEGO.png")

    try:
        titulo__ = pygame.image.load("imagenes\MENU PRINCIPAL.png")

    except FileNotFoundError:
    # establesco la fuente de texto del menu
        fuente_origen = "fuente\ARCADECLASSIC.TTF"
        fuente = pygame.font.Font(fuente_origen, 30)
        fuente_titulos = pygame.font.Font(fuente_origen, 70)

    titulo2__ = pygame.image.load("imagenes\MENU_NIVELES.png")
    titulo__opciones = pygame.image.load("imagenes\OPCIONES_TITULO.png")

    # jugador
    player__ = naveEspacial(400, 640, 0.5)

    # creando el boton a base de la clase
    start__boton = Botton(300, 220, start__, 0.9)
    exit__botton = Botton(300, 460, exit__, 0.9)
    opciones__botton = Botton(300, 340, opciones__, 0.9)

    nivel_I_botton = Botton(670, 380, nivel_I, 0.8)
    nivel_II_botton = Botton(670, 470, nivel_II, 0.8)
    nivel_III_botton= Botton(670, 560, nivel_III, 0.8)
    back__botton = Botton(40, 540, back__, 0.9)

    volumen1__botton = Botton(180, 300, volumen1__, 0.9)
    volumen2__botton = Botton(470, 300, volumen2__, 0.9)
    
    #establecer sonidos de menu
    pygame.mixer.music.load("sonido\introfondo.mp3")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)

    while correr_juego:
        eventos = pygame.event.get()
        
        if not juego:
            if not niveles and not opciones:
                PANTALLA.blit(fondo__, (0,0)) # lleno el fondo del menu

                try:
                    PANTALLA.blit(titulo__, (100, 40, 0, 0)) #coloco la imagen del titulo
                except UnboundLocalError:
                    dibujado_de_texto(PANTALLA," MENU PRINCIPAL ", fuente_titulos,BLANCO ,O0033CC, 100, 40, True)

                if start__boton.dibujar(PANTALLA):
                    niveles = True

                if opciones__botton.dibujar(PANTALLA):
                    opciones = True

                if exit__botton.dibujar(PANTALLA):
                    correr_juego = False

            if niveles and not opciones:
                PANTALLA.blit(fondo__, (0, 0))

                try:
                    PANTALLA.blit(titulo2__, (30, 20, 0, 0))

                except: 
                    dibujado_de_texto(PANTALLA, " NIVELES ", fuente_titulos,BLANCO ,NEGRO, 30, 30, True)


                if nivel_I_botton.dibujar(PANTALLA):
                    acceso = "I"
                    niveles = False
                    juego = True

                if nivel_II_botton.dibujar(PANTALLA):
                    acceso = "II"
                    niveles = False
                    juego = True

                if nivel_III_botton.dibujar(PANTALLA):
                    acceso = "III"
                    niveles = False
                    juego = True

                if back__botton.dibujar(PANTALLA):
                    niveles = False

            if opciones:
                try:
                    control_volumen(PANTALLA, fondo__, volumen1__botton, volumen2__botton,None, titulo__opciones)

                except UnboundLocalError:
                    control_volumen(PANTALLA, fondo__, volumen1__botton, volumen2__botton, fuente_titulos)

                
                if back__botton.dibujar(PANTALLA):
                    opciones = False

        
        if juego:
            match(acceso):
                case "I":
                    juego = Galaxy(PANTALLA, fondo_juego__, player__, eventos, tiempo_juego)    
                case "II":
                    pass
                case "III":
                    pass

        for event in eventos:
            if event.type == QUIT:
                correr_juego = False

            pygame.display.update()

    pygame.quit()

    sys.exit()
        

def Galaxy(PANTALLA: pygame.surface.Surface, fondo: pygame.surface.Surface, jugador: naveEspacial, eventos, tiempo_juego):
    juego = True

    PANTALLA.blit(fondo, (0, 0))

    juego = jugador.movimiento()

    jugador.dibujar(PANTALLA)
    # for event in eventos:
    #     #if event.type == pygame.USEREVENT:
    #         if event.type == tiempo_juego:
    #             jugador.dibujar(PANTALLA)

    return juego

def control_volumen(PANTALLA:pygame.surface.Surface, fondo: pygame.surface.Surface, boton1, boton2, fuente_titulo = None, titulo = None):
    PANTALLA.blit(fondo, (0 , 0))

    try:
        PANTALLA.blit(titulo, (0, 0))
    except UnboundLocalError or TypeError:
        dibujado_de_texto(PANTALLA, " OPCIONES ", fuente_titulo, BLANCO, NEGRO, 30, 30)

    if boton1.dibujar(PANTALLA) and (pygame.mixer.music.get_volume()) <= 1.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)

    if boton2.dibujar(PANTALLA) and (pygame.mixer.music.get_volume()) >= 0.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() -0.1)




    
