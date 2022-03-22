from tkinter import *
from tkinter import Button
import random

# root= tk.Tk()
root = Tk()
root.title("Word Solver")
root.geometry("800x400")
root.configure()

class Window_Functions:
    # Center's window
    app_width = 800
    app_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (app_width / 2)
    y_coordinate = (screen_height / 2) - (app_height / 2)
    root.geometry(f"{app_width}x{app_height}+{int(x_coordinate)}+{int(y_coordinate)}")


word = "Agent Anger Award Beach Beans Brick Birth Block Bacon Bagel Board Brain Bingo Bread Break Brown Buyer Candy Cause Chain Chair Chest Chief Child China Claim Coast Court Cover Cream Crime Crowd Crown Dirty Daily Dairy Dance Death Depth Draft Dream Demon Devil Drink Drive Earth Enemy Entry Event Faith Fault Field Fight Final Focus Force Frame Frank Front Fruit Grant Group Guide Heart Henry Horse Hotel House Image Index Input Japan Jones Judge Knife Layer Lewis Light Lunch Major March Match Metal Model Money Month Mouth Music Night Noise North Novel Nurse Other Owner Panel Party Phase Phone Piece Pilot Pitch Place Plane Plant Plate Point Pound Power Price Pride Prize Radio Range Ratio Reply Right River Round Route Rugby Scale Scope Score Shape Share Shift Shirt Shock Sight Simon Smile Smith Smoke Sound South Space Spite Sport Squad Stage Start State Steam Steel Stock Stone Store Study Stuff Style Sugar Table  Thing Touch Tower Track Trade Train Trend Trial Trust Truth Uncle Unity Value Video Voice Waste Watch Water While White Whole Woman World Youth Zebra Jumpy Ducks Abort Cable Games Grape Greek Gipsy Holes Habit Miles Maybe Mayor Media Movie Safer Sauce Rocks Raids Risky Under Unzip Vegas"
# makes the list of words into a list
list_of_words = list(word.split(" "))
# picks a random word
chosen_word = random.choice(list_of_words)
# print (chosen_word)#! for testing
wrong_guesses = ""
wrong_guesses_list = []
partial_word = "_ _ _ _ _"
# print(partial_word) #! for testing
############################################################
# def hangman(wrong_guesses, chosen_word, partial_word, guess):
def a_new_game():
    return

def submit ():
    global wrong_guesses, chosen_word, partial_word,wrong_guesses_list
    guess=entry_box.get()
    if (
        guess[0] == chosen_word[0]
        or guess[0].upper() == chosen_word[0]
        or guess[0] == chosen_word[0].upper()
    ):
        partial_word = partial_word.split()
        partial_word[0] = chosen_word[0]
        partial_word = " ".join([str(element) for element in partial_word])
        correct_or_wrong_guess.config(text = "Correct",font=("Helvetica", 25),fg = "#097100",justify=CENTER)
        word_to_guess.config(text = partial_word,font=("Helvetica", 25), justify=CENTER)
    elif (
        guess[0] == chosen_word[1]
        or guess[0].upper() == chosen_word[1]
        or guess[0] == chosen_word[1].upper()
    ):
        partial_word = partial_word.split()
        partial_word[1] = chosen_word[1]
        partial_word = " ".join([str(element) for element in partial_word])
        correct_or_wrong_guess.config(text = "Correct",font=("Helvetica", 25),fg = "#097100",justify=CENTER)
        word_to_guess.config(text = partial_word,font=("Helvetica", 25), justify=CENTER)
    elif (
        guess[0] == chosen_word[2]
        or guess[0].upper() == chosen_word[2]
        or guess[0] == chosen_word[2].upper()
    ):
        partial_word = partial_word.split()
        partial_word[2] = chosen_word[2]
        partial_word = " ".join([str(element) for element in partial_word])
        correct_or_wrong_guess.config(text = "Correct",font=("Helvetica", 25),fg = "#097100",justify=CENTER)
        word_to_guess.config(text = partial_word,font=("Helvetica", 25), justify=CENTER)
    elif (
        guess[0] == chosen_word[3]
        or guess[0].upper() == chosen_word[3]
        or guess[0] == chosen_word[3].upper()
    ):
        partial_word = partial_word.split()
        partial_word[3] = chosen_word[3]
        partial_word = " ".join([str(element) for element in partial_word])
        correct_or_wrong_guess.config(text = "Correct",font=("Helvetica", 25),fg = "#097100",justify=CENTER)
        word_to_guess.config(text = partial_word,font=("Helvetica", 25), justify=CENTER)
    elif (
        guess[0] == chosen_word[4]
        or guess[0].upper() == chosen_word[4]
        or guess[0] == chosen_word[4].upper()
    ):
        partial_word = partial_word.split()
        partial_word[4] = chosen_word[4]
        partial_word = " ".join([str(element) for element in partial_word])
        correct_or_wrong_guess.config(text = "Correct",font=("Helvetica", 25),fg = "#097100",justify=CENTER)
        word_to_guess.config(text = partial_word,font=("Helvetica", 25), justify=CENTER)
    else:
        wrong_guesses_list.append(guess[0])
        wrong_guesses_str = " ".join([str(element) for element in wrong_guesses_list])
        wrong_guess.config(text = "Wrong Guesses:" + wrong_guesses_str, font=("Helvetica", 25),fg = "#FF4A1B",justify=CENTER)
        

        # wrong_guesses = wrong_guesses + " " + guess
        # print("\033[31m" + "Wrong Guesses: " + wrong_guesses + "\033[0m")
        # print(
        #     "\033[31m"
        #     + "The Letter "
        #     + guess
        #     + " is not in word, guess again:"
        #     + "\033[0m"
        # )
        # print(partial_word)
    # print (wrong_guesses, chosen_word, partial_word,guess)#!for testing

#front end label and buttons

wrong_guess = Label(root, text = "Wrong Guesses:" + wrong_guesses, font=("Helvetica", 25),fg = "#FF4A1B",justify=CENTER)

correct_or_wrong_guess = Label(root, text = "",font=("Helvetica", 25), justify=CENTER)

word_to_guess= Label(root, text = partial_word,font=("Helvetica", 25), justify=CENTER)

congrats= Label(root, text = "congrats",font=("Helvetica", 25), justify=CENTER)

entry_box = Entry(root, width = 5,font=("Helvetica", 25) )

submit = Button(root, text = "Submit",font=("Helvetica", 18),bg="#B900FF", command=submit )
new_game = Button(root, text = "New Game",font=("Helvetica", 18),bg="#FF4A1B", command=a_new_game )

# positions
top= Label(root)
top.pack()
correct_or_wrong_guess.pack()
wrong_guess.pack()
word_to_guess.pack()
entry_box.pack()
submit.pack ()
congrats.pack()
new_game.pack()

root.mainloop()