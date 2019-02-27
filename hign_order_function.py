from functools import reduce


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
