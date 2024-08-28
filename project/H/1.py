import time

def time_of_function(func):
    def wrapper():
        t1 = time.time()
        result = func()
        t2 = time.time()
        print(f'Работа заняла {t2 - t1} секунд')
        return result
    def f2():
        print('f2')
    wrapper.original_func = func
    return wrapper

def func_one():
    my_list = 1+2
    print('Функция func_one() отработала')

# @time_of_function
def func_two():
    my_list = 11+22
    print('Функция func_two() отработала')


time_of_function(func_one)()
time_of_function(func_one).f2()
time_of_function(func_one).original_func()