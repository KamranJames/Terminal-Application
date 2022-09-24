import cowsay 
from colorama import init
from termcolor import colored
from modules import main
from modules import guess 
from modules import levels 
from modules import check
from modules import usranswr 
from modules import game
init()
f

game()
print(colored("""
██████╗░██╗██████╗░██████╗░██╗░░░░░███████╗░░░░░░██████╗░██╗██████╗░██████╗░██╗░░░░░███████╗
██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░██╔════╝░░░░░░██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░██╔════╝
██████╔╝██║██║░░██║██║░░██║██║░░░░░█████╗░░█████╗██████╔╝██║██║░░██║██║░░██║██║░░░░░█████╗░░
██╔══██╗██║██║░░██║██║░░██║██║░░░░░██╔══╝░░╚════╝██╔══██╗██║██║░░██║██║░░██║██║░░░░░██╔══╝░░
██║░░██║██║██████╔╝██████╔╝███████╗███████╗░░░░░░██║░░██║██║██████╔╝██████╔╝███████╗███████╗
╚═╝░░╚═╝╚═╝╚═════╝░╚═════╝░╚══════╝╚══════╝░░░░░░╚═╝░░╚═╝╚═╝╚═════╝░╚═════╝░╚══════╝╚══════╝""", 'green', 'on_blue'))
main()


while game:
    cowsay.cow(colored("Welcome to the guessing game your first riddle is: \n", 'green', 'on_cyan'))

    while guess.guessnum < 4 and levels.lvlone == True: 
        print("I am cool as a breeze, I stop your heart with ease, seasons may be my enemy, but im part of you and you are friend to me. What am I? \n")
        print("Enter your guess or type 'hint', 'answer' or 'quit' below.")
        answer = usranswr()
        guess.guessnum +=1
     
        if "SNEEZE" in answer:
           cowsay.cow(colored("Great work! Next level Options:  \n,", 'green', 'on_cyan'))
           guess.guessnum = 0
           levels.lvlone = False
           levels.lvltwo = True
           break
       
        elif answer == "HINT": 
           guess.guessnum -=1
           cowsay.cow(colored("Achoo!\n", 'green', 'on_cyan'))

        elif answer == "ANSWER": 
            guess.guessnum -=1 
            cowsay.cow(colored("Sneeze!\n", 'green', 'on_cyan'))
            break
          
        elif answer == "QUIT" or guess.guessnum == 4:
            cowsay.cow(colored("Better luck next time! ", 'green', 'on_cyan'))
            quit()

    check()
    while levels.lvltwo == True:
        cowsay.cow(colored("Your riddle is: \n,", 'green', 'on_cyan'))
        print("\n I am fast or I am slow, i'll keep you young and on your toes, your in charge of my tempo. What am I? \n")
        print("Enter your guess or type 'hint', 'answer' or 'quit' below.")
        answer = input()
        answer = answer.upper()
        guess.guessnum +=1

        if "RUNNING" in answer:
           cowsay.cow(colored("\n Great work! Final level Options: \n",'green', 'on_cyan'))
           levels.lvltwo = False
           levels.lvlthree = True 
           break

        elif answer == "HINT": 
         guess.guessnum -=1
         cowsay.cow(colored("A way to go places.\n",'green', 'on_cyan'))

        elif answer == "ANSWER":
           cowsay.cow(colored("Running!\n", 'green', 'on_cyan'))
           guess.guessnum -=1
           break

        elif answer == "QUIT" or guess.guessnum == 4:
           cowsay.cow(colored("Better luck next time! ", 'green', 'on_cyan'))
           quit()
        else:
            print(colored("Try again!",'green', 'on_cyan'))

    check()
    while levels.lvlthree == True:
        cowsay.cow(colored("You riddle is: \n,", 'green', 'on_cyan'))
        print("\n Pearl white chest without key or lid. Inside of which, a golden treasure is hid. What am I? \n")
        print("Enter your guess or type 'hint', 'answer' or 'quit' below.")
        answer = input()
        answer = answer.upper()
        guess.guessnum +=1

        if "EGG" in answer:
           print(colored("""
██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝""", 'green', 'on_blue'))
           cowsay.cow(colored("\n CONGRATULATIONS\n",'green', 'on_cyan'))
           levels.lvltwo = False
           levels.lvlthree = True 
           levels.lvlcancel = False
           quit()

        elif answer == "HINT": 
         guess.guessnum -=1
         cowsay.cow(colored("The creator of this chest is a farm animal\n",'green', 'on_cyan'))

        elif answer == "ANSWER":
           cowsay.cow(colored("Egg\n", 'green', 'on_cyan'))
           guess.guessnum -=1
           break

        elif answer == "QUIT" or guess.guessnum == 4:
           cowsay.cow(colored("Better luck next time! ", 'green', 'on_cyan'))
           quit()
        else:
            print(colored("Try again!",'green', 'on_cyan'))