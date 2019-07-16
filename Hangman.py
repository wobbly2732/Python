# Owned
__author__ = "Tim Chapman"
__copyright__ = "none"
__credits__ = ""
__license__ = "Apache v2.0"
__version__ = "0.1"
__maintainer__ = "Tim Chapman"
__email__ = "tim.chapman273@gmail.com"
__status__ = "Development"

#importing modules
import time
import os

#Set Global Variables
word = "secret"
word2 = word
turns = 10
guess = ""
guesses2 = ""
failed = 0
name = ""

#Modules
def hangman1():
	print("")
	print("")
	print("")
	print("")
	print("")
	print("_______")
def hangman2():
	print("")
	print("   |")
	print("   |")
	print("   |")
	print("   |")
	print("___|___")
def hangman3():
	print("    ____")
	print("   |")
	print("   |")
	print("   |")
	print("   |")
	print("___|___")
def hangman4():
	print("    ____")
	print("   |    |")
	print("   |")
	print("   |")
	print("   |")
	print("___|___")
def hangman5():
	print("    ____")
	print("   |    |")
	print("   |    O")
	print("   |")
	print("   |")
	print("___|___")
def hangman6():
	print("    ____")
	print("   |    |")
	print("   |    O")
	print("   |    |")
	print("   |")
	print("___|___")
def hangman7():
	print("    ____")
	print("   |    |")
	print("   |    O")
	print("   |  --|")
	print("   |")
	print("___|___")
def hangman8():
	print("    ____")
	print("   |    |")
	print("   |    O")
	print("   |  --|--")
	print("   |")
	print("___|___")
def hangman9():
	print("    ____")
	print("   |    |")
	print("   |    O")
	print("   |  --|--")
	print("   |   /")
	print("___|___")
def hangman10():
	print("    ____")
	print("   |    |")
	print("   |    O")
	print("   |  --|--")
	print("   |   / \ ")
	print("___|___")

#Main
name = input("What is your name? ")
print ("Hello, " + name, "it's time to play Hangman!")
time.sleep(0.5)
print ("Start guessing...")
time.sleep(0.5)


while word != "":

	# ask the user to guess a character
	guess = input("guess a character:")
	guesses = guess
	guesses2 += guess
	if(word.find(guesses) != -1):
		os.system('clear')
		print("letters guessed:", guesses2)
		print ("great guess")
		print ("You have", + turns, 'more guesses' )
		newstr = word.replace(guesses, "")
		word = ""
		guesses = ""
		word = newstr
	else:
		if failed == 10:
			break
		else:
			failed +=1
			turns -=1
			os.system('clear')
			print("letters guessed:", guesses2) 
			print ("You have ", + turns, " remaining")
			hangman = "hangman"
			hangman += str(failed)
			locals()[hangman]()												
																	
if failed == 10:
	print("You lose, better luck next time")
else:						
	print("Congratulations you successfully found the word " + word2)
