import efx,data,sides
from copy import deepcopy
from time import sleep

def man(setup=True):				#Function allows recalling later during GameMechanics
	if setup: man.parts=["","","","","","","","","",""]
	man.hangman_display=\
f"""		                ______________
 				|             {man.parts[0]}					𓁹 O 𓁹
H				|             {man.parts[1]}
A				|            {man.parts[2]}{man.parts[3]}{man.parts[4]}
N				|           {man.parts[5]} {man.parts[6]} {man.parts[7]}
G				|            {man.parts[8]} {man.parts[9]}
M				|
A				|
N				|
 				|
		 	  ______|______
			 /_____________\\ \n\n"""


def LoadGame():					#Loads the main game after login is successfull
	man()					#Reloads game chunks
	TPlayer=deepcopy(sides.Player)
	prog=TPlayer['data'];wprog=TPlayer['words']
	while True:
		efx.Printer("Choose Difficulty level\n\n",delay=0.01)
		efx.Printer(efx.diffics_display,delay=0.000005,clear=False)
		efx.Printer("\n\t  [1] CURSED\t\t\t     [2] GHOST\t\t\t         [3] PHANTOM",delay=0.005,clear=False)
		choice=input(efx.Printer("\n\nCHOICE: ",clear=False)); choice.lower()
		if choice in ("cursed","1"): difficulty="Cursed"; chances,code=10,0; break
		elif choice in ("ghost","2"): difficulty="Ghost"; chances,code=8,1; man.parts[:2]=["|","|"]; man(setup=False); break
		elif choice in ("phantom","3"): difficulty="Phantom";chances,code=5,2; break

	efx.Printer("Opening parchment...")
	efx.Printer("WORD SELECTED!",pdelay=0.5)
	word=data.LoadWord(difficulty,wprog)
	status=GameMechanics(word,chances,difficulty)

	if status=="completed":
		efx.Printer(man.hangman_display,delay=0.005)
		efx.Printer(f"Word guessed! It was {word.upper()}!\n\n",clear=False,pdelay=0.5)

		prog[code]+=1; wprog.append(word)
		data.DataAdder(TPlayer,rmv=sides.Player)

		efx.Printer("Whew.. You managed to escape!",clear=False,pdelay=4)
		(sides.Player).update(TPlayer)
	else:
		efx.Printer(man.hangman_display,delay=0.005)
		efx.Printer("GAME OVER!\n\n",clear=False)
		efx.Printer(f"You failed to guess the word! The word was: {word.upper()}!",clear=False,pdelay=5)
		efx.Printer("The hangman got you!",pdelay=0.5)
		efx.Printer("Hanging..."); efx.ClearScreen(); sleep(5)
	Menu()


def GameMechanics(word,chances,difficulty):				#Handles the game's mechanics,i.e. how it works
	wrd_display=('_ '*len(word)).rstrip()
	guess=''
	while chances:

		if wrd_display.split()==list(word): return "completed"

		efx.Printer(man.hangman_display,delay=0.0005 )
		efx.Printer(f"\tWORD STATUS: {wrd_display}\t\t\t[contains {wrd_display.count('_')} letters more to guess!]",clear=False,delay=0.005)
		guess=input(efx.Printer(f"\n\nYour Guess ({chances} left): ",clear=False)).lower(); guess=guess.strip()

		if guess==word: return "completed"
		elif len(guess)==len(word) and guess!=word:
			efx.Printer("Incorrect guess!",pdelay=0.5)
			setup_man(difficulty)
			chances-=1
			continue

		if ""==guess or len(guess)>1:
			efx.Printer("Your guess must contain the whole word or just one letter!",pdelay=0.5)
			efx.Printer("The hangman is watching and there's no escape!",pdelay=0.3)
			continue

		if guess in word:
			efx.Printer("Letter exists in the word!",pdelay=0.5)

			if word.count(guess)==wrd_display.count(guess):
				efx.Printer(f"No more {guess.upper()}'s in the word!",pdelay=0.5)
				continue

			wrd_display=update_display(guess,word,wrd_display,difficulty)

		else:
			efx.Printer("Incorect guess!")
			setup_man(difficulty)
			chances-=1


def update_display(guess,word,display,difficulty):				#Changes word display at each correct guess
	for pos,letter in enumerate(word):
		if letter==guess and display[2*pos]=='_':
			display=display[:(2*pos)]+guess+display[(2*pos)+1:]
		if word.count(guess)==display.count(guess): break

	return display


def setup_man(difficulty):				#Updates hangman display at each incorrect guess
	Nparts=["|","|","_","O","_","/","|","\\","/","\\"]
	pace=1

	if difficulty=='Phantom': pace=2

	status=man.parts.index("")
	man.parts[status:status+pace]=Nparts[status:status+pace]
	man(setup=False)


def Menu():				#Includes the dynamic game menu
	while True:
                        choice=input(efx.Printer(
f"""            .___  ___.  _______ .__   __.  __    __
            |   \\/   | |   ____||  \\ |  | |  |  |  |                                  ■ USER: {sides.Player['userid']} ■
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

                [5] Exit

            CHOICE: """,delay=0.0005));choice=(choice.lower()).strip()
                        if choice in ("play game",'1'):
                                efx.Printer("Loading....")
                                LoadGame()

                        elif choice in ("game help",'2'):
                                input(efx.Printer(efx.help,delay=0.0005))

                        elif choice in ("view profile",'3'):
                                sides.Profile()

                        elif choice in ("leaderboard",'4'):
                                ...

                        elif choice in ("exit",'5'):
                                choice=efx.Exit()
                                if choice==False: Menu()
