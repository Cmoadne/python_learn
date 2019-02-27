import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x < 0:
        return -x
    else:
        return x


# 必选参数 默认参数
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


# 关键字参数 这些关键字参数在函数内部自动组装为一个dict
def my_arg(name, age, **kw):
    print('name:', name, 'age：', age, 'others:', kw)


# 命名关键字参数  用* 指示后面参数为命名关键字参数， 如果定义了可变参数，*省略
def my_arg2_1(name, age, *, city, job='engineer'):
    print('name:', name, 'age：', age, 'city', city, 'job', job)


def my_arg2_2(name, age, *number, city, job='engineer'):
    print('name:', name, 'age：', age, 'numbers:', number, 'city:', city,
          'job:', job)


# 所有参数，必选 默认 可变 命名关键字 关键字
def my_all_arg(name, age=23, year=1995, *number, city='beijing', **kw):
    print('name:', name, 'age：', age, 'year:', year, 'numbers:', number,
          'city:', city, 'kw:', kw)


# 递归
def my_fact(n):
    if n == 1:
        return 1
    else:
        return n * my_fact(n - 1)


# 尾递归，可以不让栈溢出，但是python解释器没有做优化，所以还是溢出
def my_fact_tail(n, product):
    if n == 1:
        return product
    else:
        return my_fact_tail(n - 1, n * product)
