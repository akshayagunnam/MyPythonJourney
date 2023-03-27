# Python Class 3337
# Lesson 6 Problem 6 part (b)
# Author: Calculus_sus (950197)
def backgammon_roll():

   scoreList1 = []
   scoreList2 = []
   total1 = 0
   total2 = 0
   for i in range (0,50):
        start1 = input("Player 1, press enter to roll")
        import random
        roll1 = random.randrange(7)
        roll2 = random.randrange(7)
        score1 = 0
        score2 = 0
        if start1 == '':
            if roll1 == roll2:
                score1 = ((roll1 + roll2)*2)
                print ("Player 1 rolled", score1)
            else:
                score1 = (roll1 + roll2)
                print ("Player 1 rolled", score1)
        scoreList1.append(score1)
        for j in range(0, len(scoreList1)):
            total1 = total1 + scoreList1[j]

        print ("")
        print ("SCORE:")
        print ("PLAYER 1 -",total1)
        print ("PLAYER 2 -",total2)
        print ("")

        start2 = input("Player 2, press enter to roll")
        import random
        roll1 = random.randrange(7)
        roll2 = random.randrange(7)
        if start2 == '':
            if roll1 == roll2:
                score2 = ((roll1 + roll2)*2)
                print ("Player 2 rolled", score2)
            else:
                score2 = (roll1 + roll2)
                print ("Player 2 rolled", score2)
        scoreList2.append(score2)
        for j in range(0, len(scoreList2)):
            total2 = total2 + scoreList2[j]
        
        print ("")
        print ("SCORE:")
        print ("PLAYER 1 -",total1)
        print ("PLAYER 2 -",total2)
        print ("")

        if total1 >= 100:
             print ("Player 1 wins!")
             break
        elif total2 >= 100:
            print ("Player 2 wins!")
            break
            
backgammon_roll()

