def checkPerfectNum(n) :
    i = 2
    sum = 1

    while(i <= n//2):
        if (n % i == 0) :
            sum += i            
        i += 1
        if sum == n:
            print(n)

if __name__ == "__main__":

    list_of_integers = []
    for x in range (100, 1000):
            list_of_integers.append(x)
    for num in list_of_integers:
             if checkPerfectNum(num) != None:
                 print (checkPerfectNum(num))
   
        
