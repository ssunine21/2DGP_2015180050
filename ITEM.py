from pico2d import *
import main_game
import random

#protected 위치값
protected_positionX = 0
protected_positionY = 0

#보호막 상태
protect_State = 0


class Protected:
    item_image = None
    effect_image = None

    def __init__(self):
        global protected_positionX, protected_positionY
        self.x, self.y = 75, 225
        protected_positionX += (random.randint(1, 3) * 150)
        protected_positionY += (random.randint(1, 40) * 150)

        self.x += protected_positionX
        self.y += protected_positionY

        self.defaultY = self.y

        if Protected.item_image == None:
            Protected.item_image = load_image('image\ITEM\protectedITEM.png')

        if Protected.effect_image == None:
            Protected.effect_image = load_image('image\ITEM\protected.png')

    def handle_move(self, frame_time):
        distance = main_game.MAX_SPEED_PPS * frame_time

        self.y -= distance

        if main_game.girl.x % 150 == 75:
            self.defaultY -= 150
            self.y = self.defaultY

    def draw(self):
        # x와 y 위치를 랜덤으로 넣기
        while self.x > 370:
            self.x -= 450
        self.item_image.draw(self.x, self.y)

        if protect_State >= 1:
            self.effect_image.draw(main_game.girl.x, main_game.girl.y + 15)

    def update(self):
        global protect_State
        for PROTECT in main_game.protected:
            if main_game.collide(main_game.girl, PROTECT):
                if protect_State == 0:
                    main_game.protected.remove(PROTECT)
                    protect_State = 1
                else:
                    pass

    def collision(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def collision_box(self):
        draw_rectangle(*self.collision())