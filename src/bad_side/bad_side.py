import pygame
import random
from bad_side.bad import Bad

class BadSide:

    def __init__(self):
        self.bad_arr = []
        self._flag_born = True

    def bad_die(self):
        """
        remove những bad ở trạng thái die
        :return None
        """
        for bad in self.bad_arr:
            if bad.is_die == True and bad.die_step > 7:
                self.bad_arr.remove(bad)

    def bad_born(self):
        """
        Sinh ra thêm bad
        :return None
        """
        click = pygame.mouse.get_pressed()
        if click[2] == 1 and self._flag_born == True:
            x_pos = random.randint(0, 960 - 32)
            y_pos = random.randint(0, 640 - 32)
            self.bad_arr.append(Bad(x_pos, y_pos))
            self._flag_born = False
        elif click[2] == 0:
            self._flag_born = True

    def born(self):
        """
        Sinh ra thêm 1 khi 2 bad gần nhau
        """
        range = 100

        random.seed()

        for bad_1 in self.bad_arr:
            for bad_2 in self.bad_arr:
                if bad_1 != bad_2 and len(self.bad_arr) <= 10000:
                    if (bad_1.pos[0] - bad_2.pos[0])**2 + (bad_1.pos[1] - bad_2.pos[1])**2 <= range**2:
                        percent = random.random()
                        if percent < 1/len(self.bad_arr)**1.74:
                            x_pos = bad_1.pos[0] + bad_2.pos[0]
                            y_pos = bad_1.pos[1] + bad_2.pos[1] 
                            self.bad_arr.append(Bad(x_pos//2, y_pos//2))

    def update(self, screen, good_arr):
        """
        Cập nhập trạng thái
        :param screen : pygame.display
        :return None
        """
        self.bad_die()
        #self.bad_born()
        for bad in self.bad_arr:
            screen.blit(bad.get_move_img(), bad.get_middle_pos()) 
            bad.update(good_arr)