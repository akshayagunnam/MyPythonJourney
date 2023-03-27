class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        numList = []
        for i in range (n + 1):
            numList.append(str(i))
        numList.remove("0")
        for a in range (int(n/3)):
            x = a*3 
            if n >= 3:
                numList[2+x] = "Fizz"
        for a in range (int(n/5)):
            x = a*5
            if n >= 5:
                numList[4+x] = "Buzz"
        for a in range (int(n/15)):
            x >= 15
            x = a*15
            if n >= 15:
                numList[x - 1] = "FizzBuzz"
        return numList

    
