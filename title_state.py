import game_framework
import choice_state
import howtoplay
from pico2d import *


name = "TitleState"
image = None
title_music = None
choice_music = None
select_music = None
over_music = None

frame = 0

def enter():
    global image, title_music, choice_music, select_music, over_music
    image = load_image('image\start\TS.png')
    title_music = load_music('music\stage1BGM.mp3')

    title_music.set_volume(20)
    title_music.repeat_play()

    choice_music = load_wav('music\choice.ogg')
    choice_music.set_volume(40)

    select_music = load_wav('music\select.wav')
    select_music.set_volume(45)

    over_music = load_wav('music\gameOver.wav')
    over_music.set_volume(30)


def choiceMusic():
    choice_music.play()

def selectMusic():
    select_music.play()

def gameoverMusic():
    over_music.play()


def exit():
    global image
    del(image)


def handle_events():
    global frame

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
                if frame == 0:
                    choiceMusic()
                    game_framework.push_state(choice_state)
                else:
                    choiceMusic()
                    game_framework.push_state(howtoplay)
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                selectMusic()
                frame = 0
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                selectMusic()
                frame = 1



def draw():
    clear_canvas()
    image.clip_draw(frame * 450, 0, 450, 750, 225, 375)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass