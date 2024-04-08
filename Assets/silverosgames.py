from termcolor import colored
from colorama import init
import random
import os

def clear():
    os.system('cls')


"""
WORDLE
By: MilesWK and Grey41

NOTE:

You may NOT use the code contained in the wordlegame() function without explicit
permission from the developers.
"""
    
def wordlegame():
    #Define Variables here:
    #For the chosen word. 
    first = "" 
    second = ""
    third = ""
    forth = ""
    fifth = ""
    #For the input
    first1 = "" 
    second1 = ""
    third1 = ""
    forth1 = ""
    fifth1 = ""
    #For their 6 guesses:
    guesses = 0
    UserInput1 = "------"
    length = 0
    letters = []
    removed_letters = []
    #Start of program:
    init(autoreset=True)
    words = []
    words_text = open("Words.txt", "r")
    for line in words_text:
      words.append(line.strip())
    word = random.choice(words)
    while guesses != 6 and UserInput1 != word: 
      #Puts the letters into variables
      #For the computer word:
      first = word[0]
      second = word[1]
      third = word[2]
      forth = word[3]
      fifth = word[4]
      guessed = []
      clear()
      print("Welcome to Wordle! by MilesWK and Grey41. The aim of the game is to guess the five letter word in six guesses. \n\nThe Yellow letters mean the right letter in the wrong place, green is right letter in right place, and white is not in the word at all.")
      print("To start playing, enter a five letter word.")
      while length != 5 or UserInput1 not in words:
        UserInput1 = str(0)
        UserInput1 = input()
        UserInput1 = UserInput1.lower()
        if len(UserInput1) != 5:
          print(colored("Word isn't 5 letters long","red"))
        elif UserInput1 not in words:
          print(colored("Word not in word list.","red"))
        else:
          guesses = guesses + 1
          clear()
          first1 = UserInput1[0]
          second1 = UserInput1[1]
          third1 = UserInput1[2]
          forth1 = UserInput1[3]
          fifth1 = UserInput1[4]

          #This script will give them the official letters. 

          if first1 == first:
            first1 = colored(first1, "green")
          elif first1 in (second, third, forth, fifth):
            first1 = colored(first1, "yellow")
          else:
            first1 = first1
            if first1 not in removed_letters:
              removed_letters.append(first1)

          if second1 == second:
            second1 = colored(second1, "green")
          elif second1 in (first, third, forth, fifth):
            second1 = colored(second1, "yellow")
          else:
            second1 = second1
            if second1 not in removed_letters:
              removed_letters.append(second1)

          if third1 == third:
            third1 = colored(third1, "green")
          elif third1 in (first, second, forth, fifth):
            third1 = colored(third1, "yellow")
          else:
            third1 = third1
            if third1 not in removed_letters:
              removed_letters.append(third1)

          if forth1 == forth:
            forth1 = colored(forth1, "green")
          elif forth1 in (first, second, third, fifth):
            forth1 = colored(forth1, "yellow")
          else:
            forth1 = forth1
            if forth1 not in removed_letters:
              removed_letters.append(forth1)

          if fifth1 == fifth:
            fifth1 = colored(fifth1, "green")
          elif fifth1 in (first, second, third, forth):
            fifth1 = colored(fifth1, "yellow")
          else:
            fifth1 = fifth1
            if fifth1 not in removed_letters:
              removed_letters.append(fifth1)

          print("  ")
          guessed.append(first1 + second1 + third1 + forth1 + fifth1)
          for item in guessed:
            print(item)
          if guesses == 6 and UserInput1 != word:
            print('  ')
            print("Oh no! You ran out of guesses! Game Over!")
            print("The word you were trying to guess was " + str(word) + ".")
            break
          DisplayLetters = ""
          letters_text = open("letters.txt", "r")
          letters = []
          for line in letters_text:
            letters.append(line.strip())
            
          for item in removed_letters:
            letters.remove(item)
            
          for line in letters:
            DisplayLetters = DisplayLetters + line + " "
            
          print("  ")
          print("  ")
          print(colored("Letters still available: ","green") + DisplayLetters)
          print("  ")
          if UserInput1 == word:
            print("  ")
            print("  ")
            print(colored("Congrats! You have found the correct word! ","green") + "You got it in " + colored(str(guesses),"cyan") + " guesses!")
            print("  ")
            break
