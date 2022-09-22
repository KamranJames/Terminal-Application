from simple_term_menu import TerminalMenu

class Guess_Counter:
  def __init__(self, guessnum):
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
        menu_entries=main_menu_items,
      
    )
    
    while True:
        main_sel = main_menu.show()

        if main_sel == 0:
            guess.guessnum == 0
            break
            
        elif main_sel == 1:
            guess.guessnum +=1
            break
            
        elif main_sel == 2:
            guess.guessnum +=2
            break
           
        elif main_sel == 3:
            main_menu_exit = True
            quit()


if __name__ == "__main__":
    main()
