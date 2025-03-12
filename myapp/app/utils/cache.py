import functools
import time

def cached(expire: int = 300):
    def decorator(func):
        cache = {}
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in cache:
                result, timestamp = cache[key]
                if time.time() - timestamp < expire:
                    return result
            result = func(*args, **kwargs)
            cache[key] = (result, time.time())
            return result
        return wrapper
    return decorator
