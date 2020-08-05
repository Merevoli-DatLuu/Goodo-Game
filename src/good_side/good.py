import pygame
import random

class Good:

    def __init__(self, x = 100, y = 100):
        # image sources
        self.move_img_src = '..\img\Good\Move\good_move_'
        self.born_img_src = '..\img\Good\Born\good_born_'
        self.die_img_src = '..\img\Good\Die\good_die_'

        # move image array
        self.move_img_arr = list(map(lambda id : self.move_img_src + str(id) + '.png', range(0, 30)))
        self.move_arr = list(map(pygame.image.load, self.move_img_arr))
        
        # born image array
        self.born_img_arr = list(map(lambda id : self.born_img_src + str(id) + '.png', range(0, 13)))
        self.born_arr = list(map(pygame.image.load, self.born_img_arr))

        # die image array
        self.die_img_arr = list(map(lambda id : self.die_img_src + str(id) + '.png', range(0, 8)))
        self.die_arr = list(map(pygame.image.load, self.die_img_arr))
        
        self.action_arr = self.born_arr
        self.pos = [x, y]
        self.move_step = 0
        self.born_step = 0
        self.die_step = 0
        self.is_born = True
        self.is_die = False

        self._x_scale = 0
        self._y_scale = 0

    def move(self):
        """
        Thay đổi pos và move_step khi di chuyển
        :return None
        """
        """mouse_pos = pygame.mouse.get_pos()

        if mouse_pos[0] - self.pos[0] > 0 and mouse_pos[0] - self.pos[0] <= 60:
            self.pos[0] += 1
        else:
            self.pos[0] += (mouse_pos[0] - self.pos[0])//60

        if mouse_pos[1] - self.pos[1] > 0 and mouse_pos[1] - self.pos[1] <= 60:
            self.pos[1] += 1
        else:
            self.pos[1] += (mouse_pos[1] - self.pos[1])//60
        """
        if self.move_step == 0:
            self._x_scale = random.random()*2 - 1
            self._y_scale = random.random()*2 - 1
        length_unit = 1
        if self.pos[0] + self._x_scale*length_unit >= 0 and self.pos[0] + self._x_scale*length_unit <=700 - 32:
            self.pos[0] = self.pos[0] + self._x_scale*length_unit
        if self.pos[1] + self._y_scale*length_unit >= 0 and self.pos[1] + self._y_scale*length_unit <= 500 - 32:
            self.pos[1] = self.pos[1] + self._y_scale*length_unit

        self.move_step = (self.move_step + 1)%30

    def born(self):
        """
        Thay đổi born_step khi được khởi tạo
        :return None
        """
        self.born_step += 1

        if self.born_step >= 13:
            self.is_born = False
            self.action_arr = self.move_arr

    def die(self):
        """
        Good die khi bị click vào
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

    def update(self):
        """
        Cập nhật trạng thái của good sau mỗi bước đi
        :return None
        """
        if self.is_born:
            self.born()
        else:
            self.move()
            self.die()

    def get_middle_pos(self):
        """
        Lấy tọa độ giữa đối tượng Good
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
        if self.is_born == True:
            return self.born_arr[self.born_step]
        elif self.is_die == True:
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