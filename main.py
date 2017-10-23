#! /usr/bin/env python
from random import randrange
import pygame
from pygame.locals import *
from pygame import *
from pygame.transform import *


pygame.init()
pygame.font.init()

# TODO: Add sounds
font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name, 72)

# Display size
screen = pygame.display.set_mode((800, 620))


background_filename = 'images/bg_c1.png'
background = image.load(background_filename).convert()
pygame.display.set_caption('Bridges')

player = {
    'surface': image.load('images/player3.png').convert_alpha(),
    'position': [10, 10],
    'speed': {
        'x': 0,
        'y': 0
    }
}

# exploded_ship = {
#     'surface': pygame.image.load('ship_exploded.png').convert_alpha(),
#     'position': [],
#     'speed': {
#         'x': 0,
#         'y': 0
#     },
#     'rect': Rect(0, 0, 48, 48)
# }

running = True
clock = pygame.time.Clock()
bridgef = image.load('images/bridge.png').convert_alpha()
bridgeft = image.load('images/bridge_transp.png').convert_alpha()
bridges = [{
        'angle':-60,
        'flip': False,
        'surface': rotate(bridgef,-60),
        'position': [150, 100],
        'crossed': False },
        {
        'angle': -40,
        'flip': True,
        'surface': flip(rotate(bridgef,-40), True, False),
        'position': [40, 300],
        'crossed': False },
        {
        'angle':-90,
        'flip': False,
        'surface': rotate(bridgef,-90),
        'position': [400, 340],
        'crossed': False },
        {
        'angle':-90,
        'flip': False,
        'surface': rotate(bridgef,-90),
        'position': [400, 60],
        'crossed': False },
        {
        'angle':-60,
        'flip': False,
        'surface': rotate(bridgef,-60),
        'position': [620, 25],
        'crossed': False },
        {
        'angle':-70,
        'flip': True,
        'surface': flip(rotate(bridgef,-70), True, False),
        'position': [630, 350],
        'crossed': False },
        {
        'angle':0,
        'flip': False,
        'surface': rotate(bridgef,0),
        'position': [500, 250],
        'crossed': False }
    ]
# ticks_to_asteroid = 90
# explosion_sound = pygame.mixer.Sound('boom.wav')
# explosion_played = False

#
# def move_asteroids():
#     for asteroid in asteroids:
#         asteroid['position'][1] += asteroid['speed']
#
# def remove_used_asteroids():
#     for asteroid in asteroids:
#         if asteroid['position'][1] > 560:
#             asteroids.remove(asteroid)
# ticks = 0
#

def get_rect(obj):
    return Rect(obj['position'][0],
                obj['position'][1],
                obj['surface'].get_width(),
                obj['surface'].get_height())

def get_b_rect(obj):
    print(obj['position'][0], obj['position'][1],obj['surface'].get_width(),obj['surface'].get_height())
    return Rect(obj['position'][0]+50,
                obj['position'][1]+50,
                obj['surface'].get_width()-50,
                obj['surface'].get_height()-50)

def bridge_crossed():
    person_rect = get_rect(player)
    for bridge in bridges:
        if person_rect.colliderect(get_b_rect(bridge)):
            bridge['crossed'] = True

# collided = False

# collision_animation_counter = 0

while running:
    # if ticks < ticks_to_asteroid:
    #     ticks += 1
    # else:
    #     ticks = 0
    #     asteroids.append(create_asteroid()).

    screen.blit(pygame.Surface(screen.get_size()), (0, 0))
    screen.blit(background, (0, 0))
    player_score = 0
    bridge_crossed()
    # remove_used_asteroids()
    # move_asteroids()
    for bridge in bridges:
        if not bridge['crossed']:
            screen.blit(bridge['surface'], bridge['position'])
        else:
            if bridge['flip']:
                bridge['surface'] = flip(rotate(bridgeft,bridge['angle']), True, False)
            else:
                bridge['surface'] = rotate(bridgeft,bridge['angle'])
            screen.blit(bridge['surface'], bridge['position'])
            player_score += 1
        if player_score == 6:
            textsurface = game_font.render("GAME OVER", False, (300,300, 300))
            screen.blit(textsurface , (0,0))


    # if not collided:
    #     collided = ship_collided()

    player_score = "Pontos : " + str(player_score)

    textsurface = game_font.render(player_score, False, (0, 0, 0))
    screen.blit(textsurface , (0,0))

    player['position'][0] += player['speed']['x']
    player['position'][1] += player['speed']['y']
    screen.blit(player['surface'], player['position'])
    # else:
    #     if not explosion_played:
    #         explosion_played = True
    #         explosion_sound.play()
    #         ship['position'][0] += ship['speed']['x']
    #         ship['position'][1] += ship['speed']['y']
    #
    #         screen.blit(ship['surface'], ship['position'])
    #     elif collision_animation_counter == 3:
    #         text = game_font.render('GAME OVER', 1, (255, 0, 0))
    #         screen.blit(text, (335, 250))
    #     else:
    #         exploded_ship['rect'].x = collision_animation_counter * 48
    #         exploded_ship['position'] = ship['position']
    #         screen.blit(exploded_ship['surface'], exploded_ship['position'],
    #                     exploded_ship['rect'])
    #         collision_animation_counter += 1
    pygame.display.update()

    player['speed'] = {'x': 0, 'y': 0}
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_UP]:
        player['speed']['y'] = -5
    elif pressed_keys[K_DOWN]:
        player['speed']['y'] = 5
    if pressed_keys[K_LEFT]:
        player['speed']['x'] = -5
    elif pressed_keys[K_RIGHT]:
        player['speed']['x'] = 5

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            pygame.display.quit()
            running = False
    clock.tick(30)
