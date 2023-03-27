def player_turnX():
    #Player X's turn

    #setup
    lst = []

    #putting the current game board into a list
    with open('file.txt') as f:
        while (line := f.readline().rstrip()):
            lst.append(line+"\n")

    #finding out player names
    name = open('nameFile.txt','r')
    namee = open('nameFilee.txt','r')
    nameX = (name.read())
    nameO = (name.read())
    
    f = open('file.txt', 'w')
    #player input for which column they want to place "X" in
    playX = input(str(nameX) + ", you're X. What column do you want to play in?")

    #error messages
    if playX.isnumeric() == False:
        #if the input is not a number, show the error message
        print("PICK A NUMBER BETWEEN 0 AND 6.\n")
        playX = int(input(str(nameX) + ", you're X. What column do you want to play in?"))
    if int(playX) > 6:
        #if input number is greater than 6, show error message
        print("PICK A NUMBER BETWEEN 0 AND 6.\n")
        playX = int(input(str(nameX) + ", you're X. What column do you want to play in?"))
    if int(playX) < 0:
         #if input number is less than 0, show error message
        print("PICK A NUMBER BETWEEN 0 AND 6.\n")
        playX = int(input(str(nameX) + ", you're X. What column do you want to play in?"))
        
    #player turn X
    else:
        playX = int(playX)
        for i in range(0,6):
            if "X" not in (lst[6-i].split())[playX] and "O" not in (lst[6-i].split())[playX]:
                #if the spot is empty place it there, else place it above
                row = lst[6-i].split()
                row[playX] = "X"
                row.append("\n")
                lst[6-i] = ' '.join(row)
                #add current game board to file
                f.writelines(lst)
                break
    #print current game board
    with open('file.txt', 'r') as f:
        print("\n")
        print(f.read())


def player_turnO():
    #Player O's turn
    
    #setup
    lst = []

    #putting the current game board into a list
    with open('file.txt') as f:
        while (line := f.readline().rstrip()):
            lst.append(line+"\n")

    #finding out player names
    name = open('nameFile.txt','r')
    namee = open('nameFilee.txt','r')
    nameX = (name.read())
    nameO = (namee.read())
    
    f = open('file.txt', 'w')
    #player input for which column they want to place "O" in
    playO = input(str(nameO) + ", you're O. What column do you want to play in?")

    #error messages
    if playO.isnumeric() == False:
        #if the input is not a number, show the error message
        print("PICK A NUMBER BETWEEN 0 AND 6.\n")
        playO = int(input(str(nameO) + ", you're O. What column do you want to play in?"))
    if int(playO) > 6:
        #if input number is greater than 6, show error message
        print("PICK A NUMBER BETWEEN 0 AND 6.\n")
        playO = int(input(str(nameO) + ", you're O. What column do you want to play in?"))
    if int(playO) < 0:
        #if input number is less than 0, show error message
        print("PICK A NUMBER BETWEEN 0 AND 6.\n")
        playO = int(input(str(nameO) + ", you're O. What column do you want to play in?"))

    #player turn O
    else:
        playO = int(playO)
        for i in range(0,6):
            if "X" not in (lst[6-i].split())[playO] and "O" not in (lst[6-i].split())[playO]:
                #if the spot is empty place it there, else place it above
                row = lst[6-i].split()
                row[playO] = "O"
                row.append("\n")
                lst[6-i] = ' '.join(row)
                #add current game board to file
                f.writelines(lst)
                break
    #print current game board
    with open('file.txt', 'r') as f:
        print("\n")
        print(f.read())


def winning_verticalX():
        
    #setup
    lst = []
    score = 0

    #finding out player names
    name = open('nameFile.txt','r')
    namee = open('nameFilee.txt','r')
    nameX = (name.read())
    nameO = (namee.read())
    
    #putting the current game board into a list
    with open('file.txt') as f:
        while (line := f.readline().rstrip()):
            lst.append(line)
    
    for i in range (1,4):     #rows
        lst[i].split(' ')     #induvidual spots in each row
        for k in range (0,6): 
            if (lst[i].split(' '))[k] == "X" and (lst[i+1].split(' '))[k] == "X" and (lst[i+2].split(' '))[k] == "X" and (lst[i+3].split(' '))[k] == "X":
                #if there are 4 "X"s in the same spot but one row up compared to the last one, win. 
                print ("Congratulations, "+nameX+", you won!") #
                #after winning, erase files and end program
                f = open("file.txt",'w')
                f.close()
                nameX = open("nameFile.txt",'w')
                nameX.close()
                nameO = open("nameFilee.txt",'w')
                nameO.close()
                raise SystemExit       
            
def winning_verticalO():
    
    #setup
    lst = []
    score = 0

    #finding out player names
    name = open('nameFile.txt','r')
    namee = open('nameFilee.txt','r')
    nameX = (name.read())
    nameO = (namee.read())
    
    #putting the current game board into a list
    with open('file.txt') as f:
        while (line := f.readline().rstrip()):
            lst.append(line)

    for i in range (1,4):     #rows
        lst[i].split(' ')     #induvidual spots in each row
        for k in range (0,6):
            if (lst[i].split(' '))[k] == "O" and (lst[i+1].split(' '))[k] == "O" and (lst[i+2].split(' '))[k] == "O" and (lst[i+3].split(' '))[k] == "O":
                #if there are 4 "O"s in the same spot but one row up compared to the last one, win.
                print ("Congratulations, "+nameO+", you won!")
                #after winning, erase files and end program
                f = open("file.txt",'w')
                f.close()
                nameX = open("nameFile.txt",'w')
                nameX.close()
                nameO = open("nameFilee.txt",'w')
                nameO.close()
                raise SystemExit
    
                
def winning_horizontalX():

    #setup
    lst = []

    #finding out player names
    name = open('nameFile.txt','r')
    namee = open('nameFilee.txt','r')
    nameX = (name.read())
    nameO = (namee.read())

    #putting the current game board into a list
    with open('file.txt') as f:
        while (line := f.readline().rstrip()):
            lst.append(line)

    for i in range (1,7):     #rows
        for k in range (0,4): #only need first 4 induvidual spots in rows because there needs to be space left for the other 3 "X"s
            if (lst[i].split(' '))[k] == "X" and (lst[i].split(' '))[k+1] == "X" and (lst[i].split(' '))[k+2] == "X" and (lst[i].split(' '))[k+3] == "X":
                #if there are 4 "X"s in same row, different spots one after another
                print ("Congratulations, "+nameX+", you won!")
                #after winning, erase files and end program
                f = open("file.txt",'w')
                f.close()
                nameX = open("nameFile.txt",'w')
                nameX.close()
                nameO = open("nameFilee.txt",'w')
                nameO.close()
                raise SystemExit


def winning_horizontalO():
    
    #setup
    lst = []

    #finding out player names
    name = open('nameFile.txt','r')
    namee = open('nameFilee.txt','r')
    nameX = (name.read())
    nameO = (namee.read())
    
    #putting the current game board into a list
    with open('file.txt') as f:
        while (line := f.readline().rstrip()):
            lst.append(line)
    
    for i in range (1,7):     #rows
        for k in range (0,4): #only need first 4 induvidual spots in rows because there needs to be space left for the other 3 "O"s
            if (lst[i].split(' '))[k] == "O" and (lst[i].split(' '))[k+1] == "O" and (lst[i].split(' '))[k+2] == "O" and (lst[i].split(' '))[k+3] == "O":
                #if there are 4 "O"s in same row, different spots one after another
                print ("Congratulations, "+nameO+", you won!")
                #after winning, erase files and end program
                f = open("file.txt",'w')
                f.close()
                nameX = open("nameFile.txt",'w')
                nameX.close()
                nameO = open("nameFilee.txt",'w')
                nameO.close()
                raise SystemExit


def winning_diagonalX():
    
    #setup
    lst = []
    score = 0

    #finding out player names
    name = open('nameFile.txt','r')
    namee = open('nameFilee.txt','r')
    nameX = (name.read())
    nameO = (namee.read())
    
    #putting the current game board into a list
    with open('file.txt') as f:
        while (line := f.readline().rstrip()):
            lst.append(line)

    #forward diagonal
    for i in range (1,6):     #rows
        for k in range (0,3): #only induvidual spots 0 thru 3 in each row because only those spots can go forward diagonal
            if (lst[-i].split(' '))[k] == "X" and (lst[-i-1].split(' '))[k+1] == "X" and (lst[-i-2].split(' '))[k+2] == "X" and (lst[-i-3].split(' '))[k+3] == "X":
                #if there are 4 "X"s, one row and one spot more than the last one, win
                print ("Congratulations, "+nameX+", you won!")
                #after winning, erase files and end program
                f = open("file.txt",'w')
                f.close()
                nameX = open("nameFile.txt",'w')
                nameX.close()
                nameO = open("nameFilee.txt",'w')
                nameO.close()
                raise SystemExit

    #backward diagonal
    for i in range (1,6):     #rows
        for k in range (3,7): #only induvidual spots 3 thru 7 in each row because only those spots can go backward diagonal
            if (lst[-i].split(' '))[k] == "X" and (lst[-i-1].split(' '))[k-1] == "X" and (lst[-i-2].split(' '))[k-2] == "X" and (lst[-i-3].split(' '))[k-3] == "X":
                #if there are 4 "X"s, one row and one spot more than the last one, win
                print ("Congratulations, "+nameX+", you won!")
                #after winning, erase files and end program
                f = open("file.txt",'w')
                f.close()
                nameX = open("nameFile.txt",'w')
                nameX.close()
                nameO = open("nameFilee.txt",'w')
                nameO.close()
                raise SystemExit
                
def winning_diagonalO():

    #setup
    lst = []
    score = 0

    #finding out player names
    name = open('nameFile.txt','r')
    namee = open('nameFilee.txt','r')
    nameX = (name.read())
    nameO = (namee.read())
    
    #putting the current game board into a list
    with open('file.txt') as f:
        while (line := f.readline().rstrip()):
            lst.append(line)

    #forward diagonal
    for i in range (1,6):     #rows
        for k in range (0,3): #only induvidual spots 0 thru 3 in each row because only those spots can go forward diagonal
            if (lst[-i].split(' '))[k] == "O" and (lst[-i-1].split(' '))[k+1] == "O" and (lst[-i-2].split(' '))[k+2] == "O" and (lst[-i-3].split(' '))[k+3] == "O":
                #if there are 4 "X"s, one row and one spot more than the last one, win
                print ("Congratulations, "+nameO+", you won!")
                #after winning, erase files and end program
                f = open("file.txt",'w')
                f.close()
                nameX = open("nameFile.txt",'w')
                nameX.close()
                nameO = open("nameFilee.txt",'w')
                nameO.close()
                raise SystemExit

    #backward diagonal
    for i in range (1,6):     #rows
        for k in range (3,7): #only induvidual spots 3 thru 7 in each row because only those spots can go backward diagonal
            if (lst[-i].split(' '))[k] == "O" and (lst[-i-1].split(' '))[k-1] == "O" and (lst[-i-2].split(' '))[k-2] == "O" and (lst[-i-3].split(' '))[k-3] == "O":
                #if there are 4 "X"s, one row and one spot more than the last one, win
                print ("Congratulations, "+nameO+", you won!")
                #after winning, erase files and end program
                f = open("file.txt",'w')
                f.close()
                nameX = open("nameFile.txt",'w')
                nameX.close()
                nameO = open("nameFilee.txt",'w')
                nameO.close()
                raise SystemExit


def connect_four():

    PlayerX = input("Player X, enter your name: ")  #player X name
    PlayerO = input("Player O, enter your name: ")  #player O name

    #player X name file
    name = open('nameFile.txt','w')
    name.writelines(PlayerX)
    name = open('nameFile.txt','r')
    
    #player O name file
    namee = open('nameFilee.txt','w')
    namee.writelines(PlayerO)
    namee = open('nameFilee.txt','r')
    
    print("")
    #add starting game board to a file
    f = open("file.txt", 'w') 

    #starting game board in a list
    lst = ["0 1 2 3 4 5 6\n", ". . . . . . .\n", ". . . . . . .\n", ". . . . . . .\n", ". . . . . . .\n", ". . . . . . .\n", ". . . . . . .\n", ]
    f.writelines(lst)

    #print starting game board
    with open('file.txt', 'r') as f:
        print(f.read())
        
    #gameplay
    for i in range (0, 21):  #maximum of 21 turns for each person because there are only 42 spots on the board
        #player X
        player_turnX()

        #check if playerX has won
        winning_verticalX()
        winning_horizontalX()
        winning_diagonalX()
            
        #player O
        player_turnO()

        #check if player O has won
        winning_verticalO()
        winning_horizontalO()
        winning_diagonalO()

connect_four()
