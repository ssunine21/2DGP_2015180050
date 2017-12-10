import main_game
from pico2d import *


class Map:
    def __init__(self, mapcourse, bgmcourse, x, y):
        self.x, self.y = x, y
        self.defaultY = self.y
        self.image = load_image(mapcourse)
        self.stageBGM = load_music(bgmcourse)

        self.stageBGM.set_volume(50)
        self.stageBGM.repeat_play()

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if main_game.Level == 43:
            self.changeMusic(main_game.stage1_map, main_game.stage2_map)
            main_game.Level += 1

        if main_game.Level == 92:
            self.changeMusic(main_game.stage2_map, main_game.stage3_map)
            main_game.Level += 1

    def changeMusic(self, Amusic, Bmusic):
        Amusic.stageBGM.stop()
        Bmusic.stageBGM.repeat_play()

    def handle_move(self, frame_time):
        distance = main_game.MAX_SPEED_PPS * frame_time

        self.y -= distance

        if main_game.girl.x % 150 == 75:
            self.defaultY -= 150
            self.y = self.defaultY
