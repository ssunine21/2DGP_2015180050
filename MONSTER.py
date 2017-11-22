from pico2d import *
import main_game
import random
import SKILL

#Monster 위치값
positionX = 0
positionY = 0

M1image = None
M2image = None


class MONSTER:
    def __init__(self):
        # Monster 위치는 x(70, 220, 370), y(150단위에서 -60)
        global positionX, positionY, M1image
        self.x, self.y = 70, 240
        positionX += (random.randint(1, 3) * 150)
        positionY += (random.randint(1, 3) * 150)
        self.x += positionX
        self.y += positionY
        self.defaultY = self.y
        self.frame = random.randint(0, 7)
        self.frametime = 0

        if M1image == None:
            M1image = load_image('image\MONSTER\monster1_state.png')

    def handle_move(self, frame_time):
        distance = main_game.MAX_SPEED_PPS * frame_time

        self.y -= distance

        if main_game.Character.x % 150 == 75:
            self.defaultY -= 150
            self.y = self.defaultY

    def draw(self):
        # x와 y 위치를 랜덤으로 넣기
        while self.x > 370:
            self.x -= 450

        M1image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        for Mon in main_game.Monster:
            if Mon.y < 0 :
                main_game.Monster.remove(Mon)

            if main_game.collide(main_game.Character, Mon):
                main_game.Monster.remove(Mon)
                main_game.HP_gauge.frame -= 15
                main_game.skill.skill_frame += 1
        self.frametime += 1
        if self.frametime % 10 == 0:
            self.frame = (self.frame + 1) % 8

    def collision(self):
        return self.x - 22, self.y - 35, self.x + 22, self.y + 35

    def collision_box(self):
        draw_rectangle(*self.collision())


class MONSTER2:

    def __init__(self):
        #Monster 위치는 x(70, 220, 370), y(150단위에서 -60)
        global positionX, positionY, M2image
        self.x, self.y = 70, 1440
        positionX += (random.randint(1, 3) * 150)
        positionY += (random.randint(1, 3) * 150)
        self.x += positionX
        self.y += positionY
        self.defaultY = self.y
        self.attack = 0
        #frametimee은 몬스터가 너무 빨라서 만든거
        self.frame = random.randint(0, 7)
        self.frametime = 0

        if M2image == None:
            M2image = load_image('image\MONSTER\monster2_state.png')

    def handle_move(self, frame_time):
        distance = main_game.MAX_SPEED_PPS * frame_time

        self.y -= distance

        if main_game.Character.x % 150 == 75:
            self.defaultY -= 150
            self.y = self.defaultY

    def draw(self):
        #x와 y 위치를 랜덤으로 넣기
        while self.x > 370:
            self.x -= 450

        M2image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        for Mon in main_game.Monster2:
            if Mon.y < 0:
                main_game.Monster2.remove(Mon)

            if main_game.collide(main_game.Character, Mon):
                main_game.Monster2.remove(Mon)
                for ATK in main_game.M2_ATTACK:
                    if ATK.y == Mon.y:
                        main_game.M2_ATTACK.remove(ATK)
                main_game.HP_gauge.frame -= 15
                main_game.skill.skill_frame += 1
        self.frametime += 1
        if self.frametime % 10 == 0:
            self.frame = (self.frame + 1) % 8

    def collision(self):
        return self.x - 22, self.y -35, self.x + 22, self.y + 35

    def collision_box(self):
        draw_rectangle(*self.collision())

