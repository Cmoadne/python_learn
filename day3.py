def fab_2(max_now):
    a = 0
    b = 1
    n = 0
    while n < max_now:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


L_g = fab_2(3)  # 生成
for i in L_g:
    print(i)
