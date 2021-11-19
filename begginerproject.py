import random
#libraray that uses in oder to choose
#on random words in list of words
name =input("what is your name:")

print("Good luck",name)

words =['rainbow','computer','science','programming','python','matheamtics','player','condition','reverse','water','board','geeks']
#Function will choose one random
#word from this list of words
word = random.choice(words)

print("Guess the character")

guesses =''
#number times to be used
turns = 10
while turns>0:
    #count failed times of user
    failed =0
    #all characters from the input
    #word taking one at a time
    for char in word:
        #comparing that character with the character in guesses
        if char in guesses:
            print(char)
        else :
            print("_")
            #for every failure 1 will be increment in failure
            failed+=1
    if failed==0:
        print("the word is :",word)
        break
    guess =input("guess a character")
    guesses+=guess

    if guess not in word:
        turns -=1
        if turns ==0:
            print("you loose")
            print(word)

