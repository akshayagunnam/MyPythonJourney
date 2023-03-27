print (n for n in range(110,1000,11) if n/11 == sum([int(d)**2 for d in str(n)]))
