from pico2d import *
import random

class MAP:
    def __init__(self):
        self.x, self.y = 225, 2400
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
        self.state = 0
        self.frame = 0

        if CHAR.image == None:
            CHAR.image = load_image('image\CHARACTER\character_state.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

    def handle_left_jump(self):
        if self.x == 75:
            self.x = 375
        else:
            self.x -= 150
        Map.handle_move()

        #모든 몬스터가 앞으로 당겨짐
        for Mon in Monster:
            Mon.handle_move()

        #HP게이지 충전, Monster생성하면 삭제하기
        #HP_gauge.frame -= 5
        #if HP_gauge.frame < 0:
        #    HP_gauge.frame = 1

        #캐릭터 움직임
        self.frame = 0
        self.state = 2

    def handle_right_jump(self):
        if self.x == 375:
            self.x = 75
        else:
            self.x += 150
        Map.handle_move()

        #모든 몬스터가 앞으로 당겨짐
        for Mon in Monster:
            Mon.handle_move()


        # HP게이지 충전, Monster생성하면 삭제하기
        #HP_gauge.frame -= 5
        #if HP_gauge.frame < 0:
        #    HP_gauge.frame = 1


        #캐릭터 움직임
        self.frame = 0
        self.state = 3

    def update(self):
        if self.frame < 6:
            self.frame = (self.frame + 1)
        else:
            self.frame = 6


class MONSTER:
    image = None

    def __init__(self):
        #Monster 위치는 x(70, 220, 370), y(150단위에서 -60)
        self.x, self.y = 220, 540
        self.frame = 0

        if MONSTER.image == None:
            MONSTER.image = load_image('image\MONSTER\monster_state.png')

    def handle_move(self):
        self.y -= 150

    def draw(self):
        #x와 y 위치를 랜덤으로 넣기
        #self.x += (random.randint(0, 2) * 150)
        #if self.x > 370:
        #    self.x -= 450

        #self.y += (random.randint(1, 3) * 150)
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def updata(self):
        self.frame = (self.frame + 1) % 8

        #Monster와 char가 충돌할 때
        for Mon in Monster:
            if (Mon.x - 30) < Character.x and (Mon.x + 30) > Character.x and (Mon.y - 30) < Character.y and (Mon.y + 30) > Character.y:
                Monster.remove(Mon)
                HP_gauge.frame -= 20
                if HP_gauge.frame < 0:
                    HP_gauge.frame = 0


class gauge:
    def __init__(self):
        self.x, self.y = 35, 150
        self.frame = 0

        #count는 HP속도 조절
        self.count = 0
        self.HP_gauge = load_image('image\GAUGE\HP_gauge.png')

    def draw(self):
        self.HP_gauge.clip_draw(self.frame * 30, 0, 30, 230, self.x, self.y)

    def update(self):
        global running

        #HP속도조절
        if self.count % 2 == 0:
            if self.frame < 99:
                self.frame = (self.frame + 1)
            else:
                pass
                running = False
        self.count = self.count + 1


def Update():
    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            Character.handle_left_jump()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            Character.handle_right_jump()


open_canvas(450, 750)
Character = CHAR()
Monster = [MONSTER() for i in range(1)]
Map = MAP()
HP_gauge = gauge()

running = True;

while running:
    handle_events()
    clear_canvas()

#Update======================
    Update()

    Character.update()
    for Mon in Monster:
        Mon.updata()
    HP_gauge.update()
    #========================



#Draw========================
    Map.draw()

    Character.draw()
    for Mon in Monster:
        Mon.draw()
    HP_gauge.draw()
    #========================

    update_canvas()

    delay(0.05)

close_canvas()