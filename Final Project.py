from timeit import default_timer as timer

def timefunc(func):
    def inner (*asgs, **kwargs):
        start = timer ()
        results = func(*args, **kwargs)
        end = time ()
        message = '{} took {} seconds'.format(func.__name__, end -str)
        print(mesage)
        return results
    return inner
