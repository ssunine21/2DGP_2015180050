import game_framework
import main_game
from pico2d import *

name = "game_over"
image = None
count = 0


def enter():
    global image
    image = load_image('image\GAMEOVER\game_over.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                pass
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()
                game_framework.push_state(main_game)


def update():
    pass


def draw():
    global image
    clear_canvas()
    main_game.draw_main_scene()

    image.draw(225, 375)
    update_canvas()


