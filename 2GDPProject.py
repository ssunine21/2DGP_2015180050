from pico2d import *

class MAP:
    def __init__(self):
        self.x, self.y = 225, 600
        self.image = load_image('image\MAP\MAP(STAGE1)_450x750.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_move(self):
        self.y -= 150


class CHAR:
    image = None
    LEFT_RUN, RIGHT_RUN = 0, 1

    def __init__(self):
        self.x, self.y = 225, 70
        self.state = self.LEFT_RUN

        if CHAR.image == None:
            CHAR.image = load_image('image\CHARACTER\character.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_left_run(self):
        if self.x == 75:
            self.x = 375
        else:
            self.x -= 150
        Map.handle_move()

    def handle_right_run(self):
        if self.x == 375:
            self.x = 75
        else:
            self.x += 150
        Map.handle_move()

    def update(self):
        self.handle_state[self.state](self)

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
    }


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            Character.handle_left_run()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            Character.handle_right_run()

open_canvas(450, 750)
Character = CHAR()
Map = MAP()

running = True;

while running:
    handle_events()
    clear_canvas()

    Map.draw()
    Character.draw()
    update_canvas()

    delay(0.05)

close_canvas()