import main_game
from pico2d import *


class Map:
    def __init__(self, name, x, y):
        self.x, self.y = x, y
        self.defaultY = self.y
        self.image = load_image(name)

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_move(self, frame_time):
        distance = main_game.MAX_SPEED_PPS * frame_time

        self.y -= distance

        if main_game.girl.x % 150 == 75:
            self.defaultY -= 150
            self.y = self.defaultY