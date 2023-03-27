import json
#open file and read the words, output as a list

def load_words():
    try:
        filename = "dictionary_2.json"
        with open(filename,"r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words

    except Exception as e:
        return str(e)




# takes letters from user and creates all combinations of the letters
def scrabble_input(a):
    l=[]
    for i in range(len(a)):
        if a[i] not in l:
            l.append(a[i])
        for s in scrabble_input(a[:i] + a[i + 1:]):
            if (a[i] + s) not in l:
                l.append(a[i] + s)
                

    return l

#finds all words that can be made with the input by matching combo's to the dictionary and returns them
def word_check(A):
    
    for word in scrabble_input(A):
        if word in words_in_dictionary:
            yield word


#gives each word a score
def values(input):
    # scrabble values
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
    word_total = 0
    for word in word_check(input):
        for i in word:
            word_total = word_total + score[i.lower()]
        yield (word_total, str(word))
        word_total = 0

#prints the tuples that have (scrabble score, word used)
def print_words(a):
    for i in values(a):
        print (i)

#final line to run, prints answer
def answer(a):
    print ('Your highest score is', max(values(a))[0], ', and below are all possible words:')
    print_words(a)

answer(input("Enter your 7 letters"))
