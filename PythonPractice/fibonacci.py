a = int(input('n = '))

def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

lastNum = int(a[a - 1])
secondLast = a[a - 2]
newNum = lastNum + secondLast

a.insert(1,newNum)
nth = a[a + 1]

print(nth)
