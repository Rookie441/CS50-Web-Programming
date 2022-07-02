import math

def is_prime(n):
    # Intentional fail algorithm --> Fix by adding 1 to end of range
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True