import game_framework
import main_game

from pico2d import *

name = "game_over"
image = None
count = 0


def enter():
    global image
    image = load_image('image\GAMEOVER\overimage.png')


def exit():
    pass

def pause():
    pass


def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
                game_framework.change_state(main_game)


def update():
    pass


def draw():
    global image
    clear_canvas()
    main_game.draw_main_scene()

    image.draw(225, 375)
    update_canvas()


