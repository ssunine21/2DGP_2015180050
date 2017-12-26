import main_game
import game_framework
import victory_state
import game_over
import title_state
from pico2d import *


class Gauge:
    def __init__(self):
        self.x, self.y = 35, 140
        self.frame = 0

        #count는 HP속도 조절
        self.count = 0
        self.HP_gauge = load_image('image\GAUGE\HP_gauge.png')

    def draw(self):
        self.HP_gauge.clip_draw(self.frame * 30, 0, 30, 230, self.x, self.y)

    def update(self):
        #재시작했을 때 HP가 줄어들지 않는 이유 때문에 100보다 클 경우도 1로 한다.
        if self.frame < 0 or self.frame > 100:
            self.frame = 0

        #HP속도조절
        if main_game.Level < 48:
            if self.count % 20 == 0:

                if self.frame < 100:
                    self.frame = (self.frame + 1)
                else:
                    title_state.gameoverMusic()
                    game_framework.push_state(game_over)
                    pass

            self.count = self.count + 1

        elif main_game.Level < 96:
            if self.count % 12 == 0:

                if self.frame < 100:
                    self.frame = (self.frame + 1)
                else:
                    title_state.gameoverMusic()
                    game_framework.push_state(game_over)
                    pass

            self.count = self.count + 1

        elif main_game.Level < 144:
            if self.count % 10 == 0:

                if self.frame < 100:
                    self.frame = (self.frame + 1)
                else:
                    title_state.gameoverMusic()
                    game_framework.push_state(game_over)
                    pass

            self.count = self.count + 1

        elif main_game.Level < 190:
            if self.count % 8 == 0:

                if self.frame < 100:
                    self.frame = (self.frame + 1)
                else:
                    title_state.gameoverMusic()
                    game_framework.push_state(game_over)
                    pass

            self.count = self.count + 1

        elif main_game.Level == 194:
            game_framework.push_state(victory_state)