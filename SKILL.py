from pico2d import *
import main_game


class Skill:
    image = None

    def __init__(self):
        self.x, self.y = 405, 60

        self.skill_Trigger = 0
        self.skill_frame = 0

        if Skill.image == None:
            Skill.image = load_image('image\SKILL\skill_state.png')

    def draw(self):
        self.image.clip_draw(self.skill_frame * 60, 0, 60, 60, self.x, self.y)

    def update(self, frame_time):
        if self.skill_frame > 5:
            self.skill_frame = 5

        if self.skill_Trigger == 1:
            main_game.stage1_map.handle_move(frame_time)
            main_game.stage2_map.handle_move(frame_time)
            main_game.stage3_map.handle_move(frame_time)

            for Mon in main_game.stage1_monster:
                Mon.handle_move(frame_time)

            for Mon in main_game.stage2_monster:
                Mon.handle_move(frame_time)

            for Mon in main_game.stage3_monster:
                Mon.handle_move(frame_time)

            for ATK in main_game.stage2_monster_attack:
                if ATK.ATTACK == 1:
                    ATK.attack_move(frame_time)
                else:
                    ATK.handle_move(frame_time)

            for Trp in main_game.stage2_trap:
                Trp.handle_move(frame_time)

            self.skill_frame -= 1

        if self.skill_frame == 0:
            self.skill_Trigger = 0

    def handel_skill(self):
        if self.skill_frame == 3:
            self.skill_Trigger = 1