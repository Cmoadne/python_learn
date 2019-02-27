from functools import reduce
import functools


# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
def hign_fun(a, b, fun_c):
    return fun_c(a) + fun_c(b)


f = abs
print(hign_fun(-2, 3, f))

# map  对list 每个元素使用函数f， 需要两个入参 函数和literator ,返回一个literator
f_t = abs
ret = map(f_t, [1, -2, 3, -5, 0])
# ret  # 只打印地址  for会把ret清空！！！
# for i in ret:
#     print(i)

list_ret = list(ret)
print(list_ret)


# reduce  把函数对多个参数积累作用，f必须接受两个参数
def my_add(x, y):
    return x + y


ret_2 = reduce(my_add, [1, 2, 3, 4, 5, 6, 7])
print(ret_2)

# 运用 把str转为int
DIGITS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


# 1行
def str2int(s):
    return reduce(lambda x, y: 10 * x + y, map(lambda x: DIGITS[x], s))


# filter
def is_odd(x):
    return x % 2 == 1


fl_1 = filter(is_odd, [1, 23, 4, 5, 6, 7, 1, 3, 2])  # true 被保留
fl_1 = list(fl_1)
print(fl_1)


# 素数筛选
# 生成全奇数数列
def odd_from3():
    n = 3
    while True:
        yield n
        n = n + 2


def division(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = odd_from3()
    while True:
        n = next(it)
        yield n
        it = filter(division(n), it)


L = []
for x in primes():

    if x < 100:
        L.append(x)
        # print(x)
    else:
        # print('num = %d' % num)
        break

print(L)

# sort
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_byname(x):
    return x[0].lower()


def by_byscore(x):
    return x[1]


# key 返回要比大小的值
L2 = sorted(L, key=by_byname)
print(L2)

L3 = sorted(L, key=by_byscore, reverse=True)
print(L3)


# 返回函数  闭包
def fun_test(*args):
    def f_3():
        sum = 0
        for x in args:
            sum = sum + x
        return sum

    return f_3


f_1 = fun_test(*(1, 2, 3, 4, 5))
f_2 = fun_test(*(1, 2, 3, 4, 5))
f_1 == f_2  # false


def count():
    fs = []
    for i in range(1, 4):

        def f():
            return i * i

        fs.append(f)
    return fs


# 都是9，原因是返回值内不能使用循环变量，或者后续会发生变化的变量
fs_l = count()
fs_l[0]()
fs_l[1]()
fs_l[2]()

# 匿名函数
# lambda
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# 装饰器
def debug1(func):
    def wrapper(*args, **kw):
        print('entry: %s' % func.__name__)
        return func(*args, **kw)

    return wrapper


@debug1
def test1():
    print('hello')


test1()


# 带参数装饰器
def debug2(text):
    def decotator(func):
        @functools.wraps(func)  # 指定name是func
        def wrapper(*args, **kw):
            print('%s entry %s' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decotator


@debug2('debug2')  # = debug('hhhh')(test2)
def test2(x):
    print('test2 %d' % x)


test2(333)

# 偏函数创建一个简化的函数，改变默认参数
int2 = functools.partial(int, base=2)
int2('1111')  # 把base 从10 改到了2
int2('1111', base=10)  # 不影响原来的使用方法


def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
