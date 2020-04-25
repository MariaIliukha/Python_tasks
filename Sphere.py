import math

class Sphere(object):

    def __init__(self, r = 1, x = 0.0, y = 0.0, z = 0.0):
        self.r = r
        self.x = x
        self.y = y
        self.z = z


    def get_volume(self):
        return math.pi * self.r ** 3 * 4 / 3
    

    def get_square(self):
        return 4 * math.pi * self.r ** 2

    def  get_radius(self):
        return self.r

    def get_center(self):
        center = (self.x, self.y, self.z)
        return center

    def set_radius(self, rad):
        self.r = rad

    def set_center(self, xx, yy, zz):
        self.x = xx
        self.y = yy
        self.z = zz

    def is_point_inside(self, xx, yy, zz):
        left_side = (self.x - xx) ** 2 + (self.y - yy) ** 2 + (self.z - zz) ** 2
        if left_side <= self.r ** 2:
            return True
        return False

s0 = Sphere(1.99, 1, 2, -1)

print s0.get_radius()
print s0.is_point_inside(0, 0, 0.99)


