import main_game
from pico2d import *

image = None


class CHAR:
    positionX1 = 1
    positionX2 = 2
    positionX3 = 3
    position = positionX2

    LEFT_RUN, RIGHT_RUN = 0, 1

    def __init__(self):
        global image
        self.x, self.y = 225, 70

        #state는 이미지 위치 way는 캐릭터방향
        self.state = 0
        self.way = 0
        #frametime은 캐릭터가 너무 빨라서만든거
        self.frame = 0
        self.frametime = 0
        self.sidestep = 0

        if image == None:
            image = load_image('image\CHARACTER\character_state.png')

    def draw(self):
        image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

    def handle_left_jump(self, frame_time):

        distance = main_game.MAX_SPEED_PPS * frame_time

        self.x -= distance

        if self.position == self.positionX2:
            if self.x < 75:
                self.x = 75
                self.position = self.positionX1
                self.way = 0

        elif self.position == self.positionX1:
            if self.x <= 0:
                self.x = 450
                self.sidestep = 1
            elif self.x < 375 and self.sidestep == 1:
                self.x = 375
                self.position = self.positionX3
                self.way = 0
                self.sidestep = 0

        elif self.position == self.positionX3:
            if self.x < 225:
                self.x = 225
                self.position = self.positionX2
                self.way = 0

        main_game.Map1.handle_move(frame_time)
        main_game.Map2.handle_move(frame_time)
        main_game.Map3.handle_move(frame_time)

        #모든 몬스터와 함정이 앞으로 당겨짐
        for Mon in main_game.Monster:
            Mon.handle_move(frame_time)

        for Mon in main_game.Monster2:
            Mon.handle_move(frame_time)

        for Mon in main_game.Monster3:
            Mon.handle_move(frame_time)

        for ATK in main_game.M2_ATTACK:
            if ATK.ATTACK == 1:
                ATK.attack_move(frame_time)
            else:
                ATK.handle_move(frame_time)

        for Trp in main_game.Trap:
            Trp.handle_move(frame_time)

        #캐릭터 움직임
        self.frame = 0
        self.state = 2

    def handle_right_jump(self, frame_time):

        distance = main_game.MAX_SPEED_PPS * frame_time

        self.x += distance

        if self.position == self.positionX2:
            if self.x > 375:
                self.x = 375
                self.position = self.positionX3
                self.way = 0

        elif self.position == self.positionX3:
            if self.x >= 450:
                self.x = 0
                self.sidestep = 1
            elif 75 < self.x and self.sidestep == 1:
                self.x = 75
                self.position = self.positionX1
                self.sidestep = 0
                self.way = 0

        elif self.position == self.positionX1:
            if self.x > 225:
                self.x = 225
                self.position = self.positionX2
                self.way = 0

        main_game.Map1.handle_move(frame_time)
        main_game.Map2.handle_move(frame_time)
        main_game.Map3.handle_move(frame_time)

        #모든 몬스터와 함정이 앞으로 당겨짐
        for Mon in main_game.Monster:
            Mon.handle_move(frame_time)

        for Mon in main_game.Monster2:
            Mon.handle_move(frame_time)

        for Mon in main_game.Monster3:
            Mon.handle_move(frame_time)

        for ATK in main_game.M2_ATTACK:
            if ATK.ATTACK == 1:
                ATK.attack_move(frame_time)
            else:
                ATK.handle_move(frame_time)

        for Trp in main_game.Trap:
            Trp.handle_move(frame_time)

        #캐릭터 움직임
        self.frame = 0
        self.state = 3


    def update(self, frame_time):
        if self.way == 1:
            main_game.Character.handle_left_jump(frame_time)
        elif self.way == 2:
            main_game.Character.handle_right_jump(frame_time)

        self.frametime += 1
        if self.frametime % 3 == 0:
            if self.frame < 6:
                self.frame = (self.frame + 1)
            else:
                self.frame = 6

    def collision(self):
        return self.x - 13, self.y - 20, self.x + 13, self.y + 10

    def collision_box(self):
        draw_rectangle(*self.collision())