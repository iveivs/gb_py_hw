import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        res = func(*args, **kwargs)
        finish = time.time_ns()
        print(finish - start)
        return res
    return wrapper


def cacher(func):
    cach = {}
    def wrapper(*args):
        key = args
        if key not in cach:
            cach[key] = func(*args)
        print(cach)
        return cach[key]
    return wrapper


@timer
@cacher
def syn(n):
    temp_list = []
    for i in range(0 , n + 1):
        x = (1 + i) ** i
        temp_list.append(x)
    return temp_list
    

syn(3)
syn(4)
syn(7)
syn(3)