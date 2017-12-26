import game_framework
import choice_state
import howtoplay
import main_game
import title_state
from pico2d import *


name = "VictoryState"
image = None
victory_music = None

frame = 0

def enter():
    global image, victory_music

    image = load_image('image\start\state_victory.png')
    victory_music = load_wav('music\music_victory.wav')

    victory_music.set_volume(30)
    victory_music.repeat_play()


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
                    title_state.choiceMusic()
                    game_framework.change_state(main_game)
                else:
                    game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                title_state.selectMusic()
                frame = 0
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                title_state.selectMusic()
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