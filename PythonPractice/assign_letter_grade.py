def assign_letter_grade(score):
    if 96 <= score <= 100:
        print ("A+")
    elif 88 <= score <= 95:
        print ("A")
    elif 85 <= score <= 87:
        print ("B+")
    elif 80 <= score <= 84:
        print ("B")
    elif 77 <= score <= 79:
        print ("C+")
    elif 70 <= score <= 76:
        print ("C")
    elif 66 <= score <= 69:
        print ("D")
    elif 50 <= score <= 65:
        print ("F")
    elif 0 <= score <= 49:
        print ("I")
    else:
        print("Only Enter Numbers 0 - 100 as your score")


