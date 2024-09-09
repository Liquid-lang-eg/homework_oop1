# Задание 1

class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def find_out_taste(self):
        if self.taste == None:
            return "У вас обычная газировка"
        else:
            return f'Ваша газировка обладает {self.taste} вкусом!'

soda1 = Soda('клубничная')
soda2 = Soda()
print(soda1.find_out_taste())
print(soda2.find_out_taste())

# Задание 2

class Math:

    def division(self, a: isinstance(int, float), b: isinstance(int, float)):
        return a / b

    def multiplication(self, a: isinstance(int, float), b: isinstance(int, float)):
        return a * b

    def addition(self, a: isinstance(int, float), b: isinstance(int, float)):
        return a + b

    def subtraction(self, a: isinstance(int, float), b: isinstance(int, float)):
        return a - b

math = Math()
print(math.multiplication(3, 4))
print(math.division(8, 4))
print(math.subtraction(4, 4))
print(math.addition(1, -1))


# Задание 3


class Car:

    def __init__(self):
        self.color = None
        self.type = None
        self.year = None

    def car_is_on(self):
        print('Автомобиль заведен')

    def car_is_of(self):
        print('Автомобиль заглушен')

    def new_color(self, new_color):
        self.color = new_color

    def new_type(self, new_type):
        self.type = new_type

    def new_year(self, new_year):
        self.year = new_year

car = Car()
car.car_is_on()
car.car_is_of()
car.new_color('желтый')
car.new_type('Chevrolette')
car.new_year('2015')
print(car.color, car.type, car.year)


# Задание 4

import math

class Sphere:

    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

    def get_square(self):
        return 4 * math.pi * (self.radius ** 2)

    def get_radius(self):
        return self.radius

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, new_radius: int):
        self.radius = new_radius

    def set_center(self, x_new, y_new, z_new):
        self.x = x_new
        self.y = y_new
        self.z = z_new

    def is_point_inside(self, point_x, point_y, point_z):
        if self.x - self.radius < point_x < self.x + self.radius:
            if self.y - self.radius < point_y < self.y + self.radius:
                if self.z - self.radius < point_z < self.z + self.radius:
                    return True
        return False

sphere = Sphere(2, 0, 0, 0)
print(sphere.is_point_inside(1, 1, 1))


# Задание 5

class SupperStr(str):
    def __init__(self, value: str):
        super().__init__()
        self.value = value

    def is_repeatance(self, s: str):
        while len(s) <= len(self.value):
            if s == self.value:
                return True
            else:
                s += s
        return False

    def is_palindrom(self):

        if self.value.lower() == self.value[::-1].lower():
            return True
        else:
            return False


super_str = SupperStr('лоло')
print(super_str.is_palindrom())
print(super_str.is_repeatance('ло'))
