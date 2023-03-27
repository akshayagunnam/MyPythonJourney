
total = 0   # Will keep a running total of square numbers
currentNumber = 1

while (currentNumber <= 100):
    nextSquareNumber = currentNumber * currentNumber   # Will be the square of the current number
    total = total + nextSquareNumber   # Will add the current square to the total
    currentNumber = currentNumber + 1

print(total)   # Output the sum of the squares of the first 100 positive integers.
