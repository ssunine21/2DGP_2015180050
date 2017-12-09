import game_framework

import GIRL
import MAP
import GAUGE
import MONSTER
import TRAP

from SKILL import Skill
from ATTACK import Stage2_Attack, Stage3_Attack


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
frame_time = 0


def get_frame_time():
    global current_time, frame_time

    frame_time = get_time() - current_time
    current_time += frame_time

    return frame_time
#====================================


girl = None
stage1_monster = None
stage2_monster = None
stage3_monster = None

stage2_monster_attack = None
stage3_monster_attack = None

stage2_trap = None

stage1_map = None
stage2_map = None
stage3_map = None

hp_gauge = None

skill = None


def enter():
    global girl, stage1_monster, stage2_monster, stage3_monster, stage2_trap, stage1_map, stage2_map, stage3_map
    global hp_gauge, stage2_monster_attack, stage3_monster_attack, skill, current_time, Level

    #다시시작 할때를 위한 객체 위치 초기화
    MONSTER.monster_positionX = 0
    MONSTER.monster_positionY = 0
    TRAP.trap_positionX = 0
    TRAP.trap_positionY = 0
    Level = 0

    girl = GIRL.Girl()

    stage1_monster = [MONSTER.Stage1_Monster() for i in range(20)]
    stage2_monster = [MONSTER.Stage2_Monster() for i in range(20)]
    stage3_monster = [MONSTER.Stage3_Monster() for i in range(20)]

    stage2_monster_attack = [Stage2_Attack() for i in range(10)]
    stage3_monster_attack = [Stage3_Attack() for i in range(10)]

    stage2_trap = [TRAP.Trap() for i in range(13)]


    stage1_map = MAP.Map('image\MAP\MAP(STAGE1)_450x750.png', 225, 3600)
    stage2_map = MAP.Map('image\MAP\MAP(STAGE2)_450x750.png', 225, 10800)
    stage3_map = MAP.Map('image\MAP\MAP(STAGE3)_450x750.png', 225, 18000)

    hp_gauge = GAUGE.Gauge()
    skill = Skill()

    current_time = get_time()


def exit():
    global girl, stage1_monster, stage2_monster, stage3_monster, stage2_trap, stage1_map, stage2_map, stage3_map
    global hp_gauge, stage2_monster_attack, stage3_monster_attack, skill
    pass

def pause():
    pass


def resume():
    pass


def handle_events():
    global Level, frame_time

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if girl.way == 2:
                pass
            else:
                girl.way = 1
                Level += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if girl.way == 1:
                pass
            else:
                girl.way = 2
                Level += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_x):
            skill.handel_skill()


def update():
    global stage1_monster, stage2_monster, stage3_monster, stage2_trap, stage2_monster_attack, stage3_monster_attack, frame_time

    frame_time = get_frame_time()

    # Update =============================
    girl.update(frame_time)

    for Mon in stage1_monster:
        Mon.update()
    for Mon in stage2_monster:
        Mon.update()
    for Mon in stage3_monster:
        Mon.update()

    for ATK in stage2_monster_attack:
        ATK.update(frame_time)

    for ATK in stage3_monster_attack:
        ATK.update(frame_time)

    for Trp in stage2_trap:
        Trp.update()

    hp_gauge.update()
    skill.update(frame_time)
    # ====================================


def draw_main_scene():
    global stage1_monster, stage2_monster, stage3_monster, stage2_trap, stage2_monster_attack, stage3_monster_attack
    # Draw ===============================
    stage1_map.draw()
    stage2_map.draw()
    stage3_map.draw()

    girl.draw()

    for ATK in stage2_monster_attack:
        ATK.draw()
    for ATK in stage3_monster_attack:
        ATK.draw()

    for Mon in stage1_monster:
        Mon.draw()
    for Mon in stage2_monster:
        Mon.draw()
    for Mon in stage3_monster:
        Mon.draw()


    for Trp in stage2_trap:
        Trp.draw()

    hp_gauge.draw()
    skill.draw()

    girl.collision_box()

    #for Mon in Monster:
    #    Mon.collision_box()

    #for Mon in Monster2:
    #    Mon.collision_box()

    for Mon in stage3_monster:
        Mon.collision_box()

    for ATK in stage3_monster_attack:
        ATK.collision_box()
    # ====================================


def draw():
    clear_canvas()
    draw_main_scene()
    update_canvas()