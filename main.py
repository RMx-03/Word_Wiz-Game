"""
    Word - Wiz
    Rules:  
            guess a 5 letter word
            the game will provide feedback for each input
            correct letter in the correct position - green 
            correct letter but different position - yellow 
            wrong letter - red : added to the list of incorrect letters 
"""
# libraries
import random
from collections import Counter


# Importing the words .txt file line by line into a list
word_path = "words.txt"
word_bank = []
def import_word(word_path):
   
    with open(word_path, "r") as file:
        for line in file:
            word = line.rstrip().lower()
            word_bank.append(word)
    return word_bank


# Selecting the random word from the word bank
def random_word(word_bank):
    guess_word = random.choice(word_bank)    
    return guess_word


# Take user input
MAX_LENGTH = 5
def user_input():
    while True:
        user_guess = input(f"What is your guess?(MAX {MAX_LENGTH} CHARACTERS): ").lower() 
        validate_word = user_guess.isalpha()

        # Checks the validity of input 
        if validate_word and len(user_guess) == MAX_LENGTH:
            return user_guess
        else:
            if not validate_word:
                print("Invalid input! Please enter only letters.")
            if len(user_guess) != MAX_LENGTH:
                print(f"Invalid input! Please enter exactly {MAX_LENGTH} letters.")
        


# Evaluate the guessed word by the user
def evaluate_guess(guess_word, user_guess):
    letter_counter = Counter(guess_word)  # keeps a track of occurence of each letter
    correct_letter_index = []  # to keep track of correct occupied indices   
    response_sys = ['_'] * len(guess_word)  # placeholder for the result - ensures that the result is displayed in correct order 

    # First Phase
    for i in range(len(guess_word)):
        if user_guess[i] == guess_word[i]:  # correct letter correct position
            response_sys[i] = f"\033[92m{user_guess[i]}\033[0m"         
            correct_letter_index.append(i)  # marking the index as used 
            letter_counter[user_guess[i]] -= 1  # reducing the count of a letter that is at the correct position

    #Second Phase    
    for i in range(len(guess_word)):    
        if i not in correct_letter_index:  # skip already matched positions 
            if user_guess[i] in guess_word and letter_counter[user_guess[i]] > 0:  # correct letter wrong position 
                response_sys[i] = f"\033[93m{user_guess[i]}\033[0m"                
                letter_counter[user_guess[i]] -= 1  # again reducing the count to avoid marking again
            else:  # wrong letter 
                response_sys[i] = f"\033[91m{user_guess[i]}\033[0m"               
    
    print(" ".join(response_sys))
    return response_sys


# To restart or exit the game after game is complete
def restart_game():
    while True:
        user_choice = input("Play Again (Y/N): ").lower()
        if user_choice == "y":
            game()  # call the game function again
        elif user_choice == "n":
            print("Thanks for playing! Goodbye!")
            break  # exit/break the loop
        else:  # for invalid inputs - noptify the user
            print("Invalid input: Please enter 'Y' for Yes or 'N' for No!")


# Main game function
def game():    
    MAX_TURNS = 8
    print("Welcome to Word Wiz!\n")
    print(f"The max number of turns: {MAX_TURNS}\n") 
    word_bank = import_word(word_path)   
    guess_word = random_word(word_bank)

    # Main logic for the game
    attemps_left = MAX_TURNS  # using another variable to ensure MAX_TURNS constant dosen't change
    while attemps_left > 0:  # iterates the loop till the time no turns left

        user_guess = user_input()  # calling the user input function         
        
        if user_guess == guess_word:
            print(f"\033[92mCongratulations! You have guessed the word: {guess_word} \033[0m")
            break  # correct answer then break the loop 
        else:
            evaluate_guess(guess_word, user_guess)  # calling the evaluation function 
            attemps_left -= 1        
            print(f"{attemps_left} attempts remaining!\n")
    
    if  attemps_left == 0:  # on exhausting all the available turns the game exits 
            print(f"\033[91mGAME OVER! the word was:{guess_word} \033[0m")

    restart_game()  # calling the restart function after the result is displayed
            

word_wizz = game()