import time
import functools


def metric(fn):
    @functools.wraps(fn)
    def wrapper_func(*args, **kw):
        start = time.time()
        result = fn(*args, **kw)
        end = time.time()
        print('%s executed in %.2f s' % (fn.__name__, end - start))
        return result

    return wrapper_func


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功！')
