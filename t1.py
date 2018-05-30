from math import hypot

class Vector(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        print('In init')

    def __repr__(self):
        print("In repr")
        return 'Vector(%r,%r)' % (self.x, self.y)

    def __abs__(self):
        print("In abs")
        return hypot(self.x, self.y)

    def __bool__(self):
        print("In bool")
        return bool(abs(self))

    def __add__(self, other):
        print("In add")
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self, scalar):
        print("In mul")
        return Vector(self.x * scalar, self.y * scalar)


a = Vector(1,2)
b = Vector(3,4)
print(a * 2)