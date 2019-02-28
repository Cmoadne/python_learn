import types  # 判断类型的module


# oop class
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s score is %s' % (self.name, self.score))


class Student_private(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s score is %s' % (self.__name, self.__score))

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score


stu1 = Student_private('sun', 99)
print(stu1.get_score())


class Animal(object):
    def run(self):
        print('animal is running')


class Dog(Animal):  # 继承
    def run(self):  # 多态
        print('dog is running')


def who_run(Animal):  # 只要class里面有run就可以，不关注是不是animalclass
    Animal.run()


who_run(Dog())
dog1 = Dog()
who_run(dog1)

# type
type(123)
print(type(dog1))

print(type(who_run) == types.FunctionType)  # types 判断是否是某个类型

# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
isinstance('a', str)
print('dog1 is Dog?', isinstance(dog1, Dog))

# dir()  获取对象的方法
print(dir(dog1))

# getattr()、setattr()以及hasattr()
print(hasattr(dog1, 'run'))  # 是否有run这个方法
fn = getattr(dog1, 'run')  # 获取方法并赋给新变量
fn()
if not hasattr(dog1, 'x'):  # 定义新属性
    setattr(dog1, 'x', 19)
print(dog1.x)


# 实例属性和类属性
class obj_test(object):
    name = 'obi_test'  # 类属性


# 对象属性会覆盖类属性
obj = obj_test()
print(obj.name)  # obi_test   对象没有name属性，回去找class的name属性
print(obj_test.name)  # obi_test
obj.name = 'obj'
print(obj.name)  # obj
print(obj_test.name)  # obi_test
