import main_game
from handle_Move_All import handle_move_GIRL
from pico2d import *


class Girl:

    LEFT_RUN, RIGHT_RUN = 0, 1
    image = None

    def __init__(self):
        self.x, self.y = 225, 70
        self.positionX = 1

        #state는 이미지 위치 way는 캐릭터방향
        self.state = 0
        self.way = 0

        #girl_frame_speed은 캐릭터가 너무 빨라서만든거
        self.frame = 0
        self.girl_frame_speed = 0

        #sidestep는 밖으로 나갈 때 캐릭터의 자연스러운 움직임을 위해서
        self.sidestep = 0

        if Girl.image == None:
            Girl.image = load_image('image\CHARACTER\character_state.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

    def handle_left_jump(self, frame_time):

        distance = main_game.MAX_SPEED_PPS * frame_time

        self.x -= distance

        if self.positionX == 1:
            if self.x < 75:
                self.x = 75
                self.positionX = 0
                self.way = 0

        elif self.positionX == 0:
            if self.x <= 0:
                self.x = 450
                self.sidestep = 1

            elif self.x < 375 and self.sidestep == 1:
                self.x = 375
                self.positionX = 2
                self.way = 0
                self.sidestep = 0

        elif self.positionX == 2:
            if self.x < 225:
                self.x = 225
                self.positionX = 1
                self.way = 0

        handle_move_GIRL(frame_time)

        #캐릭터 움직임
        self.frame = 0
        self.state = 2

    def handle_right_jump(self, frame_time):

        distance = main_game.MAX_SPEED_PPS * frame_time

        self.x += distance

        if self.positionX == 1:
            if self.x > 375:
                self.x = 375
                self.positionX = 2
                self.way = 0

        elif self.positionX == 2:
            if self.x >= 450:
                self.x = 0
                self.sidestep = 1

            elif 75 < self.x and self.sidestep == 1:
                self.x = 75
                self.positionX = 0
                self.sidestep = 0
                self.way = 0

        elif self.positionX == 0:
            if self.x > 225:
                self.x = 225
                self.positionX = 1
                self.way = 0

        handle_move_GIRL(frame_time)

        #캐릭터 움직임
        self.frame = 0
        self.state = 3

    def update(self, frame_time):
        if self.way == 1:
            main_game.girl.handle_left_jump(frame_time)
        elif self.way == 2:
            main_game.girl.handle_right_jump(frame_time)

        self.girl_frame_speed += 1
        if self.girl_frame_speed % 3 == 0:
            if self.frame < 6:
                self.frame = (self.frame + 1)
            else:
                self.frame = 6

    def collision(self):
        return self.x - 13, self.y - 20, self.x + 13, self.y + 10

    def collision_box(self):
        draw_rectangle(*self.collision())