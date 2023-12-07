import pygame, sys, sqlite3
from colores import *
from clases import *
from pygame.locals import *

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
    pygame.time.set_timer(tiempo_juego,10)

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

    establecer_nombre = None

    input_text = ""
    puntos = 0
    #
    with sqlite3.connect("base.db") as conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute('''CREATE TABLE jugadores 
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT NOT NULL,
time INTEGER,
score INTEGER
)''')
            conexion.commit()
            print("Se creo la tabla jugadores")
        except Exception as fallo:
            print(fallo)
    
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
    
    fuente_game_over = pygame.font.Font(fuente_origen, 50)
    fuente_puntos = pygame.font.Font(fuente_origen, 20)
    fuente_tabla = pygame.font.Font(fuente_origen, 30)
    titulo2__ = pygame.image.load("imagenes\MENU_NIVELES.png")
    titulo__opciones = pygame.image.load("imagenes\OPCIONES_TITULO.png")
    vida_jugador = pygame.image.load("imagenes\\vida.png")

    # jugador y enemigos
    jugador_sprites = pygame.sprite.Group()
    enemigos_sprites = pygame.sprite.Group()
    enemigos2_sprites = pygame.sprite.Group()
    disparos_sprites = pygame.sprite.Group()
    disparos_enemigos_sprites = pygame.sprite.Group()
    disparos_enemigos_sprites_2 = pygame.sprite.Group()


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
                
                dibujado_de_texto(PANTALLA, "NOMBRE    TIEMPO    SCORE", fuente_tabla, BLANCO, NEGRO, 70, 150, True)
                with sqlite3.connect("base.db") as conexion:
                    try:
                        cursor2 = conexion.execute("SELECT * FROM jugadores")
                        for fila in cursor2:
                            if fila[2] != None:
                                dibujado_de_texto(PANTALLA, f"{fila[1]}            S {fila[2]}                   {fila[3]}", fuente_tabla, BLANCO, NEGRO, 70, 200, True)

                    except Exception as fallo3:
                        print(fallo3)

                if establecer_nombre != None:
                    if establecer_nombre:
                        for event in eventos:
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    nombre_jugador = input_text
                                    enemigos_sprites.empty()
                                    disparos_sprites.empty()
                                    jugador_sprites.empty()
                                    player__ = NaveJugador(X / 2, Y, 0.5)   
                                    jugador_sprites.add(player__)
                                    niveles = False
                                    juego = True
                                    establecer_nombre = None
                                elif event.key == pygame.K_BACKSPACE:
                                    input_text = input_text[:-1]
                                elif event.key == pygame.K_ESCAPE:
                                    establecer_nombre = None 
                                elif len(input_text) < 5 and event.unicode.isprintable():
                                    input_text += event.unicode
                            text_surface = fuente_game_over.render(input_text, True, BLANCO)
                            PANTALLA.blit(text_surface, (300, 600))

                        dibujado_de_texto(PANTALLA, "ESC para cancelar", fuente_tabla, BLANCO, NEGRO, 250, 550, True)
                        dibujado_de_texto(PANTALLA, "ENTER para confirmar", fuente_tabla, BLANCO, NEGRO, 250, 500, True)
                            # Renderizar texto en la ventana
                            
                

                if nivel_I_botton.dibujar(PANTALLA):
                    acceso = "I"
                    establecer_nombre = True

                if nivel_II_botton.dibujar(PANTALLA):
                    acceso = "II"
                    establecer_nombre = True

                if nivel_III_botton.dibujar(PANTALLA):
                    acceso = "III"
                    establecer_nombre = True

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
                    juego, score_jugador, cronometro = Galaxy(PANTALLA, fondo_juego__, acceso, 1200, jugador_sprites, disparos_sprites, enemigos_sprites, 
                    disparos_enemigos_sprites, 1, player__, X, puntos, fuente_puntos, fuente_game_over, vida_jugador)

                case "II":
                    juego, score_jugador, cronometro = Galaxy(PANTALLA, fondo_juego__, acceso, 900, jugador_sprites, disparos_sprites, enemigos_sprites, 
                    disparos_enemigos_sprites, 1, player__, X, puntos, fuente_puntos, fuente_game_over, vida_jugador)

                case "III":
                    juego, score_jugador, cronometro = Galaxy(PANTALLA, fondo_juego__, acceso, 700, jugador_sprites, disparos_sprites, enemigos_sprites, 
                    disparos_enemigos_sprites, 1, player__, X, puntos, fuente_puntos, fuente_game_over, vida_jugador)
            if not juego:
                try:
                    with sqlite3.connect("base.db") as conexion:
                        conexion.execute("INSERT INTO jugadores (nombre,time,score) values(?, ?, ?)", (nombre_jugador,cronometro,score_jugador))
                        conexion.commit()
                except Exception as fallo2:
                    print(fallo2)

        
        for event in eventos:
            if event.type == QUIT:
                correr_juego = False

            pygame.display.update()

    pygame.quit()

    sys.exit()

def Galaxy(PANTALLA: pygame.surface.Surface, fondo: pygame.surface.Surface, nivel: str, cadencia: int, jugador_sprites: pygame.sprite.Group, 
           disparos_sprites: pygame.sprite.Group, enemigos_sprites: pygame.sprite.Group, disparo_enemigo_sprites: pygame.sprite.Group, 
           daño_enemigo, player__: NaveJugador, X, puntos: int, fuente: pygame.font.Font,fuente_game_over: pygame.font.Font, vida_):
    juego = True
    if player__.vida > 0:
        if player__.avance != 6:
            player__.cronometro = pygame.time.get_ticks()
            if len(enemigos_sprites) == 0: 
                disparo_enemigo_sprites.empty()
                enemigos_sprites = generacion_nivel(X, nivel, player__, enemigos_sprites, cadencia)

            tecla =  pygame.key.get_pressed()

            #actualizar sprites
            jugador_sprites.update()
            enemigos_sprites.update()
            disparos_sprites.update()

            # Dibujado de fondo y sprites
            PANTALLA.blit(fondo, (0, 0))

            jugador_sprites.draw(PANTALLA)
            disparos_sprites.draw(PANTALLA)
            enemigos_sprites.draw(PANTALLA) 

            for x in enemigos_sprites:
                x.movimiento(PANTALLA, enemigos_sprites, disparo_enemigo_sprites)

            # ejecucion de disparo
            if (tecla[pygame.K_w]):
                tiempo = pygame.time.get_ticks()
                if tiempo - player__.ultimo_disparo > player__.cadencia:
                    x, y = player__.rect.center        

                    proyectil = player__.disparo(x, y)

                    proyectil2 = player__.disparo(x - 20, y)

                    disparos_sprites.add((proyectil, proyectil2))

                    player__.ultimo_disparo = tiempo

            for q in enemigos_sprites:
                if type(q) == NaveEnemiga:
                    condicion = str(type(q))
                elif type(q) == NaveEnemiga_2:
                    condicion = str(type(q))
            
            match (condicion):
                case "<class 'clases.NaveEnemiga'>":
                    colicion = pygame.sprite.groupcollide(disparos_sprites, enemigos_sprites, True, True)
                    if colicion:
                        explocion = pygame.mixer.Sound("sonido\Explocion.mp3")
                        puntos += 5
                        explocion.play()
                case "<class 'clases.NaveEnemiga_2'>":    
                    colicion = pygame.sprite.groupcollide(disparos_sprites, enemigos_sprites, True, False)
                    if colicion:
                        explocion = pygame.mixer.Sound("sonido\Explocion.mp3")
                        explocion.play()
                        for jugador, enemigos_colisionados in colicion.items():
                            for enemigo in enemigos_colisionados:
                                enemigo.vida -= 1

                                if enemigo.vida == 0:
                                    enemigo.kill()

            colicion_2 = pygame.sprite.groupcollide(jugador_sprites, disparo_enemigo_sprites, False, True)


            if colicion_2:
                player__.vida -= daño_enemigo
                explocion1 = pygame.mixer.Sound("sonido\Explocion1.mp3")
                explocion1.play()

            juego = player__.movimiento(player__, puntos)

            if player__.vida >= 3:
                PANTALLA.blit(vida_, (760, 0))
            if player__.vida >= 2:
                PANTALLA.blit(vida_, (710, 0))
            if player__.vida >= 1:
                PANTALLA.blit(vida_, (660, 0))      

            dibujado_de_texto(PANTALLA, f"OLEADA   {str(player__.avance)}", fuente, BLANCO, NEGRO, 0, 20, True)
            dibujado_de_texto(PANTALLA, f"SCORE   {str(player__.score)}", fuente, BLANCO, NEGRO, 0, 0, True)

        else:
            tiempo = int(player__.cronometro / 1000)
            tecla =  pygame.key.get_pressed()

            if tecla[pygame.K_ESCAPE]:
                juego = False
                player__.sonido_click.play()

            PANTALLA.blit(fondo, (0, 0))

            dibujado_de_texto(PANTALLA, "           VICTORIA!!         ", fuente_game_over, BLANCO, NEGRO, 150, 0 )
            dibujado_de_texto(PANTALLA, f"  SCORE   {player__.score}   ", fuente_game_over, BLANCO, NEGRO, 0, 100 )
            dibujado_de_texto(PANTALLA, f"  TIEMPO    {tiempo}", fuente_game_over, BLANCO, NEGRO, 0, 200)
            dibujado_de_texto(PANTALLA, f"  ESC para salir", fuente_game_over, BLANCO, NEGRO, 200, 600)

            return juego, player__.score, tiempo
    else:
        tiempo = int(player__.cronometro / 1000)
        tecla =  pygame.key.get_pressed()

        if tecla[pygame.K_ESCAPE]:
            juego = False
            player__.sonido_click.play()

        PANTALLA.blit(fondo, (0, 0))

        dibujado_de_texto(PANTALLA, "           GAME OVER         ", fuente_game_over, BLANCO, NEGRO, 150, 0 )
        dibujado_de_texto(PANTALLA, f"  SCORE   {player__.score}   ", fuente_game_over, BLANCO, NEGRO, 0, 100 )
        dibujado_de_texto(PANTALLA, f"  TIEMPO    {tiempo}", fuente_game_over, BLANCO, NEGRO, 0, 200)
        dibujado_de_texto(PANTALLA, f"  ESC para salir", fuente_game_over, BLANCO, NEGRO, 200, 600)


        return juego, player__.score, tiempo

    return juego, None, None

def generacion_nivel(X, nivel: str, jugador: NaveJugador, enemigos_sprites: pygame.sprite.Group, cadencia: int):
    jugador.avance += 1 
    x1, x2 = (1, 4)
    match(nivel):
        case "I":
            if jugador.avance <= 1:
                for x in range(x1, x2):
                    enemigo = NaveEnemiga(X, 0 , 0.6, 2, cadencia)
                    enemigos_sprites.add(enemigo)

            elif jugador.avance >= 2 and jugador.avance <= 3: 
                for x in range(x1, x2):
                    enemigo = NaveEnemiga(X, 0 , 0.6, 2, (cadencia - 500))
                    enemigos_sprites.add(enemigo)

            elif jugador.avance >= 4:
                jugador.ordas_final += 1
                if (jugador.ordas_final % 3) != 0:
                    for x in range(x1, x2):
                        enemigo = NaveEnemiga(X, 0 , 0.6, 2, (cadencia - 700))
                        enemigos_sprites.add(enemigo)
                else:   
                    for x in range(x1, x2):
                        enemigo2 = NaveEnemiga_2(X, 0 , 0.6, 2, (cadencia))
                        enemigos_sprites.add(enemigo2)
        case "II":
            if jugador.avance <= 2:
                for x in range(x1, x2):
                    enemigo = NaveEnemiga(X, 0 , 0.6, 2, (cadencia))
                    enemigos_sprites.add(enemigo)
            
            if jugador.avance >= 3:
                jugador.ordas_final += 1
                if (jugador.ordas_final % 3) != 0:
                    for x in range(x1, x2):
                        enemigo = NaveEnemiga(X, 0 , 0.6, 2, (cadencia - 300))
                        enemigos_sprites.add(enemigo)
                else:
                    for x in range(x1, x2):
                        enemigo2 = NaveEnemiga_2(X, 0 , 0.6, 2, (cadencia))
                    enemigos_sprites.add(enemigo2)
        case "III":
                if (jugador.avance % 3) != 0:
                    for x in range(x1, x2):
                        enemigo = NaveEnemiga(X, 0 , 0.6, 2, (cadencia))
                        enemigos_sprites.add(enemigo)
                else:   
                    for x in range(x1, x2):
                        enemigo2 = NaveEnemiga_2(X, 0 , 0.6, 2, (cadencia))
                        enemigos_sprites.add(enemigo2)

    return enemigos_sprites

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