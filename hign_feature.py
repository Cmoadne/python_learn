# 切片   不包括最后一个   list tuple  strs
from collections import Iterable
from collections import Iterator
import os

list_test = list(range(100))  # 0-99
list_1 = list_test[0:10]  # 0-9
list_1
list_2 = list_test[-10:]  # 90-99
list_2
print(list_test[10::5])
print(list_test[:])

print((1, 2, 3, 4, 5)[-3:-1])
print('ABCDEF' [-1:])

# 迭代 iteration   list tuple dict strs 等任意可迭代对象
isinstance('abs', Iterable)
isinstance(123, Iterable)
dict_t = {'a': 1, 'b': 2, 'c': 3}
for key in dict_t:
    print(key, dict_t[key])

dict_t2 = {'a': 1, 'b': 2, 'c': 3}
for key, v in dict_t2.items():
    print(key, v)

for ch in 'ABC':
    print(ch)

for x, y in [(1, 2), (2, 3)]:
    print(x, y)

for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)

# 列表生成器
[x * x for x in range(11)]
[x * x for x in range(11) if x % 2 == 0]
[m + n for m in 'abc' for n in 'xyz']

[dir_1 for dir_1 in os.listdir('.')]  # 列出目录
dict_t3 = {'a': 1, 'b': 2, 'c': 3}
[k + '=' + str(v) for k, v in dict_t3.items()]  # =号！ 因为字符串相加
[k2.upper() for k2 in dict_t3]

# 生成器，推算后面的元素，不生成list，节约内存
# 1、直接列表generator   2、函数generator
gene_t = (x * x for x in range(11))
for value_g in gene_t:
    print(value_g)


def fab_(max_now):
    a = 0
    b = 1
    n = 0
    while n < max_now:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fab_(5)


def fab_2(max_now):
    a = 0
    b = 1
    n = 0
    while n < max_now:
        yield b  # 生成
        a, b = b, a + b
        n = n + 1
    return 'done'


L_g = fab_2(3)  # 生成
for i in L_g:
    print(i)

# 迭代器
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现的
isinstance('abc', Iterator)
isinstance(iter('abc'), Iterator)   # 可迭代对象转换转换为迭代器
