def is_multiple(x,y):
    '''is_multiple(x,y) -> bool
    returns True if x is a multiple of y, False otherwise
    x, y: int
    '''
    # check if y divides evenly into x
    return (x % y == 0)

def is_prime(n):
    '''is_prime(n) -> bool
    returns True if n is prime, False if n is not prime
    n: int
    '''
    # deal with the 1 case directly
    if (n < 2):
        return False

    # check every divisor from 2 up to sqrt(n)
    for div in range(2, int(n**0.5) + 1):
        if is_multiple(n, div):
            return False  # n isn't prime!

    return True  # if we made it here, n is prime

for num in range(2, 100):
    if is_prime(num):
        print(num, end=' ')
