from pico2d import *
import main_game
import game_framework
import game_over
import random
import ITEM

monster_Counter = 0


class Stage2_Attack:
    image = None
    stage2_attack_sound = None

    def __init__(self):
        global monster_Counter
        self.x = main_game.stage2_monster[monster_Counter].x
        self.y = main_game.stage2_monster[monster_Counter].y
        self.defaultY = self.y

        #공격 트리거
        self.ATTACK = 0
        monster_Counter = (monster_Counter + (random.randint(1, 3))) % 20

        if Stage2_Attack.image == None:
            Stage2_Attack.image = load_image('image\MONSTER_ATTACK\monster2_attack.png')

        if Stage2_Attack.stage2_attack_sound == None:
            Stage2_Attack.stage2_attack_sound = load_wav('music\stage2_monster_attack.wav')
            Stage2_Attack.stage2_attack_sound.set_volume(5)

    def eat(self):
        self.stage2_attack_sound.play()

    def handle_move(self, frame_time):
        distance = main_game.MAX_SPEED_PPS * frame_time

        self.y -= distance

        if main_game.girl.x % 150 == 75:
            self.defaultY -= 150
            self.y = self.defaultY

    def attack_move(self, frame_time):
        distance_attack = main_game.MAX_SPEED_PPS * frame_time
        self.y -= distance_attack

    def draw(self):
        # x와 y 위치를 랜덤으로 넣기
        while self.x > 370:
            self.x -= 450

        self.image.draw(self.x, self.y)

    def update(self, frame_time):
        for ATK in main_game.stage2_monster_attack:
            if main_game.collide(main_game.girl, ATK):
                ATK.eat()
                ATK.ATTACK = 1
        for ATK in main_game.stage2_monster_attack:
            if ATK.ATTACK == 1:
                ATK.y -= main_game.MAX_SPEED_PPS * frame_time * 0.05
                if self.attack_collide(ATK, main_game.girl):
                    if ITEM.protect_State == 1:
                        ITEM.protect_State = 0
                        main_game.stage2_monster_attack.remove(ATK)
                    else:
                        game_framework.push_state(game_over)
                        pass

    def collision(self):
        return self.x - 2, self.y - 350, self.x + 2, self.y + 20

    def attack_triger(self):
        return self.x - 3, self.y - 17, self.x + 3, self.y + 10

    def collision_box(self):
        draw_rectangle(*self.collision())
        draw_rectangle(*self.attack_triger())

    def attack_collide(self, a, b):
        left_a, bottom_a, right_a, top_a = a.attack_triger()
        left_b, bottom_b, right_b, top_b = b.collision()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False

        return True


class Stage3_Attack:
    image = None
    stage3_attack_sound = None

    def __init__(self):
        global monster_Counter
        self.x = main_game.stage3_monster[monster_Counter].x
        self.y = main_game.stage3_monster[monster_Counter].y
        self.defaultY = self.y

        # 공격 트리거
        self.ATTACK = 0
        monster_Counter = (monster_Counter + (random.randint(1, 3))) % 20

        if Stage3_Attack.image == None:
            Stage3_Attack.image = load_image('image\MONSTER_ATTACK\monster3_attack.png')

        if Stage3_Attack.stage3_attack_sound == None:
            Stage3_Attack.stage3_attack_sound = load_wav('music\stage3_monster_attack.wav')
            Stage3_Attack.stage3_attack_sound.set_volume(20)

    def eat(self):
        self.stage3_attack_sound.play()

    def handle_move(self, frame_time):
        distance = main_game.MAX_SPEED_PPS * frame_time

        self.y -= distance

        if main_game.girl.x % 150 == 75:
            self.defaultY -= 150
            self.y = self.defaultY

    def attack_move(self, frame_time):
        distance_attack = main_game.MAX_SPEED_PPS * frame_time
        self.y -= distance_attack

    def draw(self):
        # x와 y 위치를 랜덤으로 넣기
        while self.x > 370:
            self.x -= 450

        self.image.draw(self.x, self.y)

    def update(self, frame_time):
        for ATK in main_game.stage3_monster_attack:
            if main_game.collide(main_game.girl, ATK):
                ATK.eat()
                ATK.ATTACK = 1

        for ATK in main_game.stage3_monster_attack:
            if ATK.ATTACK == 1:
                ATK.y -= main_game.MAX_SPEED_PPS * frame_time * 0.05
                if self.attack_collide(ATK, main_game.girl):
                    if ITEM.protect_State == 1:
                        ITEM.protect_State = 0
                        main_game.stage3_monster_attack.remove(ATK)
                    else:
                        game_framework.push_state(game_over)
                        pass


    def collision(self):
        return self.x - 2, self.y - 350, self.x + 2, self.y + 20

    def attack_triger(self):
        return self.x - 3, self.y - 17, self.x + 3, self.y + 10

    def collision_box(self):
        draw_rectangle(*self.collision())
        draw_rectangle(*self.attack_triger())

    def attack_collide(self, a, b):
        left_a, bottom_a, right_a, top_a = a.attack_triger()
        left_b, bottom_b, right_b, top_b = b.collision()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False

        return True