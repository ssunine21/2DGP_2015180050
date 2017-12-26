import game_framework
import main_game
import title_state
from pico2d import *


name = "ChoiceState"
choice_image = None
boy_image = None
girl_image = None

frame_time = 0
CHAR_choice = 0
boy_frame = 0
girl_frame = 0


def enter():
    global choice_image, boy_image, girl_image
    choice_image = load_image('image\start\choice.png')
    boy_image = load_image('image\CHARACTER\CharPSD.png')
    girl_image = load_image('image\CHARACTER\girl_state.png')



def exit():
    global choice_image, boy_image, girl_image
    del(choice_image)
    del(boy_image)
    del(girl_image)


def handle_events():
    global CHAR_choice

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.pop_state()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                title_state.selectMusic()
                CHAR_choice = 0
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                title_state.selectMusic()
                CHAR_choice = 1
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
                title_state.choice_music.play()
                delay(0.5)
                game_framework.change_state(main_game)


def draw():
    global CHAR_choice

    clear_canvas()

    choice_image.clip_draw(CHAR_choice * 450, 0, 450, 750, 225, 375)
    boy_image.clip_draw(boy_frame*100, 300, 100, 100, 225, 460)
    girl_image.clip_draw(girl_frame*100, 300, 100, 100, 225, 230)
    update_canvas()


def update():
    global CHAR_choice, boy_frame, girl_frame, frame_time

    if frame_time % 40 == 0:
        if CHAR_choice == 0:
            if boy_frame < 6:
                boy_frame = (boy_frame + 1)
            else:
                boy_frame = 0

        if CHAR_choice == 1:
            if girl_frame < 6:
                girl_frame = (girl_frame + 1)
            else:
                girl_frame = 0
    frame_time += 1


def pause():
    pass


def resume():
    pass