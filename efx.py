import os
from time import sleep
from sys import exit

lore="""
In the late 1900s, a secluded village was haunted by a sinister figure known by the villagers as the Hangman.\nThe legend told of a dark,cursed parchment that appeared in the hands of those who crossed the Hangman’s path.\nThe parchment bore a hidden word that must be guessed to escape.

For each incorrect guess, a spectral figure of the Hangman would draw closer to completion—a noose tightening\naround a ghostly neck. The cursed villagers who failed to guess the word were seized by the Hangman, their\nsouls trapped within the parchment’s dark embrace.

Though the Hangman disappeared centuries ago, whispers of his curse persist. Those who find the cursed \nparchment or hear the chilling challenge are said to risk becoming the Hangman’s next victims, forever bound to\nthe terror of his eternal game.

**ADAPTED"""


diffics_display="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣷⡀
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


help=r""" 			 ____  ____  ________  _____     _______
	                |_   ||   _||_   __  ||_   _|   |_   __ \
	                  | |__| |    | |_ \_|  | |       | |__) |
			  |  __  |    |  _| _   | |   _   |  ___/
			 _| |  | |_  _| |__/ | _| |__/ | _| |_
			|____||____||________||________||_____|


Disclaimer: This game is VERY HARD!

Welcome to the HANGMAN game — an exciting classic word guessing game! If you've played the previously published version;
this is just a remastered version of it! Your skills will be tested as you navigate through THREE thrilling levels of difficulty.

                     ┌──────────────────────────────────────┐
                     │            Game Overview             │
                     └──────────────────────────────────────┘

You will guess a word chosen from one of three difficulty levels.
The higher the difficulty, the fewer chances you have to win (obvious, right?).

                     ┌──────────────────────────────────────┐
                     │           Difficulty Levels          │
                     └──────────────────────────────────────┘

[1] CURSED
   - Chances: 10
   - Description: The easiest level! You'll encounter shorter and simpler words. Makes the game EASIER for beginners!

[2] GHOST
   - Chances: 8
   - Description: A moderate challenge. The words here are longer and slightly trickier than those in the Cursed level.

[3] PHANTOM
   - Chances: 5
   - Description: The ultimate test! This highest difficulty level features the longest and most challenging words.

                     ┌──────────────────────────────────────┐
                     │             Key Features             │
                     └──────────────────────────────────────┘

- Unique Words: No word is repeated across different difficulty levels, so don’t hope to find a word you’ve already guessed in easier modes.

- Profile Tracking: You’ll be able to check how many words you’ve guessed from each difficulty level in your profile!

- Local Data Storage: All your game data is stored locally, so you can’t continue playing on another device.

- Local Leaderboard: Multiple users play on the SAME device? Check where you stand when compared to them in the leaderboard! (Players
   must be on the same device!)


↲ Press ENTER to continue!"""


def ClearScreen():				#Calling this will clear the terminal window (won't work in Python's' IDLE)
	if os.name=='nt': os.system('cls')
	else: os.system('clear')


def Printer(text,clear=True,delay=0.05):					#Deals with dynamic typing effect
	dot="..." in text

	if clear: ClearScreen()

	for j in text:
		sleep(0.9 if dot and j=='.' else delay)
		print(j,end='',flush=True)
	sleep(0.05)

	return ''


def Exit(opt=False):				#Custom exit function
	while True:
		choice=input(Printer("Are you sure you want to exit?(Y/N) ")).upper()
		if choice=='Y':
			Printer("Exiting..."); ClearScreen()
			exit()
		elif choice=='N':
			Printer("Exit request terminated!"); sleep(0.5)
			return False
