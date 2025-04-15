import functools



#def singleton(cls):
# instance = None
#     print('1111')
#     @functools.wraps(cls)
#     def inner(*args, **kwargs):
#         nonlocal instance
#         if instance is None:
#             instance = cls(*args, **kwargs)
#         return instance
#
#     return inner

class singleton(type):
    _instances = {}
    print('1')
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print('2')
            cls._instances[cls] = super(singleton, cls).__call__(*args, **kwargs)
        print('3')
        return cls._instances[cls]


# @singleton
class Connection(metaclass=singleton):
    val = 100500

class Connection1:
    pass

if __name__ == '__main__':

    pass
    c = Connection()
    c1 = Connection()
    # # print(c is c1)
    # # print(type(c))
    # c2 = type(c)()
    #
    # print(c, c1, c2)
    #
    # print(c == c1)
    # print(c != c2)
    # print(c1 != c2)
    #
    # # print(type(Connection), type(Connection1))
