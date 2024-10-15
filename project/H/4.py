def my_magic_method(obj):
    return obj.__my_magic_method__()


class MyClass:
    def __my_magic_method__(self):
        print("do some magic")


my_obj = MyClass()
my_magic_method(my_obj)  # do some magic