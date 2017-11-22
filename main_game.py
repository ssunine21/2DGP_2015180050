import game_framework
import game_over

import CHAR
import MAP
import GAUGE
from SKILL import SKILL
from MONSTER import MONSTER, MONSTER2
from TRAP import TRAP
from ATTACK import ATTACK1


from pico2d import *

name = "main_game"

#SPEED
MAX_SPEED_PPS = 1000

#난이도
Level = 0


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.collision()
    left_b, bottom_b, right_b, top_b = b.collision()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True


#시간================================
current_time = 0.0


def get_frame_time():
    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


#====================================
Character = None
Monster = None
Monster2 = None
M2_ATTACK = None
Trap = None
Map1 = None
Map2 = None
Map3 = None
HP_gauge = None
skill = None


def enter():
    global Character, Monster, Monster2, Trap, Map1, Map2, Map3, HP_gauge, M2_ATTACK, skill
    global current_time

    Character = CHAR.CHAR()
    skill = SKILL()

    Monster = [MONSTER() for i in range(20)]
    Monster2 = [MONSTER2() for i in range(20)]
    M2_ATTACK = [ATTACK1() for i in range(10)]

    Trap = [TRAP() for i in range(13)]

    Map1 = MAP.MAP1()
    Map2 = MAP.MAP2()
    Map3 = MAP.MAP3()
    HP_gauge = GAUGE.gauge()

    current_time = get_time()


def exit():
    global Character, Monster, Monster2, Trap, Map1, Map2, Map3, HP_gauge, M2_ATTACK, skill

    del(Character)
    del(skill)
    del(Monster)
    del(Monster2)
    del(Trap)
    del(Map1)
    del(Map2)
    del(Map3)
    del(HP_gauge)
    del(M2_ATTACK)

def pause():
    pass


def resume():
    pass


def handle_events():
    global Level

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if Character.way == 2:
                pass
            else:
                Character.way = 1
                Level += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if Character.way == 1:
                pass
            else:
                Character.way = 2
                Level += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_x):
            Character.handle_skill()
            skill.skill_frame = 0


def update():
    global Monster, Monster2, Trap

    frame_time = get_frame_time()

    # Update =============================
    Character.update(frame_time)

    for Mon in Monster:
        Mon.update()
    for Mon in Monster2:
        Mon.update()
    for ATK in M2_ATTACK:
        ATK.update(frame_time)

    for Trp in Trap:
        Trp.update()

    HP_gauge.update()
    skill.update()
    # ====================================


def draw_main_scene():
    global Monster, Monster2, Trap
    # Draw ===============================
    Map1.draw()
    Map2.draw()
    Map3.draw()

    Character.draw()

    for Mon in Monster:
        Mon.draw()
    for Mon in Monster2:
        Mon.draw()

    for ATK in M2_ATTACK:
        ATK.draw()

    for Trp in Trap:
        Trp.draw()

    HP_gauge.draw()
    skill.draw()

    Character.collision_box()

    #for Mon in Monster:
    #    Mon.collision_box()

    #for Mon in Monster2:
    #    Mon.collision_box()

    #for ATK in M2_ATTACK:
    #    ATK.collision_box()
    # ====================================


def draw():
    clear_canvas()
    draw_main_scene()
    update_canvas()