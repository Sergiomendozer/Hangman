from tkinter import *
from tkinter import Button

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

def submit ():
    return
    
#front end label and buttons
wrong_guesses = Label(root, text = "wrong Guesses", font=("Helvetica", 25),justify=CENTER)

correct_or_wrong_guess = Label(root, text = "correct_or_wrong_guess",font=("Helvetica", 25), justify=CENTER)

word_to_guess= Label(root, text = "_ _ _ _ _",font=("Helvetica", 25), justify=CENTER)

congrats= Label(root, text = "congrats",font=("Helvetica", 25), justify=CENTER)

entry_box = Entry(root, width = 5,font=("Helvetica", 25) )

submit = Button(root, text = "submit",font=("Helvetica", 18),bg="#B900FF", command=submit )
# positions
top= Label(root)
top.pack()
correct_or_wrong_guess.pack()
wrong_guesses.pack()
word_to_guess.pack()
entry_box.pack()
submit.pack ()
congrats.pack()

root.mainloop()