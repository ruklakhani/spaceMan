import random

# Declarations
fave_words = ["cooky", "imagine", "incredible"]


# user input returns
def user_input(prompt):
    try:
        i = input(prompt)

        while i == "":
            i = input("Input needed")
        return i

    except(err):
        print("Error: {}".format(err))


# random word choices
def pickWord():
    choice = user_input("Topic? \n 1 - ruk's favorite words \n\n")

    if choice == "1":
        # pick index
        rand = random.randint(1, len(fave_words) - 1)
        hiddenWord = fave_words[rand]
        # tuple to return index and word
        hiddenValues = (len(hiddenWord), hiddenWord)
        return hiddenValues
    else:
        print("Invalid response- pick again \n")
        pickWord()
    if choice == "2":
        # pick index
        rand = random.randint(1, len(best_pals) - 1)
        hiddenWord = best_pals[rand]
        # tuple to return index and word
        hiddenValues = (len(hiddenWord), hiddenWord)
        return hiddenValues
    else:
        print("Invalid response- pick again \n")
        pickWord()


def play(word):
    # declarations
    hiddenWord = word[1]
    hiddenLength = word[0]
    lives = 7
    end = False
    blanks = ["X"]
    counter = 0

    # populate blanks
    for x in range(hiddenLength - 1):
        blanks.append("X")

    # run loop
    while not end:

        joined = ' '.join(blanks)
        print(joined + '\n')
        print("Guesses: {}\n\n".format(lives))
        guess = user_input("Guess a letter: \n")

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

        # the end
        if (lives == 0):
            print("Wapow! You goofed it... Try again?")
        elif (counter == hiddenLength):
            print("Oooooooh BAYBEE")

        # take two
        if lives == 0 or counter == hiddenLength:
            again = user_input("Wanna go again? (Y/N) \n")
            again = again.lower()

        # try:
        #     if(code == "y"):
        #         blanks = ["X"]
        #         lives = 7
        #         return False
        #     if(code == "n"):
        #         return
        # except:
        #     print("Invalid input")
        #     return True


# This is the only function I can test :(
def test():
    assert(pickWord() in fave_words), "pickWord() isn't working"



#initial run
done = False
code = user_input("Play? (Y/N)\n")
code = code.lower()

if code == "n":
    done = True


#run loop
while not done:
    done = play(pickWord())
