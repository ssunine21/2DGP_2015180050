from pico2d import *
import choice_state
import main_game
import ITEM


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
        if self.skill_frame >= 5:
            self.skill_frame = 5

        if self.skill_Trigger == 1:
            if choice_state.CHAR_choice == 0:
                main_game.hp_gauge.frame -= 50
                self.skill_frame = 0
                self.skill_Trigger = 0

            elif choice_state.CHAR_choice == 1:
                ITEM.protect_State = 3
                self.skill_frame = 0
                self.skill_Trigger = 0

    def handle_skill(self):
        if self.skill_frame >= 5:
            self.skill_Trigger = 1