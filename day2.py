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
