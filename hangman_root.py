import random
import os
 
# Funtion to cls the terminal
def cls():
    os.system("cls")
 
# Function to print the hangman
def print_hangman(values):
    print()
    print("\t +--------+")
    print("\t |       | |")
    print("\t {}       | |".format(values[0]))
    print("\t{}{}{}      | |".format(values[1], values[2], values[3]))
    print("\t {}       | |".format(values[4]))
    print("\t{} {}      | |".format(values[5],values[6]))
    print("\t         | |")
    print("  _______________|_|___")
    print("  `````````````````````")
    print()
 
# Function to print the hangman after winning
def print_hangman_win():
    print()
    print("\t +--------+")
    print("\t         | |")
 
    print("\t         | |")
    print("\t O       | |")
    print("\t/|\\      | |")
    print("\t |       | |")
    print("  ______/_\\______|_|___")
    print("  `````````````````````")
    print()
 
# Function to print the word to be guessed
def print_word(values):
    print()
    print("\t", end="")
    for x in values:
        print(x, end="")
    print() 
 
# Function to check for win
def check_win(values):
    for char in values:
        if char == '_':
            return False
    return True    
 
# Function for each hangman game
def hangman_game(word):
 
    cls()
 
    # Stores the letters to be displayed
    word_display = []
 
    # Stores the correct letters in the word
    correct_letters = []
 
    # Stores the incorrect guesses made by the player
    incorrect = []
 
    # Number of chances (incorrect guesses)
    chances = 0
 
    # Stores the hangman's body values
    hangman_values = ['O','/','|','\\','|','/','\\']
 
    # Stores the hangman's body values to be shown to the player
    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
 
    # Loop for creating the display word
    for char in word:
        if char.isalpha():
            word_display.append('_')
            correct_letters.append(char.upper())
        else:
            word_display.append(char)
 
    # Game Loop         
    while True:
 
        # Printing necessary values
        print_hangman(show_hangman_values)
        print_word(word_display)            
        print()
        print("Incorrect characters : ", incorrect)
        print()
 
 
        # Accepting player input
        inp = input("Enter a character = ")
        if len(inp) != 1:
            cls()
            print("Wrong choice! Try Again :(")
            continue
 
        # Checking whether it is a alphabet
        if not inp[0].isalpha():
            cls()
            print("Wrong choice! Try Again :(")
            continue
 
        # Checking if it already tried before   
        if inp.upper() in incorrect:
            cls()
            print("Already tried this! Try another one.")
            continue   
 
        # Incorrect character input 
        if inp.upper() not in correct_letters:
             
            # Adding in the incorrect list
            incorrect.append(inp.upper())
             
            # Updating the hangman display
            show_hangman_values[chances] = hangman_values[chances]
            chances = chances + 1
             
            # Checking if the player lost
            if chances == len(hangman_values):
                print()
                cls()
                print("\tGAME OVER!!!")
                print_hangman(hangman_values)
                print("The word is :", word.upper())
                break
 
        # Correct character input
        else:
 
            # Updating the word display
            for i in range(len(word)):
                if word[i].upper() == inp.upper():
                    word_display[i] = inp.upper()
 
            # Checking if the player won        
            if check_win(word_display):
                cls()
                print("\tCongratulations! ")
                print_hangman_win()
                print("The word was :", word.upper())
                break
        cls() 
     
 
if __name__ == "__main__":
 
    cls()
 
    # Types of categories
    topics = {1: "English Words", 2:"Marvel Characters", 3:"Game Characters"}
 
    # Words in each category
    dataset = {"English Words":["WARLIKE", "JOKER", "IRON PICKAXE", "WATER", "FLASHLIGHT", "SWITZERLAND", "ARCADE MACHINE", "ELEPHANT", "SLEDGEHAMMER"],\
                 "Marvel Characters":["CAPTAIN AMERICA", "IRON MAN", "THANOS", "HAWKEYE", "BLACK PANTHER", "BLACK WIDOW"],
                 "Game Characters":["PHOENIX WRIGHT", "CARL JOHNSON", "TOMMY VERCETTI", "MAX PAYNE", "STEVE"]
                 }
     
    # The GAME LOOP
    while True:
 
        # Printing the game menu
        print()
        print("-----------------------------------------")
        print("\t\tWELCOME TO HANGMAN PYTHON")
        print("-----------------------------------------")
        for key in topics:
            print("Press", key, "to select", topics[key])
        print("Press", len(topics)+1, "to quit")    
        print()
         
        # Handling the player category choice
        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            cls()
            print("Wrong choice! Try again.")
            continue
 
        # Sanity checks for input
        if choice > len(topics)+1:
            cls()
            print("No such topic! Try again.")
            continue   
 
        # The EXIT choice   
        elif choice == len(topics)+1:
            print()
            print("Thank you for playing!")
            break
 
        # The topic chosen
        chosen_topic = topics[choice]
 
        # The word randomly selected
        ran = random.choice(dataset[chosen_topic])
 
        # The overall game function
        hangman_game(ran)