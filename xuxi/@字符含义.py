def wrap(f):
    def decorator(*args, **kw):
        print('Call %s()' % f.__name__)
        return f(*args, **kw)
    return decorator

@wrap
def func(a, b):
    return a * 10 + b

if __name__ == '__main__':
    print(func(1, 2))
import time
