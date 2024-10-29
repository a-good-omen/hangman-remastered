import os,sys
from time import sleep
from sys import exit

intro="""
                       _   _    _    _   _  ____ __  __    _    _   _
                      | | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
                      | |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
                      |  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
                      |_| |_/_/   \_|_| \_|\____|_|  |_/_/   \_|_| \_|

                        ----------Created By a-good-omen----------
\n\n\t\t\t\t  ↲ Press ENTER to start"""

lore="In the late 1900s, a secluded village was haunted by a sinister figure known by the villagers as the Hangman.\nThe legend told of a dark,cursed parchment that appeared in the hands of those who crossed the Hangman’s path.\nThe parchment bore a hidden word that must be guessed to escape.\n\nFor each incorrect guess, a spectral figure of the Hangman would draw closer to completion—a noose tightening\naround a ghostly neck. The cursed villagers who failed to guess the word were seized by the Hangman, their\nsouls trapped within the parchment’s dark embrace.\n\nThough the Hangman disappeared centuries ago, whispers of his curse persist. Those who find the cursed \nparchment or hear the chilling challenge are said to risk becoming the Hangman’s next victims, forever bound to\nthe terror of his eternal game.\n\n**ADAPTED"

diffics="""
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

menu="""
            .___  ___.  _______ .__   __.  __    __
            |   \\/   | |   ____||  \\ |  | |  |  |  |                                  ■ USER: %s ■
            |  \\  /  | |  |__   |   \\|  | |  |  |  |
            |  |\\/|  | |   __|  |  . `  | |  |  |  |
            |  |  |  | |  |____ |  |\\   | |  `--'  |
            |__|  |__| |_______||__| \\__|  \\______/\n\n
                [1] Play Game                      _________
                                                           |
                [2] Game Help                              0
                                                          /|\\
                [3] Profile                               / \\
                                                 ______________
                [4] Leaderboard

                [5] Exit\n\n\n

            CHOICE: """

help="""
\t\t\t    .  . __ .   .___.
\t\t\t    |  ||   |   |   |
\t\t\t    |__||_  |   |___|
\t\t\t    |  ||   |   |
\t\t\t    |  ||__ |__.|

\t\t     WELCOME TO HANGMAN-REMASTERED!
      A classic word guessing game, remastered with the best gameplay!
\t Originally published at https://github.com/a-good-omen/.

──────────────────────────────────────────────────────────────────────────

                           - OVERVIEW -

   A word will be given with all its letters concealed. Each correct guess
   reveals a letter, while each incorrect guess brings you closer to being..
   HANGED!

       - No hints are provided at any difficulty level.
       - You may guess a single letter or the entire word.
       - Each incorrect guess (letter or word) reduces your chances by 1.
       - Guessing the full word correctly will end the game immediately.
       - Guesses that are more than one letter long and don’t match the
	 word’s length are ignored and will not penalize your chances.

   NOTE: The number of chances indicates the remaining incorrect guesses
   you can make, not the number of attempts to guess the word.

──────────────────────────────────────────────────────────────────────────

                           - GAME DETAILS -

  The game has three difficulty levels, each offering a unique challenge.

    CURSED
    Chances - 10
    The easiest level. Words are the shortest in the game.

    GHOST
    Chances - 8
    The medium level. Words are slightly longer than CURSED.

    PHANTOM
    Chances - 5
    The hardest level, with the longest words.

──────────────────────────────────────────────────────────────────────────

                          - MORE INFORMATION -

   Players can check and edit their profile via the PROFILE option
   in the menu.

   LEADERBOARD ranks the top 5 players based on the number of words guessed,
   with priority given to words guessed at higher difficulty levels. If
   players are tied, they are ranked alphabetically.

   NOTE: The leaderboard WORKS ONLY IF more than 1 player is using the same
   device and the top 5 players have guessed atleast 1 word.

──────────────────────────────────────────────────────────────────────────\n\n↲ ENTER to continue"""

Lboard='''
\t  _      ______          _____  ______ _____  ____   ____          _____  _____
\t | |    |  ____|   /\\   |  __ \\|  ____|  __ \\|  _ \\ / __ \\   /\\   |  __ \\|  __ \\
\t | |    | |__     /  \\  | |  | | |__  | |__) | |_) | |  | | /  \\  | |__) | |  | |
\t | |    |  __|   / /\\ \\ | |  | |  __| |  _  /|  _ <| |  | |/ /\\ \\ |  _  /| |  | |
\t | |____| |____ / ____ \\| |__| | |____| | \\ \\| |_) | |__| / ____ \\| | \\ \\| |__| |
\t |______|______/_/    \\_\\_____/|______|_|  \\_\\____/ \\____/_/    \\_\\_|  \\_\\_____/
\n\t     RANK                         USERID                    TOTAL PROGRESS\n'''


def ClearScreen():				#Calling this will clear the terminal window (won't work in Python's' IDLE)
	if os.name=='nt': os.system('cls')
	else: os.system('clear')


def Printer(text,clear=True,delay=0.02,pdelay=None):					#Deals with dynamic typing effect
	dot="..." in text
	if clear: ClearScreen()

	for letter in text:
		sleep(0.9 if dot and letter=='.' else delay)
		print(letter,end='',flush=True)

	if pdelay!=None: sleep(pdelay)

	return ''


def Exit():				#Custom exit function
	while True:
		choice=input(Printer("Are you sure you want to exit?(Y/N) "))

		if choice in 'yY':
			Printer("Exiting..."); ClearScreen()
			exit()

		elif choice in 'nN':
			Printer("Exit request terminated!",pdelay=0.5)
			return False


def man(setup=True):                            #Function allows reloading chunks later in the game
        if setup: man.parts=['']*10

        man.hangman_display=f"""
                                 ______________
                                |             {man.parts[0]}
H                               |             {man.parts[1]}
A                               |            {man.parts[2]}{man.parts[3]}{man.parts[4]}
N                               |           {man.parts[5]} {man.parts[6]} {man.parts[7]}
G                               |            {man.parts[8]} {man.parts[9]}
M                               |
A                               |
N                               |
                                |
                          ______|______
                         /_____________\\ \n\n"""
