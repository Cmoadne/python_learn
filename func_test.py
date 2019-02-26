# 导入函数
# 必选参数 默认参数 可变参数 关键字参数 命名关键字参数
from function import my_abs
from function import my_move
from function import my_var

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

nxy = my_move(100, 100, 100, 100)
nxy = my_move(100, 100, angle=100)  # 对指定参数赋值
print(nxy)  # 返回多个值时，返回一个tuple

print(my_var(*[1, 2, 3, 4]))  # 加*调用可变参数
