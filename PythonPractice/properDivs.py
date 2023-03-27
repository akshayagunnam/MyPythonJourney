# Python Class 3337
# Lesson 5 Problem 7 part (b)
# Author: Calculus_sus (950197)
def is_multiple(x, y):
    '''is_multiple(x, y) -> bool
    returns True if x is a multiple of y, False otherwise
    x, y: int
    '''
    # check if y divides evenly into x
    remainder = x % y
    if remainder == 0:
        return True
    else:
        return False

def sum_of_proper_divs():
    multiples_list = []
    for n in range (100, 999):
        for x in range (int(n/2) + 1):
            if x != 0:
                if is_multiple(n, x) == True:
                    multiples_list.append(x)
                else:
                    x += 1
    total = 0
    for p in range (0, len(multiples_list)):
        total = total + multiples_list[p]
    if n == total:
        print (total)
        
sum_of_proper_divs()
    
