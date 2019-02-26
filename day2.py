#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 输入输出
name = input('please input your name:')
print('hello', name)  # or just name

# print absolute value of an integer:
a = int(input('please input a:'))  # transform int format
if (a > 0):  # do not forget :
    print(a)
elif a < 0:  # use elif
    print(-a)
else:
    pass  # use pass to skip

# 转义字符
print("I'm OK\n")
print('I\'m OK\n')
print('\\\n\\\n')
print(r'\\\n\\', '\n')
print('''line1
line2
lin3''', '\n')
print(r'''line1
line2
line3''', '\n')

# 除法
print(10 / 3, '\n')  # not int
print(10 // 3)
print(10 % 3)

# unicode 内存中     utf-8文件中
ord('a')  # 得到a对应的数字
ord('中')  # 得到中对应的数字
chr(97)  # 根据数转换成字符
chr(20013)
'ABC'.encode('ASCII')  # 转换成ascii码
b = '中文'.encode('UTF-8')  # 转换成utf-8
print(b)
b'ABC'.decode('ASCII')  # 解码  bytes
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')  # 解码bytes得到字符
b'\xe4\xb8\xad\xe6'.decode('utf-8', errors='ignore')  # 解码忽略错误

len('acv')  # 字符串长度
len('中文')
len(b'abc')  # bytes长度
len(b'\xe4\xb8\xad\xe6\x96\x87')
len('中文'.encode('utf-8'))  # 中文对应的bytes 6

# 格式化输出
print('hello %s you have $%d' % ('sun chen', 1000))  # %之前没有逗号

print('%d %%' % 100)  # %%进行转义
print('%s  %s' % (100, 22))  # %s永远能起作用

# list  可变
list_test = [1, 2, '123', [1, 'sss']]
list_test[2]
list_test[3][1]
list_test[-1]  # == list_test 最后一个元素
list_test
list_test.append(1232)  # 最后追加一个元素
list_test
list_test.pop()  # 弹出最后元素
list_test
list_test.insert(2, 'insert')  # 指定位置插入元素
list_test
list_test.pop(2)  # 弹出指定位置元素
list_test
list_test[0] = 'insert_0'  # 指定位置赋值， 改变了位置数据类型
list_test
list_test2 = []  # 空
len(list_test)
len(list_test2)

# tuple   元素不能更改，但如果元素是list 可以更改list的值
tuple_test = (1, 2, '333', [1, 2, '3333'])
tuple_test2 = (2, )  # 只有一个元素的tuple
tuple_test3 = ()  # 空
tuple_test
tuple_test[3][1] = '2143'
tuple_test

# if
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

# for 循环 不需要对条件自增
list_0_100 = list(range(101))  # 创建一个0-100 的list
sum = 0
for index in list_0_100:  # 冒号和if一样不要忘记
    sum = index + sum
sum

# while 要自增判断条件
sum = 0
n = 0
while n < 101:
    sum = sum + n
    n = n + 1
print(sum)

# break
n = 0
while n < 100:
    if n % 2 == 0:
        print(n)
    if n > 20:
        break
    n = n + 1

# continue
n = 0
while n < 100:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

# dict test   大括号创建     中括号读取 key必须不可变
dict_test = {'sun': 99, 'chen': 85, 'pan': 70}
dict_test['sun']
dict_test['sun'] = 100
dict_test
'sun' in dict_test
'li' in dict_test
dict_test.get('sun', -1)
dict_test.get('li', -1)
dict_test.pop('pan')
dict_test

# set 无序无重复
set_test = set([1, 2, 3])  # set 以list 为参数
set_test.remove(1)
set_test
set_test.add('23')
set_test2 = set((2, 3, 4, '234'))
set_test & set_test2
set_test | set_test2
set_test3 = ([1, 2, 3, [44, 4]])  # 报错，不可入可变的lisit为key


