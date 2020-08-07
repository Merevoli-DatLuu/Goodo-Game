import pygame
import random
from good_side.good import Good

class GoodSide:

    def __init__(self):
        self.good_arr = []
        self._flag_born = True

    def good_die(self):
        """
        remove những good ở trạng thái die
        :return None
        """
        for good in self.good_arr:
            if good.is_die == True and good.die_step > 7:
                self.good_arr.remove(good)

    def good_born(self):
        """
        Sinh ra thêm Good
        :return None
        """
        click = pygame.mouse.get_pressed()
        if click[2] == 1 and self._flag_born == True:
            x_pos = random.randint(0, 960 - 32)
            y_pos = random.randint(0, 640 - 32)
            self.good_arr.append(Good(x_pos, y_pos))
            self._flag_born = False
        elif click[2] == 0:
            self._flag_born = True

    def born(self):
        """
        Sinh ra thêm 1 khi 2 good gần nhau
        """
        range = 100

        random.seed()

        for good_1 in self.good_arr:
            for good_2 in self.good_arr:
                if good_1 != good_2 and len(self.good_arr) <= 10000:
                    if (good_1.pos[0] - good_2.pos[0])**2 + (good_1.pos[1] - good_2.pos[1])**2 <= range**2:
                        percent = random.random()
                        if percent < 1/len(self.good_arr)**1.74:
                            x_pos = good_1.pos[0] + good_2.pos[0]
                            y_pos = good_1.pos[1] + good_2.pos[1] 
                            self.good_arr.append(Good(x_pos//2, y_pos//2))

    def update(self, screen):
        """
        Cập nhập trạng thái
        :param screen : pygame.display
        :return None
        """
        self.good_die()
        self.good_born()

        print(len(self.good_arr))
        random.seed()
        percent = random.random()
        if percent < 0.1:
            self.born()
            print(percent)
            
        for good in self.good_arr:
            screen.blit(good.get_move_img(), good.get_middle_pos()) 
            good.update()