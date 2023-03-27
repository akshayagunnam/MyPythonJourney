string = input("string = ")     

wordsInString = string.split()      

numWordsInStr = len(wordsInString)     

x = numWordsInStr - 1       
    
lastWord = string.split(' ')[x]     

solution = len(lastWord) - lastWord.count(' ')

print(solution)



