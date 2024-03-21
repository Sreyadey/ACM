import math

def min_tents(a, b, c):
    x = a
    y = math.ceil(b / 3)
    r = a + b + c - x - 3 * y
    z = math.ceil(r / 3)
    
    if r > 0:
        return x + y + z
    else:
        return x + y

