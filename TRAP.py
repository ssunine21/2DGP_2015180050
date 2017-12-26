from pico2d import *

import main_game
import random
import ITEM
import game_framework
import game_over
import title_state

#Trap 위치값
trap_positionX = 0
trap_positionY = 0

image = None

class Trap:

    def __init__(self):
        global trap_positionX, trap_positionY, image
        self.x, self.y = 75, 7275
        trap_positionX += (random.randint(1, 3) * 150)
        trap_positionY += (random.randint(1, 5) * 150)
        self.x += trap_positionX
        self.y += trap_positionY
        self.defaultY = self.y
        self.frame = 0

        if image == None:
            image = load_image('image\TRAP\TRAP_130x130.png')

    def handle_move(self, frame_time):
        distance = main_game.MAX_SPEED_PPS * frame_time

        self.y -= distance

        if main_game.girl.x % 150 == 75:
            self.defaultY -= 150
            self.y = self.defaultY

    def draw(self):
        #x와 y 위치를 랜덤으로 넣기
        while self.x > 370:
            self.x -= 450

        image.draw(self.x, self.y)

    def update(self):
        for Trp in main_game.stage2_trap:
            for Mon in main_game.stage2_monster:
                if main_game.collide(Trp, Mon):
                    main_game.stage2_trap.remove(Trp)
            if main_game.collide(main_game.girl, Trp):
                if ITEM.protect_State >= 1:
                    ITEM.protect_State = ITEM.protect_State - 1
                    main_game.stage2_trap.remove(Trp)
                else:
                    title_state.gameoverMusic()
                    game_framework.push_state(game_over)
                    pass

    def collision(self):
        return self.x - 15, self.y -15, self.x + 15, self.y + 15

    def collision_box(self):
        draw_rectangle(*self.collision())