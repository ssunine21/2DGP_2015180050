from pico2d import *
import main_game

image = None


def handle_skill(frame_time):
    count = 1
    if len(main_game.Monster) != 0:
        while (count > 1):
            # 모든 몬스터와 함정이 앞으로 당겨짐
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

            main_game.Character.x = main_game.Monster[0].x


        if 65 < main_game.Character.x < 85:
            main_game.Character.x = 75
        elif 215 < main_game.Character.x < 235:
            main_game.Character.x = 225
        else:
            main_game.Character.x = 375

    elif len(main_game.Monster2) != 0:
        main_game.Character.y = main_game.Monster2[0].y
        main_game.Character.x = main_game.Monster2[0].x


class SKILL:
    def __init__(self):
        global image
        self.x, self.y = 405, 60

        self.skill_frame = 0

        if image == None:
            image = load_image('image\SKILL\skill_state.png')

    def draw(self):
        image.clip_draw(self.skill_frame * 60, 0, 60, 60, self.x, self.y)

    def update(self):
        if self.skill_frame > 5:
            self.skill_frame = 5

