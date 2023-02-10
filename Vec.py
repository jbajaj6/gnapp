import math


class Vec:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        xx = other.x + self.x
        yy = other.y + self.y
        zz = other.z + self.z
        return Vec(xx, yy, zz)

    def __iadd__(self, other):
        # all i... functions are meant to implement += or -= etc. operators
        return self.__add__(other)

    def __sub__(self, other):
        xx = self.x - other.x
        yy = self.y - other.y
        zz = self.z - other.z
        return Vec(xx, yy, zz)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        xx = self.x * other
        yy = self.y * other
        zz = self.z * other
        return Vec(xx, yy, zz)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        xx = self.x / other
        yy = self.y / other
        zz = self.z / other
        return Vec(xx, yy, zz)

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]"

    def magnitude(self):
        import math
        return math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))

    def normalize(self):
        if self.magnitude == Vec(0, 0, 0):
            return Vec(0, 0, 0)
        return self * (1/self.magnitude())

    def normalizeinplace(self):
        y = self * (1/self.magnitude())
        self.x = y.x
        self.y = y.y
        self.z = y.z

    def dot(self, v):
        xx = self.x * v.x
        yy = self.y * v.y
        zz = self.z * v.z
        return xx + yy + zz

    def cross(self, v):
        cx = (self.y * v.z) - (self.z * v.y)
        cy = (self.z * v.x) - (self.x * v.z)
        cz = (self.x * v.y) - (self.y * v.x)
        return Vec(cx, cy, cz)

    def crossinplace(self, v):
        cx = (self.y * v.z) - (self.z * v.y)
        cy = (self.z * v.x) - (self.x * v.z)
        cz = (self.x * v.y) - (self.y * v.x)
        self.x = cx
        self.y = cy
        self.z = cz

    # 2 dimensional
    def rotate(self, theta):
        theta = math.radians(theta)
        xx = self.x * math.cos(theta) + self.y * math.sin(theta)
        yy = self.y * math.cos(theta) - self.x * math.sin(theta)
        self.x = xx
        self.y = yy
