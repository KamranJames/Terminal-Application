
# class Guess_Counter:
#   def __init__(self, guessnum):
#    self.guessnum = guessnum

# guess = Guess_Counter
# guess.guessnum = 0 


import cowsay 
from colorama import init
from termcolor import colored
from testmodules import main
from testmodules import guess
init()
main()



# class Guess_Counter:
#   def __init__(self, guessnum):
#    self.guessnum = guessnum

# guess = Guess_Counter
# guess.guessnum = 0 

print("Welcome to the guessing game you have 4 guesses your first riddle is: \n")
while True and guess.guessnum < 4: 
    print("I am cool as a breeze, I stop your heart with ease, seasons may be my enemy, but im part of you and you are friend to me. What am I? \n")
    print("Enter your guess or type 'hint', or 'quit' below.")
    answer = input()
    answer = answer.lower()
    guess.guessnum +=1

    if "sneeze" in answer.lower():
       cowsay.cow(colored("Great work, your next riddle is: \n,",'green', 'on_cyan'))

       break

    elif answer == "hint": 
       guess.guessnum -=1
       cowsay.cow(colored("Achoo!\n",'green', 'on_cyan'))
        
    
    elif answer == "quit" or guess.guessnum == 4:
           print(colored("Better luck next time! ", "green", 'on_cyan'))
           quit()

    else:
        print("Try again!",'green', 'on_cyan')


while True and guess.guessnum < 4: 
    print("\n I am fast or I am slow, i'll keep you young and on your toes, your in charge of my tempo. What am I? \n")
    print("Enter your guess or type 'hint', or 'quit' below.")
    answer = input()
    answer = answer.lower()
    guess.guessnum +=1

    if "running" in answer:
       cowsay.cow(colored("\n Great work, your next riddle is: \n",'green', 'on_cyan'))
       break

    elif answer == "hint": 
       guess.guessnum -=1
       cowsay.cow("A way to go places.\n",'green', 'on_cyan')
    
    elif answer == "quit" or guess.guessnum == 4:
           cowsay.cow(colored("Better luck next time! ",'green', 'on_cyan'))
           quit()

    else:
        print(colored("Try again!",'green', 'on_cyan'))


while True and guess.guessnum < 4: 
    print(colored("Pearl white chest without key or lid. Inside of which, a golden treasure is hid. What am I?  \n",'green', 'on_cyan'))
    print("Enter your guess or type 'hint', or 'quit' below.",'green', 'on_cyan')
    answer = input()
    answer = answer.lower()
    guess.guessnum +=1

    if "egg" in answer:
       cowsay.cow(colored("\n CONGRATULATIONS, YOU ARE THE RIDDLE MASTER",'green', 'on_cyan'))
       break

    elif answer == "hint":
       guess.guessnum -=1
       cowsay.cow(colored("The creator of this chest is a farm animal\n",'green', 'on_cyan'))
    
    elif answer == "quit" or guess.guessnum == 4:
        cowsay.cow(colored("Better luck next time! ",'green', 'on_cyan'))
        quit()

    else:
        print(colored("Try again!",'green', 'on_cyan'))



