import pygame
import math
import random

class Bad:

    def __init__(self, x = 100, y = 100):
        # image sources
        self.move_img_src = '..\img\Bad\Move\\bad_move_'
        self.die_img_src = '..\img\Bad\Die\\bad_die_'

        # move image array
        self.move_img_arr = list(map(lambda id : self.move_img_src + str(id) + '.png', range(0, 30)))
        self.move_arr = list(map(pygame.image.load, self.move_img_arr))
        
        # die image array
        self.die_img_arr = list(map(lambda id : self.die_img_src + str(id) + '.png', range(0, 8)))
        self.die_arr = list(map(pygame.image.load, self.die_img_arr))
        
        self.speed = 2 # 20 pixels / second
        self.pos = [x, y]
        self.move_step = 0
        self.die_step = 0
        self.is_born = True
        self.is_die = False

        self._x_scale = 0
        self._y_scale = 0

    def move_to(self, pos):
        """
        Di chuyển đến pos
        :param pos : [int, int]
        :return None
        """        
        sub_x = self.pos[0] - pos[0]
        sub_y = self.pos[1] - pos[1]
        sub_scale = self.speed/math.sqrt(sub_x**2 + sub_y**2)

        self.pos[0] -= sub_x*sub_scale
        self.pos[1] -= sub_y*sub_scale

    def move(self, good_arr):
        """
        Thay đổi pos và move_step khi di chuyển
        :return None
        """
        min_distance = 0x3f3f3f3f
        min_pos = [100, 100]
        for good in good_arr:
            distance = (good.pos[0] - self.pos[0])**2 + (good.pos[1] - self.pos[1])**2
            if distance < min_distance:
                min_distance = distance
                min_pos = good.pos

        self.move_to(min_pos)

        self.move_step = (self.move_step + 1)%30

    def die(self):
        """
        bad die khi bị click vào
        :return None
        """
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        width = self.move_arr[self.move_step].get_width()
        height = self.move_arr[self.move_step].get_height()

        if  mouse[0] >= self.pos[0] - width//2 and mouse[1] >= self.pos[1] - height//2\
        and mouse[0] <= self.pos[0] + width//2 and mouse[1] <= self.pos[1] + height//2\
        and click[0] == 1:
            self.is_die = True
            return True
        else:
            return False

    def kill(self, good_arr):
        for good in good_arr:
            if (good.pos[0]<= self.pos[0] <= good.pos[0] + 32\
             or good.pos[0]<= self.pos[0] + 32 <= good.pos[0] + 32)\
            and (good.pos[1]<= self.pos[1] <= good.pos[1] + 32\
             or good.pos[1]<= self.pos[1] + 32 <= good.pos[1] + 32):
                #good_arr.remove(good)
                good.is_die = True

    def update(self, good_arr):
        """
        Cập nhật trạng thái của bad sau mỗi bước đi
        :return None
        """
        self.move(good_arr)
        self.kill(good_arr)
        self.die()

    def get_middle_pos(self):
        """
        Lấy tọa độ giữa đối tượng bad
        :return [x, y]
        """
        half_width_img = self.move_arr[self.move_step].get_width()//2
        half_height_img = self.move_arr[self.move_step].get_height()//2
        #return [self.pos[0] - half_width_img, self.pos[1] - half_height_img]
        return self.pos

    def get_move_img(self):
        """
        Lấy hình theo id
        :return pygame.image
        """
        if self.is_die == True:
            if self.die_step <= 7:
                res = self.die_arr[self.die_step]
                self.die_step += 1
                return res
            else:
                return self.die_arr[0]
        else:
            return self.move_arr[self.move_step]

    def __del__(self):
        print("Died")