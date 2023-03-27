for row in range(10):        # row goes from 0 to 9
    rowString = str(row)     # row label
    for column in range(10): # column goes from 0 to 9
        rowString += '\t' + str(row * column) # add tab and product
    print(rowString)         # print row
