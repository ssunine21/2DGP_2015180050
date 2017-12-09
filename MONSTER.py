from pico2d import *
import main_game
import random
import ATTACK

#Monster 위치값
monster_positionX = 0
monster_positionY = 0


class Stage1_Monster:
    image = None

    def __init__(self):
        global monster_positionX, monster_positionY
        # Monster 위치는 x(70, 220, 370), y(150단위에서 -60)
        self.x, self.y = 70, 240
        monster_positionX += (random.randint(1, 3) * 150)
        monster_positionY += (random.randint(1, 3) * 150)

        self.x += monster_positionX
        self.y += monster_positionY

        self.defaultY = self.y
        self.frame = random.randint(0, 7)

        #monster_frame_speed는 몬스터 그려지는 속도 조절을 위해 만듬
        self.monster_frame_speed = 0

        if Stage1_Monster.image == None:
            Stage1_Monster.image = load_image('image\MONSTER\monster1_state.png')

    def handle_move(self, frame_time):
        distance = main_game.MAX_SPEED_PPS * frame_time

        self.y -= distance

        if main_game.girl.x % 150 == 75:
            self.defaultY -= 150
            self.y = self.defaultY

    def draw(self):
        # x와 y 위치를 랜덤으로 넣기
        while self.x > 370:
            self.x -= 450

        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        for Mon in main_game.stage1_monster:
            if Mon.y < 0:
                main_game.stage1_monster.remove(Mon)

            if main_game.collide(main_game.girl, Mon):
                main_game.stage1_monster.remove(Mon)
                main_game.hp_gauge.frame -= 15
                main_game.skill.skill_frame += 1

        self.monster_frame_speed += 1

        if self.monster_frame_speed % 10 == 0:
            self.frame = (self.frame + 1) % 8

    def collision(self):
        return self.x - 22, self.y - 35, self.x + 22, self.y + 35

    def collision_box(self):
        draw_rectangle(*self.collision())


class Stage2_Monster:

    image = None

    def __init__(self):
        global monster_positionX, monster_positionY

        #Monster 위치는 x(70, 220, 370), y(150단위에서 -60)
        self.x, self.y = 70, 390
        monster_positionX += (random.randint(1, 3) * 150)
        monster_positionY += (random.randint(1, 4) * 150)

        self.x += monster_positionX
        self.y += monster_positionY
        self.defaultY = self.y
        self.attack = 0
        self.frame = random.randint(0, 7)

        #monster_frame_speed는 몬스터 그려지는 속도 조절을 위해 만듬
        self.monster_frame_speed = 0

        if Stage2_Monster.image == None:
            Stage2_Monster.image = load_image('image\MONSTER\monster2_state.png')

    def handle_move(self, frame_time):
        distance = main_game.MAX_SPEED_PPS * frame_time

        self.y -= distance

        if main_game.girl.x % 150 == 75:
            self.defaultY -= 150
            self.y = self.defaultY

    def draw(self):
        #x와 y 위치를 랜덤으로 넣기
        while self.x > 370:
            self.x -= 450

        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        for Mon in main_game.stage2_monster:
            if Mon.y < 0:
                main_game.stage2_monster.remove(Mon)

            if main_game.collide(main_game.girl, Mon):
                main_game.stage2_monster.remove(Mon)
                for ATK in main_game.stage2_monster_attack:
                    if ATK.y == Mon.y:
                        main_game.stage2_monster_attack.remove(ATK)
                main_game.hp_gauge.frame -= 15
                main_game.skill.skill_frame += 1
        self.monster_frame_speed += 1
        if self.monster_frame_speed % 10 == 0:
            self.frame = (self.frame + 1) % 8

    def collision(self):
        return self.x - 22, self.y -35, self.x + 22, self.y + 35

    def collision_box(self):
        draw_rectangle(*self.collision())


class Stage3_Monster:

    image = None

    def __init__(self):
        global monster_positionX, monster_positionY
        #Monster 위치는 x(70, 220, 370), y(150단위에서 -60)
        self.x, self.y = 60, 540
        monster_positionX += (random.randint(1, 3) * 150)
        monster_positionY += (random.randint(1, 3) * 150)
        self.x += monster_positionX
        self.y += monster_positionY
        self.defaultY = self.y
        self.attack = 0
        self.frame = random.randint(0, 7)

        #Stage3_Monster는 걷는 상태와 무기를 휘두르는 상태로 나뉨
        self.state = 1

        #monster_frame_speed는 몬스터 그려지는 속도 조절을 위해 만듬
        self.monster_frame_speed = 0

        if Stage3_Monster.image == None:
            Stage3_Monster.image = load_image('image\MONSTER\monster3_state.png')

    def handle_move(self, frame_time):
        distance = main_game.MAX_SPEED_PPS * frame_time

        self.y -= distance

        if main_game.girl.x % 150 == 75:
            self.defaultY -= 150
            self.y = self.defaultY

    def draw(self):
        #x와 y 위치를 랜덤으로 넣기
        while self.x > 370:
            self.x -= 450

        self.image.clip_draw(self.frame * 140, self.state * 140, 140, 140, self.x, self.y)

    def update(self):
        for Mon in main_game.stage3_monster:
            if Mon.y < 0:
                main_game.stage3_monster.remove(Mon)

            if main_game.collide(main_game.girl, Mon):
                main_game.stage3_monster.remove(Mon)
                for ATK in main_game.stage3_monster_attack:
                    if ATK.y == Mon.y:
                        main_game.stage3_monster_attack.remove(ATK)
                main_game.hp_gauge.frame -= 15
                main_game.skill.skill_frame += 1

        self.monster_frame_speed += 1
        if self.monster_frame_speed % 28 == 0:
            self.frame = (self.frame + 1) % 8

    def collision(self):
        return self.x - 22, self.y -45, self.x + 22, self.y + 35

    def collision_box(self):
        draw_rectangle(*self.collision())