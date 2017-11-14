#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/19 19:06
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary :　对象和面向对象编程。

# 直走五百米
# 右转一百米
# 打印“so sexy”

# 左西右东、上北下南，左下角为原点

# START I
# 定义智能小车
car = [0, 0, "porsche"] # x, y === x - east-west; y - south-north

def straightsouth(): # 朝南向下
    car[1] -= 1

def turnright(): # 右拐向西
    car[0] -= 1

def speak():
    print "so sexy", car

def main():
    while car[1] > -500:
        straightsouth()
    while car[0] > -100:
        turnright()
    speak()

main()
# END I

# START II
# 定义智能小车类
class Car(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def whereami(self):
        return self.__x, self.__y
    def east(self):
        self.__x -= 1
    def west(self):
        self.__x += 1
    def south(self):
        self.__y -= 1
    def north(self):
        self.__y += 1
    def error(self):
        print "error"
    def speak(self, msg):
        print msg
    def move(self, path): # path: (("direction", distance),)
        for direction, distance in path:
            if direction == "east":
                method = self.east
            elif direction == "west":
                method = self.west
            elif direction == "south":
                method = self.south
            elif direction == "north":
                method = self.north
            else:
                method = self.error
            # method = self.east if direction == "east" else self.west if direction == "west" else self.south if direction == "south" else self.north if direction == "north" else self.error
            # method = getattr(self, direction, self.error)
            while distance:
                method()
                distance -= 1
# 实例化智能小车
_car = Car(0, 0)
_car.move((("south", 500), ("west", 100)))
_car.speak("so sexy")
print _car.whereami()
# END II

# START 多态
class Auto(object):
    def __init__(self):
        self.sound = "voom"
    def speedup(self):
        print self.sound
    def ParallelParking(self): # 多态的应用形式：接口和实现
        try:
            print self.start
            self.backoff()
            self.turninto()
            self.turnoutof()
            self.adjust()
            print self.stop
        except Exception:
            print "undefined"
            # raise Exception("backoff/turninto/turnoutof/adjust must be implemented")

class BMW(Auto):
    def __init__(self):
        super(BMW, self).__init__()

class Benz(Auto):
    def __init__(self):
        super(Benz, self).__init__()

class Mazada(Auto):
    def __init__(self):
        self.sound = "booboo"

class Kia(Auto):
    def __init__(self):
        Auto.__init__(self)
        self.sound = "boo"
        self.start = ".".join(("="*5, self.__class__.__name__, "start"))
        self.stop = ".".join(("="*5, self.__class__.__name__, "stop"))
    def backoff(self):
        print "离车位方向车辆三十公分"
    def turninto(self):
        print "向车位打方向盘到极限"
    def turnoutof(self):
        print "反打方向盘到极限"
    def adjust(self):
        print "车身调正"

auto = Auto()
auto.speedup() # 调用自己的方法
auto.ParallelParking() # 调用自己的接口（ParallelParking）、访问自己的方法（backoff/turninto/turnoutof/adjust，均未定义）和变量（start/stop，均未定义）

bmw = BMW()
bmw.speedup() # 调用继承父类的方法（speedup）、访问父类的变量（sound）
benz = Benz()
benz.speedup() # 调用继承父类的方法（speedup）、访问父类的变量（sound）
mazada = Mazada()
mazada.speedup() # 调用继承父类的方法（speedup）、访问自己的变量（sound）
mazada.ParallelParking() # 调用继承父类的接口（ParallelParking）、访问父类的方法（backoff/turninto/turnoutof/adjust，均未定义）和变量（start/stop，均未定义）
kia = Kia()
kia.speedup() # 调用继承父类的方法（speedup）、访问自己的变量（sound）
kia.ParallelParking() # 调用继承父类的接口（ParallelParking）、访问自己的方法（backoff/turninto/turnoutof/adjust）和变量（start/stop）
# END 多态
