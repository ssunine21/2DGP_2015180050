import main_game
from pico2d import *


class MAP1:
    def __init__(self):
        self.x, self.y = 225, 3600
        self.defaultY = self.y
        self.image = load_image('image\MAP\MAP(STAGE1)_450x750.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_move(self, frame_time):
        distance = main_game.MAX_SPEED_PPS * frame_time

        self.y -= distance

        if main_game.Character.x % 150 == 75:
            self.defaultY -= 150
            self.y = self.defaultY




class MAP2:
    def __init__(self):
        self.x, self.y = 225, 10800
        self.defaultY = self.y
        self.image = load_image('image\MAP\MAP(STAGE2)_450x750.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_move(self, frame_time):
        distance = main_game.MAX_SPEED_PPS * frame_time

        self.y -= distance

        if main_game.Character.x % 150 == 75:
            self.defaultY -= 150
            self.y = self.defaultY




class MAP3:
    def __init__(self):
        self.x, self.y = 225, 18000
        self.defaultY = self.y
        self.image = load_image('image\MAP\MAP(STAGE3)_450x750.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_move(self, frame_time):
        distance = main_game.MAX_SPEED_PPS * frame_time

        self.y -= distance

        if main_game.Character.x % 150 == 75:
            self.defaultY -= 150
            self.y = self.defaultY
