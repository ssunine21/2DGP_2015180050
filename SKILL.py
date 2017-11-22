from pico2d import *

image = None

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

