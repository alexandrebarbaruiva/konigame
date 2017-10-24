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
    return Rect(obj['position'][0] + 40,
                obj['position'][1] + 40,
                obj['surface'].get_width() - 40,
                obj['surface'].get_height() - 10)

def get_b_rect(obj):
    print(obj['position'][0], obj['position'][1],obj['surface'].get_width(),obj['surface'].get_height())
    return Rect(obj['position'][0] + 50,
                obj['position'][1] + 50,
                obj['surface'].get_width() - 50,
                obj['surface'].get_height() - 50)

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

# Color definitions
color_red = (255,0,0)
color_green = (0,255,0)
color_black = (0,0,0)

# Display size
screen = pygame.display.set_mode((800, 620))

# Load background image
bg_filename = 'images/bg_c1.png'
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
            'angle': -60,
            'flip': False,
            'surface': rotate(bdgf,-60),
            'position': [150, 100],
            'crossed': False },
            {
            'show': True,
            'angle': -40,
            'flip': True,
            'surface': flip(rotate(bdgf,-40), True, False),
            'position': [40, 300],
            'crossed': False },
            {
            'show': True,
            'angle': -90,
            'flip': False,
            'surface': rotate(bdgf,-90),
            'position': [400, 340],
            'crossed': False },
            {
            'show': True,
            'angle':-90,
            'flip': False,
            'surface': rotate(bdgf,-90),
            'position': [400, 60],
            'crossed': False },
            {
            'show': True,
            'angle':-60,
            'flip': False,
            'surface': rotate(bdgf,-60),
            'position': [620, 25],
            'crossed': False },
            {
            'show': True,
            'angle':-70,
            'flip': True,
            'surface': flip(rotate(bdgf,-70), True, False),
            'position': [630, 350],
            'crossed': False },
            {
            'show': True,
            'angle':0,
            'flip': False,
            'surface': rotate(bdgf,0),
            'position': [500, 250],
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
    print([bridge['show'] for bridge in bridges])
    print(type(player_score), player_score)
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

    if player_score >= 6:
        text_surface = font_over.render("GAME OVER", True, color_red)
        screen.blit(text_surface , (100,200))
        running = button(350,350,100,50,color_red)
        quit_surface = game_font.render("QUIT", True, color_black)
        screen.blit(quit_surface , (365,365))


    # Show score
    player_score_surface = "Pontuação: " + str(player_score)
    score_surface = small_font.render(player_score_surface, False, color_black)
    screen.blit(score_surface , (0,0))

    #Restart Button
    reset_game = not button(650,0,77,35,color_green)
    start_surface = small_font.render("RESET", True, color_black)
    screen.blit(start_surface , (655,10))
    if reset_game:
        bridges = brdg()

    # Player location
    player['position'][0] += player['speed']['x']
    player['position'][1] += player['speed']['y']
    screen.blit(player['surface'], player['position'])

    # Restart game
    player['speed'] = {'x': 0, 'y': 0}
    pygame.display.update()
    clock.tick(30)
