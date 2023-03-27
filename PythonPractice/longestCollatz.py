def next_collatz_term(n):
    '''next_collatz_term(n) -> int
    returns next term in Collatz sequence
    n: int, must be greater than or equal to 2.
    '''
    if n%2 == 0:
        return n//2
    else:
        return 3*n + 1

def collatz_sequence(n):
    '''collatz_sequence(n) -> None
    prints Collatz sequence starting at n
    n: positive int
    '''
    print(n)
    while n != 1:
        n = next_collatz_term(n)
        print(n)

def collatz_length(n):
    '''collatz_length(n) -> int
    returns length of Collatz sequence starting at n
    n: positive int
    '''
    count = 1
    while n != 1:
        n = next_collatz_term(n)
        count += 1
    return count

def find_longest_collatz(limit):
    '''find_longest_collatz(limit) -> int
    returns the integer less than limit with the longest Collatz sequence
    limit: positive int
    '''
    # variables to store the maximums
    maxLength = 1
    maxStartingValue = 1
    for i in range(2, limit):  # try each starting number
        newLength = collatz_length(i)
        if newLength > maxLength:  # found a new biggest one
            # update the max variables
            maxLength = newLength
            maxStartingValue = i
    return maxStartingValue
print(find_longest_collatz(1000))
