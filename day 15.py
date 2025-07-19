# Create a decorator to log function execution time ?

import time
import functools

# Decorator to log execution time
def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' executed in {end - start:.4f} seconds")
        return result
    return wrapper

# Sample function using the decorator
@log_execution_time
def example_function():
    time.sleep(1.5)  # Simulating a slow process

example_function()


