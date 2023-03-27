
date = input("What Is Today's Date? ")


if int(date) > 31:
    print ("ERROR! There are only 31 days in January.")

elif int(date) < 0:
    print ("ERROR! That's not a real date.")

elif int(date) % 7 == 1:
    print ("Today is a Sunday.")

elif int(date) % 7 == 2:
    print ("Today is a Monday.")

elif int(date) % 7 == 3:
    print ("Today is a Tuesday.")

elif int(date) % 7 == 4:
    print ("Today is a Wednesday.")

elif int(date) % 7 == 5:
    print ("Today is a Thursday.")

elif int(date) % 7 == 6:
    print ("Today is a Friday.")

elif int(date) % 7 == 0:
    print ("Today is a Saturday.")





