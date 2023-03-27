x = input("x = ")
digits = len(str(x))
list = str(x).split()
y = -1
z = 0
while y < int(x)/2 and z < int(x)/2:
    list[y] == list[z]
    y = y + 1
    z = z + 1

if list[y] != list[z]:
    print ("False")

elif list[y] == list[z]:
    print ("True")

            
