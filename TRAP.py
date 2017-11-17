import main_game
from pico2d import *
import random
import game_framework

#Trap 위치값
TRAP_positionX = 0
TRAP_positionY = 0

image = None

class TRAP:

    def __init__(self):
        global TRAP_positionX, TRAP_positionY, image
        self.x, self.y = 75, 7275
        TRAP_positionX += (random.randint(1, 3) * 150)
        TRAP_positionY += (random.randint(1, 5) * 150)
        self.x += TRAP_positionX
        self.y += TRAP_positionY
        self.defaultY = self.y
        self.frame = 0

        if image == None:
            image = load_image('image\TRAP\TRAP_130x130.png')

    def handle_move(self, frame_time):
        distance = main_game.MAX_SPEED_PPS * frame_time

        self.y += (distance * -1)

        if self.y < (self.defaultY - 150):
            self.defaultY -= 150
            self.y = self.defaultY

    def draw(self):
        #x와 y 위치를 랜덤으로 넣기
        while self.x > 370:
            self.x -= 450

        image.draw(self.x, self.y)

    def update(self):
        for Trp in main_game.Trap:
            for Mon in main_game.Monster2:
                if main_game.collide(Trp, Mon):
                    main_game.Trap.remove(Trp)
            if main_game.collide(main_game.Character, Trp):
                game_framework.quit()

    def collision(self):
        return self.x - 35, self.y -35, self.x + 35, self.y + 35

    def collision_box(self):
        draw_rectangle(*self.collision())