import random

word = "Agent Anger Award Beach Beans Brick Birth Block Bacon Bagel Board Brain Bingo Bread Break Brown Buyer Candy Cause Chain Chair Chest Chief Child China Claim Coast Court Cover Cream Crime Crowd Crown Dirty Daily Dairy Dance Death Depth Draft Dream Demon Devil Drink Drive Earth Enemy Entry Event Faith Fault Field Fight Final Focus Force Frame Frank Front Fruit Grant Group Guide Heart Henry Horse Hotel House Image Index Input Japan Jones Judge Knife Layer Lewis Light Lunch Major March Match Metal Model Money Month Mouth Music Night Noise North Novel Nurse Other Owner Panel Party Phase Phone Piece Pilot Pitch Place Plane Plant Plate Point Pound Power Price Pride Prize Radio Range Ratio Reply Right River Round Route Rugby Scale Scope Score Shape Share Shift Shirt Shock Sight Simon Smile Smith Smoke Sound South Space Spite Sport Squad Stage Start State Steam Steel Stock Stone Store Study Stuff Style Sugar Table  Thing Touch Tower Track Trade Train Trend Trial Trust Truth Uncle Unity Value Video Voice Waste Watch Water While White Whole Woman World Youth Zebra Jumpy Ducks Abort Cable Games Grape Greek Gipsy Holes Habit Miles Maybe Mayor Media Movie Safer Sauce Rocks Raids Risky Under Unzip Vegas"
# makes the list of words into a list
list_of_words = list(word.split(" "))
# picks a random word
chosen_word = random.choice(list_of_words)
print (chosen_word)#! for testing
# print("Wrong Guesses: " + wrong_guesses)
wrong_guesses = ""
partial_word = "_ _ _ _ _"
print(partial_word) #! for testing
# guess = input("Enter a letter and press enter: ")
# hangman(wrong_guesses, chosen_word, partial_word, guess)


def hangman(wrong_guesses, chosen_word, partial_word, guess):
    if (
        guess[0] == chosen_word[0]
        or guess[0].upper() == chosen_word[0]
        or guess[0] == chosen_word[0].upper()
    ):
        partial_word = partial_word.split()
        partial_word[0] = chosen_word[0]
        partial_word = " ".join([str(element) for element in partial_word])
        return is_word_guessed(wrong_guesses, chosen_word, partial_word, guess)
    elif (
        guess[0] == chosen_word[1]
        or guess[0].upper() == chosen_word[1]
        or guess[0] == chosen_word[1].upper()
    ):
        partial_word = partial_word.split()
        partial_word[1] = chosen_word[1]
        partial_word = " ".join([str(element) for element in partial_word])
        return is_word_guessed(wrong_guesses, chosen_word, partial_word, guess)
    elif (
        guess[0] == chosen_word[2]
        or guess[0].upper() == chosen_word[2]
        or guess[0] == chosen_word[2].upper()
    ):
        partial_word = partial_word.split()
        partial_word[2] = chosen_word[2]
        partial_word = " ".join([str(element) for element in partial_word])
        return is_word_guessed(wrong_guesses, chosen_word, partial_word, guess)
    elif (
        guess[0] == chosen_word[3]
        or guess[0].upper() == chosen_word[3]
        or guess[0] == chosen_word[3].upper()
    ):
        partial_word = partial_word.split()
        partial_word[3] = chosen_word[3]
        partial_word = " ".join([str(element) for element in partial_word])
        return is_word_guessed(wrong_guesses, chosen_word, partial_word, guess)
    elif (
        guess[0] == chosen_word[4]
        or guess[0].upper() == chosen_word[4]
        or guess[0] == chosen_word[4].upper()
    ):
        partial_word = partial_word.split()
        partial_word[4] = chosen_word[4]
        partial_word = " ".join([str(element) for element in partial_word])
        return is_word_guessed(wrong_guesses, chosen_word, partial_word, guess)
    else:
        wrong_guesses = wrong_guesses + " " + guess
        print("\033[31m" + "Wrong Guesses: " + wrong_guesses + "\033[0m")
        print(
            "\033[31m"
            + "The Letter "
            + guess
            + " is not in word, guess again:"
            + "\033[0m"
        )
        print(partial_word)
        return hangman(wrong_guesses, chosen_word, partial_word, input())