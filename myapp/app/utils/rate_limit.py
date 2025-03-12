import time
from functools import wraps

def rate_limit(max_calls: int, time_window: int):
    def decorator(func):
        calls = []
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            now = time.time()
            calls = [call for call in calls if now - call < time_window]
            if len(calls) >= max_calls:
                raise Exception('Rate limit exceeded')
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator
