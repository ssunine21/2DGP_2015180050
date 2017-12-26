import game_framework
import main_game
import title_state

from pico2d import *

name = "StopState"

font = None
image = None
frame = 0


def enter():
    global image, font
    image = load_image('image\start\stop.png')

    if font == None:
        font = load_font('image\BAUHS93.TTF', 40)


def exit():
    pass

def pause():
    pass


def resume():
    pass

def handle_events():
    global frame

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.pop_state()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
                if frame == 0:
                    title_state.choiceMusic()
                    game_framework.pop_state()
                elif frame == 1:
                    title_state.choiceMusic()
                    game_framework.change_state(main_game)
                else:
                    game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                title_state.selectMusic()
                if frame > 0:
                    frame -= 1
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                title_state.selectMusic()
                if frame < 2:
                    frame += 1


def update():
    pass


def draw():
    global image
    clear_canvas()
    main_game.draw_main_scene()

    image.clip_draw(frame * 450, 0, 450, 750, 225, 375)
    font.draw(100, 420, 'Score : %d' %main_game.score, (255, 255, 255))
    update_canvas()


