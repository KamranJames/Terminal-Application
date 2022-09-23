import cowsay 
from colorama import init
from termcolor import colored
from testmodules import main
from testmodules import guess 
from testmodules import crntlvl

# from testmodules import guesstell
# init()
main()


print("Welcome to the guessing game you have 4 guesses your first riddle is: \n")

while True and guess.guessnum < 4: 
    print("I am cool as a breeze, I stop your heart with ease, seasons may be my enemy, but im part of you and you are friend to me. What am I? \n")
    print("Enter your guess or type 'hint', 'answer' or 'quit' below.")
    answer = input()
    answer = answer.upper()
    guess.guessnum +=1
   #  guesstell()
   #  guess.guesstell +=1
   

    if "SNEEZE" in answer.upper():
       cowsay.cow(colored("Great work, your next riddle is: \n,", 'green', 'on_cyan'))
       guess.guessnum = 0
       crntlvl.level +=1 
       break

    elif answer == "HINT": 
       guess.guessnum -=1
      #  guess.guesstell -=1
       cowsay.cow(colored("Achoo!\n", 'green', 'on_cyan'))

    elif answer == "ANSWER": 
      guess.guessnum -=1 
      cowsay.cow(colored("Sneeze!\n", 'green', 'on_cyan'))
      break
        
    
    elif answer == "QUIT" or guess.guessnum == 4:
           cowsay.cow(colored("Better luck next time! ", 'green', 'on_cyan'))
           quit()

    else:
        print(colored("Try again!",'green', 'on_cyan'))

    while guess.guessnum < 4 and crntlvl.level > 1: 
      print("\n I am fast or I am slow, i'll keep you young and on your toes, your in charge of my tempo. What am I? \n")
    print("Enter your guess or type 'hint', 'answer' or 'quit' below.")
    answer = input()
    answer = answer.upper()
    guess.guessnum +=1
   #  guesstell()
   #  guess.guesstell +=1

    if "RUNNING" in answer:
       cowsay.cow(colored("\n Great work, your next riddle is: \n",'green', 'on_cyan')) 
      #  crntlvl.level +=1 
       break
   
    elif answer == "HINT": 
       guess.guessnum -=1
       cowsay.cow(colored("A way to go places.\n",'green', 'on_cyan'))
   
    elif answer == "ANSWER": 
      cowsay.cow(colored("Running!\n", 'green', 'on_cyan'))
      guess.guessnum -=1
      break
    
    elif answer == "QUIT" or guess.guessnum == 4:
           cowsay.cow(colored("Better luck next time! ",'green', 'on_cyan'))
           quit()

    else:
        print(colored("Try again!",'green', 'on_cyan'))

# while True and guess.guessnum < 4: 
#     print(colored("Pearl white chest without key or lid. Inside of which, a golden treasure is hid. What am I?  \n",'green', 'on_cyan'))
#     print("Enter your guess or type 'hint', 'answer' or 'quit' below.",'green', 'on_cyan')
#     answer = input()
#     answer = answer.upper()
#     guess.guessnum +=1
#    #  guesstell()
#    #  guess.guesstell +=1

#     if "EGG" in answer:
#        cowsay.cow(colored("\n CONGRATULATIONS, YOU ARE THE RIDDLE MASTER",'green', 'on_cyan'))
#        guess.guessnum = 0 
#        break

#     elif answer == "HINT":
#        guess.guessnum -=1
#        cowsay.cow(colored("The creator of this chest is a farm animal\n",'green', 'on_cyan'))

#     elif answer == "ANSWER": 
#       cowsay.cow(colored("Egg!\n", 'green', 'on_cyan'))
#       guess.guessnum -=1
#       break
    
#     elif answer == "QUIT" or guess.guessnum == 4:
#         cowsay.cow(colored("Better luck next time! ",'green', 'on_cyan'))
#         quit()

#     else:
#         print(colored("Try again!",'green', 'on_cyan'))


