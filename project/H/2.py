import time

def d(func):
    def wrapper():
        print('wrapper')
    wrapper.f2 = print('f2')
    wrapper.of = func
    return wrapper

def f():
    print('fff')


# Вызов оригинальной функции без декоратора
d(f).f2()
