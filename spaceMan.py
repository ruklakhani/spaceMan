import random

# Declarations
fave_words = ["cooky", "imagine", "incredible"]

# user input return
def user_input(prompt):
    # validation
    try:
        i = input(prompt)

        while i == "":
            i = input("Input needed")
        return i

    except(err):
        print("Error: {}".format(err))

# randomized word based on topic selection
def pickWord():
    # choice = user_input("Topic? \n 1 - ruk's favorite words \n\n")
    #
    # # choice
    # if choice == "1":
        # pick a random index appropriate for the given chosen index
    rand = random.randint(1, len(fave_words) - 1)
    hiddenWord = fave_words[rand]
    # tuple to return index and word
    hiddenValues = (len(hiddenWord), hiddenWord)
    return hiddenValues
    # else:
    #     print("Invalid response- pick again \n")
    #     pickWord()


def play(word):

    # declarations
    hiddenWord = word[1]
    hiddenLength = word[0]
    lives = 7
    end = False
    blanks = ["X"]
    counter = 0

    # populate blanks appropriately
    for x in range(hiddenLength - 1):
        blanks.append("X")

    # run loop and main process
    while not end:

        # readout
        joined = ' '.join(blanks)
        print(joined + '\n')
        print("Guesses: {}\n\n".format(lives))
        guess = user_input("Guess a letter: \n")

        # correct/incorrect
        wrong = True

        for i, x in enumerate(hiddenWord):
            if guess == x:
                wrong = False
                blanks[i] = x
                counter += 1

        if not wrong:
            print("HECK YEAH !!! :^) \n")
            done = False
            lose1 = False
        else:
            print("Oof pal, try again \n")
            lives = lives - 1

        # end conditions
        if (lives == 0):
            print("Wapow! You goofed it... Try again?")
        elif (counter == hiddenLength):
            print("Oooooooh BAYBEE")

        # play again
        if lives == 0 or counter == hiddenLength:
            again = user_input("Wanna go again? (Y/N) \n")
            again = again.lower()

            try:
                if(code == "y"):
                    blanks = ["X"]
                    lives = 7
                    return False
                if(code == "n"):
                    return
            except:
                print("Invalid input")
                return True


def test():
    assert("cooky" in fave_words), "FAILEDDD"


#initial run
test()
done = False
code = user_input("Play? (Y/N)\n")
code = code.lower()

if code == "n":
    done = True

#run loop
while not done:
    done = play(pickWord())
