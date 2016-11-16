#Hangman
#Casey Groves
#October 20, 2016
import random
import os

def show_start_screen():
    print ("                      Let's Play...                      ")
    print ("  _  _     ___    _  _     ___   __  __    ___    _  _   ")
    print (" | || |   /   \  | \| |   / __| |  \/  |  /   \  | \| |  ")
    print (" | __ |   | - |  | .` |  | (_ | | |\/| |  | - |  | .` |  ")
    print (" |_||_|   |_|_|  |_|\_|   \___| |_|__|_|  |_|_|  |_|\_|  ")
    print ("_|'''''|_|'''''|_|'''''|_|'''''|_|'''''|_|'''''|_|'''''| ")
    print (""""'-0-0-'"'-0-0-'"'-0-0-'"'-0-0-'"'-0-0-'"'-0-0-'"'-0-0-' """)

def show_end_screen():
    print("By: Classandra Gruves")
    print("Est. 10/20/16")
def get_category(path):
    files = os.listdir(path)

    print("Pick a puzzle pack")

    for i, f in enumerate(files):
        full_path = path + "/" + f

        with open(full_path, 'r') as file:
            print(str(i+1) + ")" + file.readline().strip())

    choice = input("Which shall we play? ")
    choice = int(choice)-1

    return path + "/" + files[choice]

def get_puzzle(file):
    #word = ["Classandra Jewlianne Gruves", "Marsmella", "Owain Bundi", "GG", "Buffalo Boy", "Coop Dogg", "Mini Coop"]

    with open(file, 'r') as f:
        words = f.read().splitlines()
        
    return random.choice(words[1:])

def check(word, solved, guesses):
    for i in range(len(word)):
        if word[i] in guesses or not word[i].isalpha():
            solved = solved[:i] + word[i] + solved[i+1:]
    
    return solved

def get_guess():
    while True:
        guess = input("Guess a letter: ")
        
        if len(guess) == 1 and guess.isalpha():
            guess = guess.lower()
            return guess
        else:
            print("Something's not right. Type in one letter only.")
            
def display_board(solved, guesses, strikes):
    
    if strikes == 0:
        pass
    elif strikes == 1:
        print('''     ____
    |    |
    |    O
    |
    |
 ___|___
|_______|  ''')
              
    elif strikes == 2:
        print('''     ____
    |    |
    |    O
    |    |
    |
 ___|___
|_______|  ''')
    elif strikes == 3:
        print('''     ____
    |    |
    |    O
    |    |
    |   /
 ___|___
|_______|  ''')
    elif strikes == 4:
        print('''     ____
    |    |
    |    O
    |    |
    |   / \
 ___|___
|_______|  ''')
    elif strikes == 5:
        print('''     ____
    |    |
    |    O
    |   -|
    |   / \
 ___|___
|_______|  ''')
    elif strikes == 6:
        print('''     ____
    |    |
    |    O
    |   -|-
    |   / \
 ___|___
|_______|  ''')
    print(solved + " [" + guesses + "]")

def play_again():
    while True:
        answer = input("Wanna play again? ")
        answer = answer.lower()
        if answer == 'no':

            print ("""    ________                __           ____              ____  __            _            
   /_  __/ /_  ____ _____  / /_______   / __/___  _____   / __ \/ /___ ___  __(_)___  ____ _
    / / / __ \/ __ `/ __ \/ //_/ ___/  / /_/ __ \/ ___/  / /_/ / / __ `/ / / / / __ \/ __ `/
   / / / / / / /_/ / / / / ,< (__  )  / __/ /_/ / /     / ____/ / /_/ / /_/ / / / / / /_/ / 
  /_/ /_/ /_/\__,_/_/ /_/_/|_/____/  /_/  \____/_/     /_/   /_/\__,_/\__, /_/_/ /_/\__, /  
                                                                     /____/        /____/   """)
            return False
        elif answer == 'yes':
            return True
        else:
            print("Calm down. Just type yes or no.")
def play():

    puzzle_dir = 'Puzzle Pack'
    category_file = get_category(puzzle_dir)
    word = get_puzzle(category_file)
    solved = "-" * len(word)
    
    guesses = ""
    strikes = 0
    limit = 6
    
    solved = check(word, solved, guesses)
    display_board(solved, guesses, strikes)

    while word != solved and strikes < limit:
        letter = get_guess()

        if letter not in word:
            strikes += 1

        guesses += letter
            
        solved = check(word, solved, guesses)
        display_board(solved, guesses, strikes)

    if word == solved:
        print("Good, Good Job. Good, Good, Good Job. G, Double O, D, J, O, B. Good Job, Good Job, Good Job.")
    elif strikes == limit:
        print("You lose. Nice Try.")

def main():
    show_start_screen()

    playing = True

    while playing == True:
        play()
        playing = play_again()

    show_end_screen()

# code execution begins here
if __name__ == "__main__":
    main()
