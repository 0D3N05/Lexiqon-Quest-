import random



def chooseRandomWord(): 
    wordlist = ["apple", "beach", "chair", "dance", "eleph", "frost", "grape", "haste", "image", "jolly",
             "knock", "lemon", "mirth", "noble", "oasis", "piano", "queen", "rider", "swirl", "teeth",
             "unity", "vivid", "wrist", "xerox", "young", "zebra", "charm", "blitz", "fable", "plumb"]
    n = random.choice(wordlist)
    return(n)

def CorrectInput(input): #Check if input is 5 letter word or not 
    input = input.strip().lower()

    if len(input) != 5:
        
        return False
    
    else:
        return True

def CorrectWord(wordtocheck):   #Decides the yellow and green part in wordle and correct or not
    if(wordtocheck == wordAnswer):
        return True
    else:
        wordtocheck = list(wordtocheck)
        AnswerArray = list(wordAnswer)
        i = 0
        for x in wordtocheck:
            if wordtocheck[i] == AnswerArray[i]:
                print(wordtocheck[i]+ ' is in position ' + str(i))
                i = i + 1
            elif wordtocheck[i] in AnswerArray:
                print(wordtocheck[i] + " is in the word but wrong position")
                i = i + 1
            else:
                print(wordtocheck[i] + ' is not in the word')
                i = i + 1
        return False

#Game Code Down Here

wordAnswer = chooseRandomWord()
print("welcome to wordle")
#print(wordAnswer)


while True:  #While True, keep asking input
    playerWord = input('Enter your word here: ')
    if CorrectInput(playerWord) == False: #if weird  input, ask again
        print("Please enter a five letter word")
        continue

    if CorrectInput(playerWord) == True: #if correct input , check it
        if CorrectWord(playerWord) == True: #if guess is correct, exit game
            print("very smart u did it")
            break                 #if correct guess, end game
        else:
            continue               #if wrong, keep asking question


    
