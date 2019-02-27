# 导入函数
# 必选参数 默认参数 可变参数 命名关键字参数 关键字参数
from function import my_abs
from function import my_move
from function import my_var
from function import my_arg
from function import my_arg2_1
from function import my_arg2_2
from function import my_all_arg
from function import my_fact
from function import my_fact_tail

a = abs(-5)
a
b = abs
aa = b(-5)
aa
aaa = hex(1234222)
aaa
aaaa = str(123214)
aaaa
help(hex)

# 使用自己写的函数
print(my_abs(-5))
# my_abs('a')

# 默认参数
nxy = my_move(100, 100, 100, 100)
nxy = my_move(100, 100, angle=100)  # 对指定参数赋值
print(nxy)  # 返回多个值时，返回一个tuple

# 可变参数
print(my_var(*[1, 2, 3, 4]))  # 加*调用可变参数

# 关键字参数
my_arg('sunchen', 32)
my_arg('sunchen', 23, city='beijing')
extra = {'city': 'beijig', 'job': 'xixix'}
my_arg('sunchen', 23, **extra)

# 命名关键字参数
my_arg2_1('sunchen', 23, city='jiax', job='office')
# 有可变参数  可变参数可以是list 或者tuple
my_arg2_2('sunchen', 23, *(), city='jiaxing')
my_arg2_2('sunchen', 23, *(1, 2, 3, 4), city='jiaxing')

# 所有参数集合
my_all_arg('sunchen', 23, *(), city='jiaxing', job='office')
extra2 = {'job': 'office'}
extra_list = [2, 3, 4]
my_all_arg('sunchen', 23, 1996, *extra_list, city='jiaxing', **extra2)

# 可以通过tuple(list) + dicr 实现所有参数调用
# 将位置参数和关键字参数分离, 有默认值可以不穿参数，
agrs = ('sunchen', 23, 1997, *())
kw2 = {'job': 'office'}
my_all_arg(*agrs, **kw2)

print(my_fact(100))
print(my_fact_tail(100, 1))
