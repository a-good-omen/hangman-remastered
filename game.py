import efx,data,time

parts=["","","","","","","","","",""]
hangman_display=f"""
		                ______________
 				|             {parts[0]}					𓁹  𓁹
H				|             {parts[1]}
A				|            {parts[2]} {parts[3]} {parts[4]}
N				|           {parts[5]} {parts[6]} {parts[7]}
G				|            {parts[8]} {parts[9]}
M				|
A				|
N				|
 				|
		 	  ______|______
			 /_____________\\ """


def LoadGame():					#Loads the main game after login is successfull
	while True:
		efx.Printer("Choose Difficulty level\n\n",delay=0.01)
		efx.Printer(efx.diffics_display,delay=0.000005,clear=False)
		efx.Printer("\n\t  [1] Cursed\t\t\t      [2] Ghost\t\t\t         [3] Phantom",delay=0.005,clear=False)
		choice=input(efx.Printer("\n\nCHOICE: ",clear=False)); choice.lower()
		if choice in ("cursed","1"): diffic="Cursed"; chances=10; break
		elif choice in ("ghost","2"): diffic="Ghost"; chances=8;break
		elif choice in ("phantom","3"): diffic="Phantom";chances=5; break

	efx.Printer("Opening parchment...")
	efx.Printer("WORD SELECTED!"); time.sleep(0.5)
	word="gamehub"
	status=GameMechanics(word,chances,diffic)

	if status=="completed":
		efx.Printer(f"Word guessed! It was {word.upper()}"); time.sleep(0.1)
		efx.Printer("You managed to escape!")
	else:
		efx.Printer("GAME OVER!"); time.sleep(0.1)
		efx.Printer(f"You failed to guess the word! The word was: {word.upper()}!"); time.sleep(0.5)
		efx.Printer("Hanging..."); efx.ClearScreen(); time.sleep(2)
	Menu()


def GameMechanics(word,chances,difficulty):
	wrd_display=('_ '*len(word)).rstrip()

	while chances:
		efx.ClearScreen(); time.sleep(0.1)
		efx.Printer(hangman_display,delay=0.0005 )
		efx.Printer(f"\n\n\tWORD STATUS: {wrd_display}",clear=False,delay=0.005)
		guess=input(efx.Printer(f"\n\nYour Guess ({chances} left): ",clear=False)).lower(); guess=guess.strip()

		if guess==word or wrd_display.split()==list(word): return "completed"

		if ""==guess or len(guess)>1:
			efx.Printer("Your guess must contain the whole word or just one letter!"); time.sleep(0.5)
			efx.Printer("The hangman is watching and there's no escape!"); time.sleep(0.1)
			continue

		if guess in word:
			efx.Printer("Letter exists!"); time.sleep(0.5)
			wrd_display=update_display(guess,word,wrd_display)

		else:
			efx.Printer("Incorect guess!")
			setup_man(parts,difficulty)
			chances-=1


def update_display(guess,word,display):
	for pos,letter in enumerate(word):
		if letter==guess and display[2*pos]=='_':
			display=display[:(2*pos)]+guess+display[(2*pos)+1:]
			break

	return display


def setup_man(Oparts,diffic):
	parts=["|","|","_","O","_","/","|","\\","/","\\"]
	if diffic=='phantom': pace=2


def Menu():
	from sides import Player
	while True:
                        choice=input(efx.Printer(
f"""                .___  ___.  _______ .__   __.  __    __
                |   \/   | |   ____||  \ |  | |  |  |  |                                  ■ USER: {Player} ■
                |  \  /  | |  |__   |   \|  | |  |  |  |
                |  |\/|  | |   __|  |  . `  | |  |  |  |
                |  |  |  | |  |____ |  |\   | |  `--'  |
                |__|  |__| |_______||__| \__|  \______/\n\n
                [1] Play Game                      _________
                                                           |
		[2] Game Help                              0
                                                          /|\\
                [3] View Profile                          / \\
                                                 ______________
                [4] Leaderboard

                [5] Exit

                CHOICE: """,delay=0.0005));choice=choice.lower()
                        if choice in ("play game",'1'):
                                efx.Printer("Loading....")
                                LoadGame()
                        elif choice in ("game help",'2'):
                                ...
                        elif choice in ("view profile",'3'):
                                ...
                        elif choice in ("leaderboard",'4'):
                                ...
                        elif choice in ("exit",'5'):
                                choice=efx.Exit(opt='menu')
                                if choice==False: Menu()
