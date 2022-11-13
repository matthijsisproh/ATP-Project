from functools import wraps
import time


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Timer: function {func.__name__} completed in {round(end_time - start_time, 1)} sec.')
        return result
    return wrapper

def logger(func):
    @wraps(func)   
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Logger: function {func.__name__} ran with args: {args}, and kwargs: {kwargs}.')
        return result
    return wrapper


# def cache(func):
#     """Keep a cache of previous function calls"""
#     @wraps(func)
#     def wrapper_cache(*args, **kwargs):
#         cache_key = args + tuple(kwargs.items())
#         if cache_key not in wrapper_cache.cache:
#             wrapper_cache.cache[cache_key] = func(*args, **kwargs)
#         return wrapper_cache.cache[cache_key]
#     wrapper_cache.cache = dict()
#     return wrapper_cache
