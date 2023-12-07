import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ingrese su nombre")

# Configuración de la fuente
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)

# Bucle principal del juego
def game_loop():
    input_text = ""
    clock = pygame.time.Clock()

    while True:
        screen.fill((0, 0, 0))

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Nombre ingresado:", input_text)
                    return  # Salir del bucle del juego si se presiona Enter
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        # Renderizar texto en la ventana
        text_surface = font.render(input_text, True, text_color)
        screen.blit(text_surface, (10, 10))

        pygame.display.flip()
        clock.tick(30)

# Ejecutar el juego
game_loop()