def number_guess():
    import random
    guess = -1
    number = random.randrange(0,101)
    while guess != number:
        guess = int(input("Enter your guess: "))
        if int(guess) > int(number):
            print("Sorry,",guess,"is too high.")
        if guess < number:
            print("Sorry,",guess,"is too low.")

    print("Good Job!",number,"is my number.")
number_guess()
