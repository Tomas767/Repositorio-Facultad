import sys
from colores import *
from clases import *
from pygame.locals import K_DOWN, QUIT

def dibujado_de_texto(PANTALLA: pygame.surface.Surface, texto: str, fuente: pygame.font.Font, color_del_texto, color_fondo, x, y, marco = False):
    img = fuente.render(texto, True, color_del_texto, color_fondo)

    PANTALLA.blit(img, (x, y))

def iniciar__juego__():
    X = 800
    Y = 640


    # pantalla de juego y su resulocion en pixeles
    PANTALLA = pygame.display.set_mode((X, Y))

    # renderizado de actualizacion de la pantalla
    fps = 30
    tiempo_juego = pygame.time.get_ticks()
    reloj = pygame.time.Clock()
    pygame.time.set_timer(tiempo_juego,20)

    # icono y pantalla
    icono = pygame.image.load("imagenes/ICONO.png")
    pygame.display.set_caption("Space Invader")
    pygame.display.set_icon(icono)

    menu_principal(PANTALLA, X, Y)

def menu_principal(PANTALLA: pygame.surface.Surface ,X: int, Y: int):
    # banderas de acceso o seguimiento del juego
    correr_juego = True

    niveles = False

    juego = False

    opciones = False

    puntos = 0

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

    fuente_origen = "fuente\ARCADECLASSIC.TTF"

    try:
        titulo__ = pygame.image.load("imagenes\MENU PRINCIPAL.png")

    except FileNotFoundError:
    # establesco la fuente de texto del menu
        fuente = pygame.font.Font(fuente_origen, 30)
        fuente_titulos = pygame.font.Font(fuente_origen, 70)
    
    fuente_game_over = pygame.font.Font(fuente_origen, 80)
    fuente_puntos = pygame.font.Font(fuente_origen, 20)

    titulo2__ = pygame.image.load("imagenes\MENU_NIVELES.png")
    titulo__opciones = pygame.image.load("imagenes\OPCIONES_TITULO.png")

    # jugador y enemigos
    jugador_sprites = pygame.sprite.Group()
    enemigos_sprites = pygame.sprite.Group()
    disparos_sprites = pygame.sprite.Group()
    disparos_enemigos_sprites = pygame.sprite.Group()


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
                    dibujado_de_texto(PANTALLA," MENU PRINCIPAL ", fuente_game_over,BLANCO ,O0033CC, 100, 40, True)

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

                except UnboundLocalError:
                    dibujado_de_texto(PANTALLA, " NIVELES ", fuente_titulos,BLANCO ,NEGRO, 30, 30, True)


                if nivel_I_botton.dibujar(PANTALLA):
                    enemigos_sprites.empty()
                    disparos_sprites.empty()
                    for x in range(1, 4):
                        enemigo = NaveEnemiga(X, 0 , 0.6, 2, 1000)
                        enemigos_sprites.add(enemigo)
                    player__ = NaveJugador(X / 2, Y, 0.5)   
                    jugador_sprites.add(player__)
                    acceso = "I"
                    enemigos_sprites.empty()
                    disparos_sprites.empty()
                    disparos_enemigos_sprites.empty()
                    niveles = False
                    juego = True

                if nivel_II_botton.dibujar(PANTALLA):
                    enemigos_sprites.empty()
                    disparos_sprites.empty()
                    for x in range(1, 6):
                        enemigo = NaveEnemiga(X, 0 , 0.6, 2, 700)
                        enemigos_sprites.add(enemigo)
                    player__ = NaveJugador(X / 2, Y, 0.5)   
                    jugador_sprites.add(player__)
                    acceso = "II"
                    niveles = False
                    juego = True

                if nivel_III_botton.dibujar(PANTALLA):
                    enemigos_sprites.empty()
                    disparos_sprites.empty()
                    for x in range(1, 6):
                        enemigo = NaveEnemiga(X, 0 , 0.6, 2, 500)
                        enemigos_sprites.add(enemigo)
                    player__ = NaveJugador(X / 2, Y, 0.5)   
                    jugador_sprites.add(player__)
                    acceso = "II"
                    enemigos_sprites.empty()
                    disparos_sprites.empty()
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
                    juego, score_jugador = Galaxy(PANTALLA, fondo_juego__, 1000, (1, 5), jugador_sprites, disparos_sprites, enemigos_sprites, disparos_enemigos_sprites,
                                                  1, enemigo, player__, X, puntos, fuente_puntos, fuente_game_over)

                case "II":
                    juego, score_jugador = Galaxy(PANTALLA, fondo_juego__, 700, (1, 6), jugador_sprites, disparos_sprites, enemigos_sprites, disparos_enemigos_sprites,
                                                   1.5, enemigo, player__, X, puntos, fuente_puntos, fuente_game_over)

                case "III":
                    juego, score_jugador = Galaxy(PANTALLA, fondo_juego__, 500, (1, 6), jugador_sprites, disparos_sprites, enemigos_sprites, disparos_enemigos_sprites,
                                                   3, enemigo, player__, X, puntos, fuente_puntos, fuente_game_over)
        for event in eventos:
            if event.type == QUIT:
                correr_juego = False

            pygame.display.update()

    pygame.quit()

    sys.exit()

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

def Galaxy(PANTALLA: pygame.surface.Surface, fondo: pygame.surface.Surface, cadencia: int, cantidad_enemigos: tuple, jugador_sprites: pygame.sprite.Group, 
           disparos_sprites: pygame.sprite.Group, enemigos_sprites: pygame.sprite.Group, disparo_enemigo_sprites: pygame.sprite.Group, daño_enemigo, enemigo,
           player__: NaveJugador, X, puntos: int, fuente: pygame.font.Font,fuente_game_over: pygame.font.Font, bandera_meteoritos = False ):
    juego = True
    cronometro = pygame.time.Clock
    if player__.vida != 0:
        if len(enemigos_sprites) == 0:
            i, ii = cantidad_enemigos
            for x in range(i, ii):
                enemigo = NaveEnemiga(X, 0 , 0.6, 2, cadencia)
                enemigos_sprites.add(enemigo)

        tecla =  pygame.key.get_pressed()

        #actualizar sprites
        enemigos_sprites.update()
        disparos_sprites.update()

        # Dibujado de fondo y sprites
        PANTALLA.blit(fondo, (0, 0))

        jugador_sprites.draw(PANTALLA)
        enemigos_sprites.draw(PANTALLA) 
        disparos_sprites.draw(PANTALLA)
        disparo_enemigo_sprites.draw(PANTALLA)

        for x in enemigos_sprites:
            x.movimiento(PANTALLA , x, enemigos_sprites, disparo_enemigo_sprites)


        # ejecucion de disparo
        if (tecla[pygame.K_w]):
            tiempo = pygame.time.get_ticks()
            if tiempo - player__.ultimo_disparo > player__.cadencia:
                x, y = player__.rect.center        

                proyectil = player__.disparo(x, y)

                proyectil2 = player__.disparo(x - 20, y)

                disparos_sprites.add((proyectil, proyectil2))

                player__.ultimo_disparo = tiempo

        colicion = pygame.sprite.groupcollide(disparos_sprites, enemigos_sprites, True, True, pygame.sprite.collide_circle)

        colicion_2 = pygame.sprite.groupcollide(jugador_sprites, disparo_enemigo_sprites, False, True, pygame.sprite.collide_circle)

        if colicion:
            explocion = pygame.mixer.Sound("sonido\Explocion.mp3")
            puntos += 5
            explocion.play()

        if colicion_2:
            player__.vida -= daño_enemigo
            explocion1 = pygame.mixer.Sound("sonido\Explocion1.mp3")
            explocion1.play()
        juego = player__.movimiento(player__, puntos)

        dibujado_de_texto(PANTALLA, f"SCORE {str(player__.score)}", fuente, BLANCO, NEGRO, 0, 0)

        if bandera_meteoritos:
            pass

        if not juego:
            player__.score = 0
            cronometro = 0
            player__.kill()
    else:
        enemigos_sprites.empty()
        disparo_enemigo_sprites.empty()
        player__.kill()

        tecla =  pygame.key.get_pressed()

        if tecla[pygame.K_ESCAPE]:
            juego = False
            player__.sonido_click.play()
            cronometro = 0

        PANTALLA.blit(fondo, (0, 0))

        dibujado_de_texto(PANTALLA, "         GAME OVER         ", fuente_game_over, BLANCO, NEGRO, 100, 300 )

        dibujado_de_texto(PANTALLA, f"TU   SCORE {str(player__.score)}", fuente_game_over, BLANCO, NEGRO, 180, 400)

        dibujado_de_texto(PANTALLA, f"TU TIEMPO {str(cronometro)}", fuente_game_over, BLANCO, NEGRO, 180, 500)

    return juego, player__.score




