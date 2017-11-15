from pico2d import *
import random


#Monster 위치값
positionX = 0
positionY = 0

#Trap 위치값
TRAP_positionX = 0
TRAP_positionY = 0

#SPEED
MAX_SPEED_PPS = 1000

#난이도
Level = 0

class MAP1:
    global MAX_SPEED_PPS

    def __init__(self):
        self.x, self.y = 225, 3600
        self.defaultY = self.y
        self.image = load_image('image\MAP\MAP(STAGE1)_450x750.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_move(self):
        distance = MAX_SPEED_PPS * frame_time

        self.y += (distance * -1)

        if self.y < (self.defaultY - 150):
            self.defaultY -= 150
            self.y = self.defaultY


class MAP2:
    global MAX_SPEED_PPS

    def __init__(self):
        self.x, self.y = 225, 10800
        self.defaultY = self.y
        self.image = load_image('image\MAP\MAP(STAGE2)_450x750.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_move(self):
        distance = MAX_SPEED_PPS * frame_time

        self.y += (distance * -1)

        if self.y < (self.defaultY - 150):
            self.defaultY -= 150
            self.y = self.defaultY


class CHAR:
    global MAX_SPEED_PPS
    positionX1 = 1
    positionX2 = 2
    positionX3 = 3
    position = positionX2

    image = None
    LEFT_RUN, RIGHT_RUN = 0, 1

    def __init__(self):
        self.x, self.y = 225, 70
        #state는 이미지 위치 way는 캐릭터방향
        self.state = 0
        self.way = 0
        self.frame = 0

        # 캐릭터 위치값
        self.Cposition = 0

        if CHAR.image == None:
            CHAR.image = load_image('image\CHARACTER\character_state.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

    def handle_left_jump(self, frame_time):

        distance = MAX_SPEED_PPS * frame_time

        self.x += (distance * -1)

        if self.position == self.positionX2:
            if self.x < 75:
                self.x = 75
                self.position = self.positionX1
                self.way = 0

        elif self.position == self.positionX1:
            if self.x < 0:
                self.x = 400
            elif 300 < self.x < 375:
                self.x = 375
                self.position = self.positionX3
                self.way = 0

        elif self.position == self.positionX3:
            if self.x < 225:
                self.x = 225
                self.position = self.positionX2
                self.way = 0

        Map1.handle_move()
        Map2.handle_move()

        #모든 몬스터가 앞으로 당겨짐
        for Mon in Monster:
            Mon.handle_move()

        for Mon in Monster2:
            Mon.handle_move()


        #HP게이지 충전, Monster생성하면 삭제하기
        #HP_gauge.frame -= 5
        #if HP_gauge.frame < 0:
        #    HP_gauge.frame = 1

        #캐릭터 움직임
        self.frame = 0
        self.state = 2

    def handle_right_jump(self, frame_time):

        distance = MAX_SPEED_PPS * frame_time

        self.x += (distance)

        if self.position == self.positionX2:
            if self.x > 375:
                self.x = 375
                self.position = self.positionX3
                self.way = 0

        elif self.position == self.positionX3:
            if self.x > 450:
                self.x = 50
            elif 75 < self.x < 110:
                self.x = 75
                self.position = self.positionX1
                self.way = 0

        elif self.position == self.positionX1:
            if self.x > 225:
                self.x = 225
                self.position = self.positionX2
                self.way = 0

        Map1.handle_move()
        Map2.handle_move()

        #모든 몬스터가 앞으로 당겨짐
        for Mon in Monster:
            Mon.handle_move()

        for Mon in Monster2:
            Mon.handle_move()


        # HP게이지 충전, Monster생성하면 삭제하기
        #HP_gauge.frame -= 5
        #if HP_gauge.frame < 0:
        #    HP_gauge.frame = 1


        #캐릭터 움직임
        self.frame = 0
        self.state = 3

    def update(self):
        if self.way == 1:
            Character.handle_left_jump(frame_time)
        elif self.way == 2:
            Character.handle_right_jump(frame_time)

        if self.frame < 6:
            self.frame = (self.frame + 1)
        else:
            self.frame = 6

    def collision(self):
        return self.x - 18, self.y - 36, self.x + 18, self.y + 36

    def collision_box(self):
        draw_rectangle(*self.collision())



class MONSTER:
    global MAX_SPEED_PPS
    image = None

    def __init__(self):
        #Monster 위치는 x(70, 220, 370), y(150단위에서 -60)
        global positionX, positionY
        self.x, self.y = 70, 240
        positionX += (random.randint(1, 3) * 150)
        positionY += (random.randint(1, 3) * 150)
        self.x += positionX
        self.y += positionY
        self.defaultY = self.y
        self.frame = 0

        if MONSTER.image == None:
            MONSTER.image = load_image('image\MONSTER\monster1_state.png')

    def handle_move(self):
        distance = MAX_SPEED_PPS * frame_time

        self.y += (distance * -1)

        if self.y < (self.defaultY - 150):
            self.defaultY -= 150
            self.y = self.defaultY

    def draw(self):
        #x와 y 위치를 랜덤으로 넣기
        while self.x > 370:
            self.x -= 450

        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8


    def collision(self):
        return self.x - 22, self.y -35, self.x + 22, self.y + 35

    def collision_box(self):
        draw_rectangle(*self.collision())


class MONSTER2:
    global MAX_SPEED_PPS
    image = None

    def __init__(self):
        #Monster 위치는 x(70, 220, 370), y(150단위에서 -60)
        global positionX, positionY
        self.x, self.y = 70, 990
        positionX += (random.randint(1, 3) * 150)
        positionY += (random.randint(1, 3) * 150)
        self.x += positionX
        self.y += positionY
        self.defaultY = self.y
        self.frame = 0

        if MONSTER2.image == None:
            MONSTER2.image = load_image('image\MONSTER\monster2_state.png')

    def handle_move(self):
        distance = MAX_SPEED_PPS * frame_time

        self.y += (distance * -1)

        if self.y < (self.defaultY - 150):
            self.defaultY -= 150
            self.y = self.defaultY

    def draw(self):
        #x와 y 위치를 랜덤으로 넣기
        while self.x > 370:
            self.x -= 450

        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8


    def collision(self):
        return self.x - 22, self.y -35, self.x + 22, self.y + 35

    def collision_box(self):
        draw_rectangle(*self.collision())

class TRAP:
    global MAX_SPEED_PPS
    image = None

    def __init__(self):
        global TRAP_positionX, TRAP_positionY
        self.x, self.y = 70, 7500
        TRAP_positionX += (random.randint(1, 3) * 150)
        TRAP_positionY += (random.randint(1, 3) * 150)
        self.x += TRAP_positionX
        self.y += TRAP_positionY
        self.defaultY = self.y

        if TRAP.image == None:
            TRAP.image = load_image('image\TRAP\trap.png')

    def handle_move(self):
        distance = MAX_SPEED_PPS * frame_time

        self.y += (distance * -1)

        if self.y < (self.defaultY - 150):
            self.defaultY -= 150
            self.y = self.defaultY

    def draw(self):
        #x와 y 위치를 랜덤으로 넣기
        while self.x > 370:
            self.x -= 450

        self.image.draw(self.x, self.y)

    def update(self):
        pass


    def collision(self):
        return self.x - 70, self.y -70, self.x + 70, self.y + 70

    def collision_box(self):
        draw_rectangle(*self.collision())


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
        global running, Level

        if self.frame < 0:
            self.frame = 0
        #HP속도조절
        if Level < 48:
            if self.count % 8 == 0:
                if self.frame < 99:
                    self.frame = (self.frame + 1)
                else:
                    pass
                    #running = False
            self.count = self.count + 1
        elif Level < 150:
            if self.count % 2 == 0:
                if self.frame < 99:
                    self.frame = (self.frame + 1)
                else:
                    pass
                    #running = False
            self.count = self.count + 1


def handle_events():
    global running, Level
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
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

def Update():
    pass

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

current_time = get_time()

#====================================
open_canvas(450, 750)

Character = CHAR()

Monster = [MONSTER() for i in range(19)]
Monster2 = [MONSTER2() for i in range(20)]

Trap = TRAP()

Map1 = MAP1()
Map2 = MAP2()
HP_gauge = gauge()

running = True;

while running:
    handle_events()
    clear_canvas()

    frame_time = get_frame_time()

#Update======================
    Update()

    Character.update()
    Trap.update()

    for Mon in Monster:
        Mon.update()

    for Mon in Monster:
        if collide(Character, Mon):
            Monster.remove(Mon)
            HP_gauge.frame -= 15

    for Mon in Monster2:
        Mon.update()

    for Mon in Monster2:
        if collide(Character, Mon):
            Monster2.remove(Mon)
            HP_gauge.frame -= 15

    HP_gauge.update()
    #========================



    #Draw========================
    Map1.draw()
    Map2.draw()

    Character.draw()
    Trap.draw()

    for Mon in Monster:
        Mon.draw()

    for Mon in Monster2:
        Mon.draw()

    HP_gauge.draw()

    Character.collision_box()
    for Mon in Monster:
        Mon.collision_box()

    for Mon in Monster2:
        Mon.collision_box()
    #========================

    update_canvas()

    delay(0.05)

close_canvas()