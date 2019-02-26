#!/usr/bin/env python3
# -*- coding: utf-8 -*-
    
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

print(10 / 3, '\n')  # not int
print(10 // 3)
print(10 % 3)

# unicode 内存中     utf-8文件中
ord('a')  # 得到a对应的数字
ord('中')  # 得到中对应的数字
chr(97)  # 根据数转换成字符
chr(20013)
'ABC'.encode('ASCII')  # 转换成ascii码
'中文'.encode('UTF-8')  # 转换成utf-8
b'ABC'.decode('ASCII')  # 解码  bytes
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')  # 解码bytes得到字符
b'\xe4\xb8\xad\xe6'.decode('utf-8', errors='ignore')  # 解码忽略错误

len('acv')  # 字符串长度
len('中文')
len(b'abc')  # bytes长度
len(b'\xe4\xb8\xad\xe6\x96\x87')
len('中文'.encode('utf-8'))     # 中文对应的bytes 6

