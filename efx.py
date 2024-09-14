import time
from sys import exit

lore="""
In the late 1900s, a secluded village was haunted by a sinister figure known by the villagers as the Hangman.\nThe legend told of a dark,cursed parchment that appeared in the hands of those who crossed the Hangman’s path.\nThe parchment bore a hidden word that must be guessed to escape.

For each incorrect guess, a spectral figure of the Hangman would draw closer to completion—a noose tightening\naround a ghostly neck. The cursed villagers who failed to guess the word were seized by the Hangman, their\nsouls trapped within the parchment’s dark embrace.

Though the Hangman disappeared centuries ago, whispers of his curse persist. Those who find the cursed \nparchment or hear the chilling challenge are said to risk becoming the Hangman’s next victims, forever bound to\nthe terror of his eternal game.

**This game has been adapted from this lore."""

diffics_display="""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣧⠀⢀                                                                  ⡠⠄⠀⠀⠄⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⠃⠻⣧⠈⣦                                                                ⠊⢀⣤⣞⣔⢤⡈⠆
⠀⠀⠀⠀⠀⠀⠀⠤⠴⠶⠿⢿⣿⡿⠁⠀⠀⠈⠆⠘⣷⡄                                                            ⠄⢠⣿⣧⣿⣿⣟⠇⠈⠢⡀
⠀⠀⣤⣤⣤⣤⣤⣤⠤⠆⠂⣸⠟⠀⢀⣐⠒⠶⢶⣤⣽⣿⣦⣤⣤⣤⣀⣀⣀⠀			 ⣀⣀                               ⠌⠀⣿⠿⠿⠿⠿⣿⡀⢰⠒⠊
⠀⠀⠈⠛⢿⣿⣷⡄⠀⠀⢠⠋⢠⣾⡟⠻⣷⣄⠀⠀⠈⠉⠛⠻⢿⣿⡿⠋                   ⠰⣿⣿⣿⣿⠆                            ⠌⢀⡾⠁⠀⠀⠀⠀⡈⣇⠀⢆
⠀⠀⠀⠀⠀⠙⢻⣿⣦⠀⠁⢠⣿⣿⠁⠀⣿⣿⣆⠀⣇⠀⠀⣴⠟⠁                  ⢀⣀⣠⣇⣙⣻⣟⣋⣸⣄⣀⣀                      ⣀⠄⠃⠘⠇⠀⠈⠀⠀⠉⠀⣸⠆⡈⠢⢀
⠀⠀⠀⠀⠀⠀⢸⣿⠹⣷⡄⠸⣿⣿⡄⠀⣿⣿⠏⠀⣿⡀⠊⢀⡴⠃                  ⠙⠟⣿⣿⠋⠋⠙⠙⣿⣿⠻⠋                     ⠸⡀⢰⣎⠀⠀⠀⠀⠀⢀⡴⠎⠁⠀⢐⠄⠀⡕
⠀⠀⠀⠀⠀⠀⢸⡇⢰⠀⠙⢆⠈⠻⢷⡴⠟⠋⠀⠀⣿⣷⣾⠟                    ⣠⣴⢿⣿⠺⣶⣷⠗⣿⡿⣧⣄                       ⠑⠀⠪⡢⡀⠀⠀⠀⠈⠀⣀⢀⡴⠅⠀⠈
⠀⠀⠀⠀⠀⠀⠸⠀⣸⠀⠀⠀⢀⣀⣠⣤⠶⠊⠁⠀⢹⣿⡃                          ⠈⠁                              ⢄⠑⠯⢞⣪⡀⣴⣾⡗⠋⠀⡀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⣴⣶⣿⣿⣿⣭⡀⠂⢤⣄⣀⢸⣿⣇                                                           ⠑⠂⠄⡈⠙⠈⢁⡠⠔⠂
⠀⠀⠀⠀⠀⠀⠀⣼⣿⠿⠛⠉⠀⠉⠙⠛⠲⠤⠈⠙⠿⣿⣿⡄                                                              ⠈⠀⠐⠁
⠀⠀⠀⠀⠀⠀⠰⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧"""



def ClearScreen():				#Calling this will clear the terminal window (won't work in Python's' IDLE)
	print("\033[H\033[J")  


def Printer(text,repetitions=1,clear=True,delay=0.05):					#Deals with dynamic typing effect
	dot="..." in text

	if clear: ClearScreen()

	for i in range(repetitions):
		for j in text:
			time.sleep(0.9 if dot and j=='.' else delay)
			print(j,end='',flush=True)
		time.sleep(0.05)

	return ''


def Exit(opt=False):				#Custom exit function
	if opt:
		while True:
			choice=input(Printer("Are you sure you want to exit?(Y/N) ")).upper()
			if choice=='Y':
				Printer("Exiting...")
				exit()
			elif choice=='N':
				Printer("Exit request terminated!")
				return False
	else:
		Printer("Exitting...")
		ClearScreen()
		exit()