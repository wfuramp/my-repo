import time
from functools import wraps

def retry(attempts=3, interval_seconds=60, logger=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            _attempts = attempts
            while _attempts > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    _attempts -= 1
                    if logger:
                        logger.error(f"Exception in {func.__name__}: {e}. {_attempts} retries left.")
                    if _attempts == 0:
                        raise e
                    time.sleep(interval_seconds)
        return wrapper
    return decorator
