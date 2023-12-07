import random

class RandomError(Exception):
    pass

try:
    num = random.random()
    if num < 0.1:
        raise RandomError
except RandomError as e:
    print("Random Error generated")
else:
    print(num)
