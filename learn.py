import random
for function in dir(random):
    print(f"Function: {function} | Type: {type(getattr(random, function))} | Docstring: {getattr(random, function).__doc__}")