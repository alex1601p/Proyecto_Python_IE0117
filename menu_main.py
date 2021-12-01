import pygame
import sys
from config import *
from niveles import level
from pygame.locals import *


# Constantes para el codigo
clock = pygame.time.Clock()
pygame.display.set_caption('Labyrinth quest')

# tamaño de la pantalla
screen = pygame.display.set_mode((800, 600))

background_menu = pygame.image.load('Fondos\prueba.jpg').convert()
sprite_menu = pygame.image.load('Personaje\iz1.png').convert()

# Se define un nivel de referenia
# para inicializar alunas funciones
level_1 = level(level_map_1, screen,
                "sprites\Sprite lvl 1.png",
                "Puntajes\Level1.txt")
# Colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
plomo = (232, 224, 224)
yellow = (255, 255, 0)

# Inicializacion
pygame.init()
pygame.mixer.init()
pygame.font.init()

# Detecta la informacion de la pantalla
display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h

cancion1 = pygame.mixer.Sound("Sonidos\Musica playa.mp3")
cancion2 = pygame.mixer.Sound("Sonidos\Musica bosque.mp3")
cancion3 = pygame.mixer.Sound("Sonidos\Musica selva.mp3")
cancion4 = pygame.mixer.Sound("Sonidos\Musica nieve.mp3")
cancion5 = pygame.mixer.Sound("Sonidos\Musica mazmorra.mp3")
cancion6 = pygame.mixer.Sound("Sonidos\Musica dungeon.mp3")
cancion7 = pygame.mixer.Sound("Sonidos\Musica luna.mp3")
cancion8 = pygame.mixer.Sound("Sonidos\Musica inferno.mp3")
cancion9 = pygame.mixer.Sound("Sonidos\Musica marte.mp3")
cancion10 = pygame.mixer.Sound("Sonidos\Musica cielo.mp3")

pasos = pygame.mixer.Sound("Sonidos\Pasos en arena.mp3")


# Fuentes para la letra de menu
small_font = pygame.font.SysFont('comicsansms', 15)
medium_font = pygame.font.SysFont('comicsansms', 30)
large_font = pygame.font.SysFont('comicsansms', 50)


# Datos para los botones en menu principal
size_button = [200, 45]

button_levels = [300, 200]
color_levels = [plomo, yellow]

button_score = [300, 270]
color_score = [plomo, yellow]

button_options = [300, 340]
color_options = [plomo, red]

button_controls = [300, 410]
color_controls = [plomo, green]

button_exit = [300, 480]
color_exit = [plomo, yellow]

button_regress = [625, 500]
color_regress = [plomo, yellow]

button_back_levels = [300, 200]
color_back_levels = [plomo, yellow]

button_continue = [300, 300]
color_continue = [plomo, yellow]

# Datos para botones de niveles
size_but_lvl = [100, 45]
color_but_lvl = [plomo, green]

# posciones de los botones
button_lvl1 = [75, 235]
button_lvl2 = [212, 235]
button_lvl3 = [349, 235]
button_lvl4 = [486, 235]
button_lvl5 = [625, 235]
button_lvl6 = [75, 325]
button_lvl7 = [212, 325]
button_lvl8 = [349, 325]
button_lvl9 = [486, 325]
button_lvl10 = [625, 325]


def msg_button(msg, color, button_X, button_Y, width, height, size='small'):
    # Texto dentro del boton
    text_select, textRect = obj_text(msg, color, size)
    textRect.center = (button_X+(width/2), button_Y+(height/2))
    screen.blit(text_select, textRect)


def buttons(text, surface, state, posit, size_butt, id_button=None):
    # Para la creacion de los botones
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Define si el cursor esta en el boton o no
    if (posit[0] + size_butt[0] > cursor[0] > size_butt[0] and posit[0]
       + size_butt[0] < cursor[0] + size_butt[0] and posit[1]
       + size_butt[1] > cursor[1] > size_butt[1] and posit[1]
       + size_butt[1] < cursor[1] + size_butt[1]):

        if click[0] == 1:
            if id_button == 'niveles':
                menulevels()
            if id_button == 'back_levels':
                pygame.mixer.stop()
                menulevels()

            if id_button == 'continue':
                pygame.mixer.unpause()
                return

            if id_button == 'puntajes':
                score()
            if id_button == 'configuracion':
                options()
            if id_button == 'detalles':
                controls()
            if id_button == 'regresar':
                intromenu()
            if id_button == 'salir':
                pygame.quit()
                quit()

            # Para los niveles
            elif id_button == 'lvl1':
                level_1 = level(level_map_1, screen,
                                "sprites\Sprite lvl 1.png",
                                "Puntajes\Level1.txt")
                cancion1.play(-1)
                game_state = True
                while game_state:
                    if level_1.GameOver():
                        screen.fill('grey')
                        level_1.run()

                        fps.render(screen, level_1.puntaje())
                        fps.clock.tick(60)
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if (event.key == pygame.K_ESCAPE):
                                    pause()
                                elif (event.key == pygame.K_m):
                                    pygame.mixer.pause()
                                elif (event.key == pygame.K_n):
                                    pygame.mixer.unpause()
                    else:
                        menulevels()

            elif id_button == 'lvl2':
                level_2 = level(level_map_2, screen,
                                "sprites\Sprite lvl 2.png",
                                "Puntajes\Level2.txt")
                cancion2.play(-1)
                game_state = True
                while game_state:
                    if level_2.GameOver():
                        screen.fill('grey')
                        level_2.run()
                        fps.render(screen, level_2.puntaje())
                        fps.clock.tick(60)
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if (event.key == pygame.K_ESCAPE):
                                    pause()
                                elif (event.key == pygame.K_m):
                                    pygame.mixer.pause()
                                elif (event.key == pygame.K_n):
                                    pygame.mixer.unpause()
                    else:
                        menulevels()

            elif id_button == 'lvl3':
                level_3 = level(level_map_3, screen,
                                "sprites\Sprite lvl 3.png",
                                "Puntajes\Level3.txt")
                cancion3.play(-1)
                game_state = True
                while game_state:
                    if level_3.GameOver():
                        screen.fill('grey')
                        level_3.run()
                        fps.render(screen, level_3.puntaje())
                        fps.clock.tick(60)
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if (event.key == pygame.K_ESCAPE):
                                    pause()
                                elif (event.key == pygame.K_m):
                                    pygame.mixer.pause()
                                elif (event.key == pygame.K_n):
                                    pygame.mixer.unpause()
                    else:
                        menulevels()

            elif id_button == 'lvl4':
                level_4 = level(level_map_4, screen,
                                "sprites\Sprite lvl 4.png",
                                "Puntajes\Level4.txt")
                cancion4.play(-1)
                game_state = True
                while game_state:
                    if level_4.GameOver():
                        screen.fill('grey')
                        level_4.run()
                        fps.render(screen, level_4.puntaje())
                        fps.clock.tick(60)
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    quit()
                                if (event.key == pygame.K_ESCAPE):
                                    pause()
                                elif (event.key == pygame.K_m):
                                    pygame.mixer.pause()
                                elif (event.key == pygame.K_n):
                                    pygame.mixer.unpause()
                    else:
                        menulevels()

            elif id_button == 'lvl5':
                level_5 = level(level_map_5, screen,
                                "sprites\Sprite lvl 5.png",
                                "Puntajes\Level5.txt")
                cancion5.play(-1)
                game_state = True
                while game_state:
                    if level_5.GameOver():
                        screen.fill('grey')
                        level_5.run()
                        fps.render(screen, level_5.puntaje())
                        fps.clock.tick(60)
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    quit()
                                if (event.key == pygame.K_ESCAPE):
                                    pause()
                                elif (event.key == pygame.K_m):
                                    pygame.mixer.pause()
                                elif (event.key == pygame.K_n):
                                    pygame.mixer.unpause()
                    else:
                        menulevels()

            elif id_button == 'lvl6':
                level_6 = level(level_map_6, screen,
                                "sprites\Sprite lvl 6.png",
                                "Puntajes\Level6.txt")
                cancion6.play(-1)
                game_state = True
                while game_state:
                    if level_6.GameOver():
                        screen.fill('grey')
                        level_6.run()
                        fps.render(screen, level_6.puntaje())
                        fps.clock.tick(60)
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if (event.key == pygame.K_ESCAPE):
                                    pause()
                                elif (event.key == pygame.K_m):
                                    pygame.mixer.pause()
                                elif (event.key == pygame.K_n):
                                    pygame.mixer.unpause()
                    else:
                        menulevels()

            elif id_button == 'lvl7':
                level_7 = level(level_map_7, screen,
                                "sprites\Sprite lvl 7.png",
                                "Puntajes\Level7.txt")
                cancion7.play(-1)
                game_state = True
                while game_state:
                    if level_7.GameOver():
                        screen.fill('grey')
                        level_7.run()
                        fps.render(screen, level_7.puntaje())
                        fps.clock.tick(60)
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if (event.key == pygame.K_ESCAPE):
                                    pause()
                                elif (event.key == pygame.K_m):
                                    pygame.mixer.pause()
                                elif (event.key == pygame.K_n):
                                    pygame.mixer.unpause()
                    else:
                        menulevels()

            elif id_button == 'lvl8':
                level_8 = level(level_map_8, screen,
                                "sprites\Sprite lvl 8.png",
                                "Puntajes\Level8.txt")
                cancion8.play(-1)
                game_state = True
                while game_state:
                    if level_8.GameOver():
                        screen.fill('grey')
                        level_8.run()
                        fps.render(screen, level_8.puntaje())
                        fps.clock.tick(60)
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if (event.key == pygame.K_ESCAPE):
                                    pause()
                                elif (event.key == pygame.K_m):
                                    pygame.mixer.pause()
                                elif (event.key == pygame.K_n):
                                    pygame.mixer.unpause()
                    else:
                        menulevels()

            elif id_button == 'lvl9':
                level_9 = level(level_map_9, screen,
                                "sprites\Sprite lvl 9.png",
                                "Puntajes\Level9.txt")
                cancion9.play(-1)
                game_state = True
                while game_state:
                    if level_9.GameOver():
                        screen.fill('grey')
                        level_9.run()
                        fps.render(screen, level_9.puntaje())
                        fps.clock.tick(60)
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if (event.key == pygame.K_ESCAPE):
                                    pause()
                                elif (event.key == pygame.K_m):
                                    pygame.mixer.pause()
                                elif (event.key == pygame.K_n):
                                    pygame.mixer.unpause()
                    else:
                        menulevels()

            elif id_button == 'lvl10':
                level_10 = level(level_map_10, screen,
                                 "sprites\Sprite lvl 10.png",
                                 "Puntajes\Level9.txt")
                cancion10.play(-1)
                game_state = True
                while game_state:
                    if level_10.GameOver():
                        screen.fill('grey')
                        level_10.run()
                        fps.render(screen, level_10.puntaje())
                        fps.clock.tick(60)
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if (event.key == pygame.K_ESCAPE):
                                    pause()
                                elif (event.key == pygame.K_m):
                                    pygame.mixer.pause()
                                elif (event.key == pygame.K_n):
                                    pygame.mixer.unpause()
                    else:
                        menulevels()

        button = pygame.draw.rect(surface, state[1],
                                  (posit[0], posit[1], size_butt[0],
                                  size_butt[1]))
    else:
        button = pygame.draw.rect(surface, state[0],
                                  (posit[0], posit[1], size_butt[0],
                                  size_butt[1]))

    msg_button(text, black, posit[0], posit[1], size_butt[0], size_butt[1])
    return button


def obj_text(text, color, size):
    # Funcion para el tamaño de letra
    if size == 'small':
        text_select = small_font.render(text, True, color)
    if size == 'medium':
        text_select = medium_font.render(text, True, color)
    if size == 'large':
        text_select = large_font.render(text, True, color)
    return text_select, text_select.get_rect()


def message(msg, color, despla_X=0, despla_Y=0, size='small'):
    # Funcion de caracteristicas del texto
    text_select, textRect = obj_text(msg, color, size)
    textRect.center = (screen_width/2)+despla_X, (screen_height/2)+despla_Y
    screen.blit(text_select, textRect)


def intromenu():
    # Menu principal, primera cara del juego
    introgame = True
    while introgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(background_menu, [0, 0])
        screen.blit(sprite_menu, [700, 300])

        # Botones y sus textos en la pagina menu
        buttons('NIVELES', screen, color_levels, button_levels,
                size_button, id_button='niveles')

        buttons('MEJORES PUNTAJES', screen, color_score, button_score,
                size_button, id_button='puntajes')

        buttons('OPCIONES', screen, color_options, button_options,
                size_button, id_button='configuracion')

        buttons('CONTROLES', screen, color_controls, button_controls,
                size_button, id_button='detalles')

        buttons('SALIR', screen, color_exit, button_exit,
                size_button, id_button='salir')

        # Mensajes libres en la pantalla
        message('LABYRINTH QUEST', black, 0, -250, size='large')
        message('LABYRINTH QUEST', red, 0, -246, size='large')

        pygame.display.update()
        clock.tick(60)


def options():
    # Para principalmente el volumen, si se puede ajuste de tamaño de pantalla
    regres = True

    while regres:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                regres = False
                pygame.quit()

        screen.blit(background_menu,[0,0])
        buttons('ATRAS',screen,color_regress,button_regress,size_but_lvl,id_button='regresar')
        message('Aqui iran las opciones',red,0,-100,size='medium')
        pygame.display.update()
        clock.tick(60)


def controls():
    # Pantalla para controles del jugador
    regres = True

    while regres:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        buttons('ATRAS', screen, color_regress, button_regress,
                size_but_lvl, id_button='regresar')

        message('Controles', red,0,-250,size='large')
        message('Teclas para utilizar',red,-200,-175,size='medium')
        message('Hola',red,0,-100,size='medium')
        pygame.display.update()
        clock.tick(60)

#lugar para los mejores puntajes de los laberintos
def score():
    scores = True

    while scores:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        buttons('ATRAS',screen,color_regress,button_regress,size_but_lvl,id_button='regresar')
        message('Aqui iran los mejores puntajes',red,0,-100,size='medium')
        pygame.display.update()
        clock.tick(60)


def pause():
    # Menu de pausa dentro del juego
    regres = True
    pygame.mixer.pause()

    while regres:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        buttons('VOLVER A NIVELES', screen, color_back_levels,
                button_back_levels, size_button, id_button='back_levels')

        regres = buttons('CONTINUAR', screen, color_continue, button_continue,
                         size_button, id_button='continue')

        message('PAUSA', green, 0, -200, size='medium')
        pygame.display.update()
        clock.tick(60)



#Estaran todos los niveles para escoger
def menulevels():
    regres = True

    while regres:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(60)
        screen.blit(background_menu,[0,0])

        buttons('Nivel I', screen, color_but_lvl, button_lvl1,
                size_but_lvl, id_button='lvl1')

        buttons('Nivel II', screen, color_but_lvl, button_lvl2,
                size_but_lvl, id_button='lvl2')

        buttons('Nivel III', screen, color_but_lvl, button_lvl3,
                size_but_lvl, id_button='lvl3')

        buttons('Nivel IV', screen, color_but_lvl, button_lvl4,
                size_but_lvl, id_button='lvl4')

        buttons('Nivel V', screen, color_but_lvl, button_lvl5,
                size_but_lvl, id_button='lvl5')

        buttons('Nivel VI', screen, color_but_lvl, button_lvl6,
                size_but_lvl, id_button='lvl6')

        buttons('Nivel VII', screen, color_but_lvl, button_lvl7,
                size_but_lvl, id_button='lvl7')

        buttons('Nivel VIII', screen, color_but_lvl, button_lvl8,
                size_but_lvl, id_button='lvl8')

        buttons('Nivel IX', screen, color_but_lvl, button_lvl9,
                size_but_lvl, id_button='lvl9')

        buttons('Nivel X', screen, color_but_lvl, button_lvl10,
                size_but_lvl, id_button='lvl10')

        buttons('ATRAS', screen, color_regress, button_regress,
                size_but_lvl, id_button='regresar')


class puntos:
    # Muestra el puntaje
    def __init__(self, puntaje):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Comic Sans MS", 20)
        self.text = self.font.render(str(puntaje), True, (0, 0, 0))
        screen.blit(self.text, (10, 10))

    def render(self, screen, puntaje):
        self.text = self.font.render(str(puntaje), True, (0, 0, 0))
        screen.blit(self.text, (10, 10))


fps = puntos(level_1.puntaje())

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        # Inicio del modulo de sonido 1
        if event.type == pygame.KEYDOWN:

            # Con n se reanuda donde se dejo pausada
            if (event.key == pygame.K_m):
                pygame.mixer.pause()
            elif (event.key == pygame.K_n):
                pygame.mixer.unpause()
        # Fin del modulo de sonido

        # Con este comando si apretas ESC el juego se cerrará
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.QUIT:
            sys.exit()

    intromenu()

    pygame.display.flip()
