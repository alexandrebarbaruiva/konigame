#! /usr/bin/env python
from random import randrange
import pygame
from pygame.locals import *
from pygame import *
from pygame.transform import *

def button(x,y,w,h,cor):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(screen, cor, (x,y,w,h))

    if x+w > mouse[0] > x and y+h > mouse[1] > y and click[0]:
        return False
    else:
        return True

def get_rect(obj):
    return Rect(obj['position'][0],
                obj['position'][1],
                obj['surface'].get_width(),
                obj['surface'].get_height())

def get_b_rect(obj):
    # if (obj['surface'].get_width() < 110):
    #     return Rect(obj['position'][0] - 10,
    #                 obj['position'][1] - 30,
    #                 obj['surface'].get_width() - 10,
    #                 obj['surface'].get_height() - 20)

    return Rect(obj['position'][0] + 20,
                obj['position'][1] + 100,
                obj['surface'].get_width() - 20,
                obj['surface'].get_height() - 200)

def bridge_crossed():
    person_rect = get_rect(player)
    for bridge in bridges:
        if person_rect.colliderect(get_b_rect(bridge)):
            bridge['crossed'] = True

pygame.init()

# Fonts
pygame.font.init()
font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name, 40)
font_over = pygame.font.SysFont("comicsansms", 100)
small_font = pygame.font.SysFont(font_name, 30)
medium_font = pygame.font.SysFont(font_name, 50)

# Color definitions
color_red = (255,0,0)
color_green = (0,255,0)
color_black = (0,0,0)

# Display size
screen = pygame.display.set_mode((1200, 720))

# Load background image
bg_filename = 'images/bg_final.png'
background = image.load(bg_filename).convert()
pygame.display.set_caption('Bridges')

player = {
    'surface': image.load('images/player3.png').convert_alpha(),
    'position': [30, 30],
    'speed': {
        'x': 0,
        'y': 0
    }
}
bdgf = image.load('images/bridge.png').convert_alpha()
bdgftr = image.load('images/bridge_transp.png').convert_alpha()
def brdg():
    return [{
            'show': True,
            'angle': -80,
            'flip': False,
            'surface': rotate(bdgf,-80),
            'position': [250, 170],
            'crossed': False },
            {
            'show': True,
            'angle': -90,
            'flip': False,
            'surface': rotate(bdgf,-90),
            'position': [405, 420],
            'crossed': False },
            {
            'show': True,
            'angle': -90,
            'flip': False,
            'surface': rotate(bdgf,-90),
            'position': [630, 420],
            'crossed': False },
            {
            'show': True,
            'angle':-90,
            'flip': False,
            'surface': rotate(bdgf,-90),
            'position': [600, 70],
            'crossed': False },
            {
            'show': True,
            'angle':-60,
            'flip': False,
            'surface': rotate(bdgf,-60),
            'position': [990, 25],
            'crossed': False },
            {
            'show': True,
            'angle':-70,
            'flip': True,
            'surface': flip(rotate(bdgf,-70), True, False),
            'position': [990, 440],
            'crossed': False },
            {
            'show': True,
            'angle': -4,
            'flip': False,
            'surface': rotate(bdgf,-4),
            'position': [805, 290],
            'crossed': False }
        ]

running = True
clock = pygame.time.Clock()
reset_game = False
bridges = brdg()
player_score = 0

while running:

    # Pressed or clicked events
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or pressed_keys[K_ESCAPE]:
            exit()
    # Check for quantity of bridges available
    available_bridges = sum([bridge['show'] for bridge in bridges])

    if(((player_score < available_bridges) and (available_bridges % 2 != 0)) or (available_bridges % 2 == 0)):
        if pressed_keys[K_UP]:
            player['speed']['y'] = -7
        elif pressed_keys[K_DOWN]:
            player['speed']['y'] = 7
        if pressed_keys[K_LEFT]:
            player['speed']['x'] = -7
        elif pressed_keys[K_RIGHT]:
            player['speed']['x'] = 7

    if pressed_keys[K_1]:
        bridges[0]['show'] = False
    if pressed_keys[K_2]:
        bridges[1]['show'] = False
    if pressed_keys[K_3]:
        bridges[2]['show'] = False
    if pressed_keys[K_4]:
        bridges[3]['show'] = False
    if pressed_keys[K_5]:
        bridges[4]['show'] = False
    if pressed_keys[K_6]:
        bridges[5]['show'] = False
    if pressed_keys[K_7]:
        bridges[6]['show'] = False

    screen.blit(pygame.Surface(screen.get_size()), (0, 0))
    screen.blit(background, (0, 0))
    # Check state of bridges
    player_score = 0
    bridge_crossed()

    for bridge in bridges:
        if bridge['show']:
            if not bridge['crossed']:
                screen.blit(bridge['surface'], bridge['position'])
            else:
                if bridge['flip']:
                    bridge['surface'] = flip(rotate(bdgftr,bridge['angle']), True, False)
                else:
                    bridge['surface'] = rotate(bdgftr,bridge['angle'])
                screen.blit(bridge['surface'], bridge['position'])
                player_score += 1

    # Player location
    # if (player['position'][0] + player['speed']['x'] < ):
    player['position'][0] += player['speed']['x']
    player['position'][1] += player['speed']['y']
    screen.blit(player['surface'], player['position'])

    if player_score >= 6 and available_bridges == 7:
        text_surface = font_over.render("GAME OVER", True, color_red)
        screen.blit(text_surface , (330,200))
        running = button(550,400,100,50,color_red)
        quit_surface = game_font.render("QUIT", True, color_black)
        screen.blit(quit_surface , (565,415))

    elif player_score == available_bridges:
        text_surface = font_over.render("GOOD JOB", True, color_black)
        screen.blit(text_surface , (320,200))
        running = button(550,350,100,50, color_green)
        quit_surface = game_font.render("QUIT", True, color_black)
        screen.blit(quit_surface , (565,365))


    # Show score
    player_score_surface = "Pontuação: " + str(player_score)
    score_surface = medium_font.render(player_score_surface, False, color_black)
    screen.blit(score_surface , (0,0))

    #Restart Button
    reset_game = not button(1120,0,77,35,color_green)
    start_surface = small_font.render("RESET", True, color_black)
    screen.blit(start_surface , (1125,10))
    if reset_game or pressed_keys[K_r]:
        bridges = brdg()

    # Restart game
    player['speed'] = {'x': 0, 'y': 0}
    pygame.display.update()
    clock.tick(30)
