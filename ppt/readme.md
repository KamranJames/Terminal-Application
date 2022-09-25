# Riddle-Riddle
[**Presentation**](https://vimeo.com/manage/videos/753509964/0db9bb4da2/privacy)

[**App Repository**](https://github.com/KamranJames/Terminal-Application.git)

## **Table of Contents** 

  - [**Features**](#features)
  - [**Implementation plan**](#implementation-plan)
  - [**Manual Testing**](#manual-testing)
  - [**Installation instructions**](#installation-instructions)
  - [**Resources**](#resources)


<div id='id-section1'>

## **Features**

The features of Riddle - Riddle are as follows:
* An input that takes the users name and returns it back to them.
* A menu option that provides our users with difficulty options.
* Three game levels which will output a different riddle each level. 
* The ability for our user to make a guess, receive a hint, ask for the answer or quit. This will be repeated throughout the levels as to give our user an option to change difficulty, or to exit our program.

<div id='id-section2'>

## **Implementation plan**

The process of creating our riddle game was constructed on day one, with a brainstorming process. I sent my option to Alex Holder to receive his feedback. I was going to attempt to build a GUI using the terminal, Alex informed me that this wouldn’t fit the brief and in hindsight might have been rather ambitious. I went back to the drawing board and came up with a more simple but fun Riddle game. I wanted to be able to output a relatively basic in concept game, that had some features that would challenge my skills and output a fun and interactive experience for the user.

I created created an 8 day limit with deadlines, throughout. This was accomplished using Trello board, I set different tasks for each day, on day one and would continue to add to my Trello board as the days progressed. This set me a metric as to how I was tracking, what things I was spending too much time on or too little and a sense of achievement for when I had accomplished a task. I would move across completed items to the done list, any blockers I was facing I would have in a seperate tab and any pending questions that I was awaiting an answer for would sit in pending.
 At the end of everyday I would go through and prioritise what was pressing and make adjustments to what could be pushed back.

[Trello Board](https://trello.com/b/mWq9YIXS/terminal-application-riddle-riddle )


<br></br>
<div id='id-section3'>

## Manual Testing
|Feature | Expected Outcome  | Actual Outcome | Remaining issues?   |   |
|---|---|---|---|---|
|Title Art| Ascii art with app title should load to the screen. | Success | Nil  |   |   |
|Option Menu| Interactive option menu should load to screen.| Success | Nil  |   |
|Option Menu Interaction | Difficulty options should be selectable. Each option should give less or more guesses.  | Success  | Nil  |   |
|Quit Option| Choosing Quit in the difficulty menu should exit program. | Success | Nil  |   |   |
|Riddle print| First level riddle should print with a cow offering input option for riddle + 3 options. | Success | Nil  |
|Cowsay | Cowsay cow, should give messages throughout the levels.| Success | Nil  |
|Colorama | Coloured text should appear throughout the levels. | | Nil  |   |
|Hint vs Guesses| Hint option, should not count towards the total number of guesses. | Success | Nil  |
|Answer = Next level | Answer option output riddle answer, then move to next level.| Success | Nil  |
|Incorrect input | Incorrect input or answer should produce “Try Again”.| Success | Nil  |
|Options menu repeat | On each successful guess, user should receive an option to change difficulty or quit. | Success | Nil  |
|Three levels | User should be able to progress through 3 levels if successful. | Success | Nil  |
|Congratulations  | Should receive a congratulations Ascii art if succesful.| Success | Nil  |
<br></br>
<div id='id-section4'>

## Installation instructions
<br></br>


Clone the files from my repository using the following command line instruction:
git clone https://github.com/KamranJames/Terminal-Application.git

From here please navigate to the src folder from where you have cloned the repository, you can also download it as a zip file from my github repository.

Enter your bash terminal enviroment and ensure Python3 is installed as well as pip.
If they are not installed you can access them here:<br></br>
[**Python**](https://www.python.org/downloads/)<br></br>
[**PIP**](https://pip.pypa.io/en/stable/cli/pip_install/)



From your bash terminal enter:

#!bin/bash<br></br>
source .venv/bin/activate<br></br>
pip3 install -r requirements.txt<br></br>
python3 src/main.py

This should activate our interactive game. 
You should now be able to play Riddle - Riddle. 

<div id='id-section5'>

## Resources
* I utilized pep 8 for my style guide.
[PEP - 8](https://peps.python.org/pep-0008/ )

* Ascii Art Generator
  I used an ascii art generator for my ascii rt. 
[F symbols website](https://fsymbols.com/generators/carty/)