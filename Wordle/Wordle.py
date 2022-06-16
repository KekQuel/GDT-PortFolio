import random
import FiveWordsDictionary
# 2500 words! (I used a website to copy and paste a list of words here and compile them into a list)


def split(word):  # Credit: https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
    return [char for char in word]  # This splits the chosen word for Wordle into 5 different letters.


# I discovered how to use functions properly (Based on the pattern above)!!!
# This function checks each letter for its status.
def Colour(i=0 or 1 or 2 or 3 or 4):
    if xSplit[i] == ChosenWord[i]:
        return 2  # 2 (green) represents correct letter, correct position.
    elif xSplit[i] == ChosenWord[0] or xSplit[i] == ChosenWord[1] or xSplit[i] == ChosenWord[2] or xSplit[i] == ChosenWord[3] or xSplit[i] == ChosenWord[4]:
        return 1  # 1 (yellow) represents correct letter, wrong position.
    elif xSplit[i] != ChosenWord[i]:
        return 0  # 0 (grey) represents wrong letter, wrong position.


Attempts = 1  # Buffer
ChosenWord = FiveWordsDictionary.Words[random.randint(0, 2499)]  # Randomly choose words from FiveWordsDictionary

while Attempts <= 6:  # Wordle has 6 attempts given to guess the correct word.
    print("Line " + str(Attempts))
    x = input("Type a five letter word in all caps! "
              "Word list from https://eslforums.com/5-letter-words/ "
              "(0 - Grey; 1 - Yellow, 2 - Green): ")

    if x in FiveWordsDictionary.Words:
        xSplit = split(x)  # Split chosen words
        ColourOne = Colour(0)  # Checks every character to see if it matches
        ColourTwo = Colour(1)
        ColourThree = Colour(2)
        ColourFour = Colour(3)
        ColourFive = Colour(4)
        print(xSplit[0], xSplit[1], xSplit[2], xSplit[3], xSplit[4])
        print(str(ColourOne), str(ColourTwo), str(ColourThree), str(ColourFour), str(ColourFive))
        if ColourOne + ColourTwo + ColourThree + ColourFour + ColourFive == 10:  # All green = win!
            print("You Win!")
            break
        else:  # Messing up once will add another point in the counter. Do that 6 times and game over.
            Attempts = Attempts + 1

    else:
        print("That does not work!")

if Attempts == 7:
    print("Game Over!")
