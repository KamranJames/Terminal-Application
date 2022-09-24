from simple_term_menu import TerminalMenu

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

class Guess_Counter:
    def __init__(self, guessnum, guesstell):
        self.guessnum = guessnum

guess = Guess_Counter
guess.guessnum = 0 

def main():
    print("Welcome to Riddle me this!! select your difficulty level. The higher difficulty you choose the less guesses you get. \n")
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


def usranswr():
    try:
        answer = input()
        answer = answer.upper()
    except ValueError:
        print ("A ValueError was raised. Please select from the options provided")
    except NameError:
        print ("A NameError was raised. Please select from the options provided")
   
    return answer 

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

def game():
    game = True 









