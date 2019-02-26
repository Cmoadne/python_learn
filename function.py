import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x < 0:
        return -x
    else:
        return x


def my_move(x, y, step=0, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# 默认参数必须指向不可变的 字符串或者数字等
def my_pow(x, y=2):
    s = 1
    while y > 0:
        y = y - 1
        s = s * x
    return s


def my_addend(L=None):  # 不能 L = []
    if L is None:
        L = []
    L.append('END')
    return L


# 可变参数函数 平方和   调用 my_var(*list)
def my_var(*numbers):
    s = 0
    for index in numbers:
        s = s + index * index
    return s
