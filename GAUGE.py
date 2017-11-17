import main_game
import game_framework
from pico2d import *


class gauge:
    def __init__(self):
        self.x, self.y = 35, 150
        self.frame = 0

        #count는 HP속도 조절
        self.count = 0
        self.HP_gauge = load_image('image\GAUGE\HP_gauge.png')

    def draw(self):
        self.HP_gauge.clip_draw(self.frame * 30, 0, 30, 230, self.x, self.y)

    def update(self):

        if self.frame < 0:
            self.frame = 0

        #HP속도조절
        if main_game.Level < 48:
            if self.count % 32 == 0:
                if self.frame < 99:
                    self.frame = (self.frame + 1)
                else:
                    game_framework.push_state(game_over)
            self.count = self.count + 1
        elif main_game.Level < 150:
            if self.count % 32 == 0:
                if self.frame < 99:
                    self.frame = (self.frame + 1)
                else:
                    game_framework.quit()
            self.count = self.count + 1
