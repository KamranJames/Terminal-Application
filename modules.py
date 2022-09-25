from simple_term_menu import TerminalMenu

# Function that intiailizes our game.
def game():
    game = True 


# Contains the three levels conditions.
class Levels:
    def __init__(self, lvlone, lvltwo, lvlthree):
        self.lvlone = lvlone
        self.lvltwo = lvltwo
        self.lvlthree = lvlthree
        self.lvlcancel = lvlcancel

levels = Levels
levels.lvlone = True
levels.lvltwo = False
levels.lvlthree = False
levels.lvlcancel = True

# Keeps count of the users guesses.
class Guess_Counter:
    def __init__(self, guessnum,):
        self.guessnum = guessnum

guess = Guess_Counter
guess.guessnum = 0 

# The main menu function.
def main():
    print(f"Welcome to Riddle Riddle!! Please enter your name:")
    name = usrname()
    
    print(f"Hello\n" +name+ "\nNow select your difficulty level. The higher difficulty you choose the less guesses you get.")
    main_menu_items = ["Easy = 4 guesses", "Medium = 3 guesses ", "Hard = 2 guesses",
                     "Quit"]
    terminal_menu = TerminalMenu(main_menu_items)
    menu_entry_index = terminal_menu

    main_menu = TerminalMenu(
        menu_entries=main_menu_items,)
    
    while True and levels.lvlcancel:
        main_sel = main_menu.show()

        if main_sel == 0:
            guess.guessnum = 0
            return
            
        elif main_sel == 1:
            guess.guessnum = 1
            return
           
        elif main_sel == 2:
            guess.guessnum = 2
            return
           
        elif main_sel == 3:
            quit()

# Gets username.
def usrname():
    try:
        name = str(input())
    except TypeError:
        print ("A TypeError was raised. Please enter a string as your name.")
    return name

# Takes in the users guess.
def usranswr():
    try:
        answer = input()
        answer = answer.upper()
    except ValueError:
        print ("A ValueError was raised. Please select from the options provided")
    return answer 


# Change difficulty menu.
def check():
    print("Would you like to change difficulty? \n")
    main_menu_items = ["Easy = 4 guesses", "Medium = 3 guesses ", "Hard = 2 guesses",
                     "Quit"]
    terminal_menu = TerminalMenu(main_menu_items)
    menu_entry_index = terminal_menu

    main_menu = TerminalMenu(
        menu_entries=main_menu_items,)
    
    while True and levels.lvlcancel:
        main_sel = main_menu.show()

        if main_sel == 0:
            guess.guessnum = 0
            return

        elif main_sel == 1:
            guess.guessnum = 1
            return

        elif main_sel == 2:
            guess.guessnum = 2
            return

        elif main_sel == 3:
            quit()










