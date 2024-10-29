import efx,data,sides
from copy import deepcopy
from time import sleep

man=efx.man

def LoadGame():					#Loads the main game after login is successfull
	man()					#Reloads game chunks
	TPlayer=deepcopy(sides.Player)
	wprog=TPlayer['words']

	while True:
		choice=input(efx.Printer("Choose Difficulty level\n\n"+efx.diffics+"\n\t  [1] CURSED\t\t\t     [2] GHOST\t\t\t         [3] PHANTOM\n\nCHOICE: ",delay=0.0005)); choice.lower()

		if choice in ("cursed","1"):
			difficulty,chances,code="Cursed",10,0
			break

		elif choice in ("ghost","2"):
			difficulty,chances,code="Ghost",8,1
			(man).parts[:2]=["|","|"]
			man(setup=False); break

		elif choice in ("phantom","3"):
			difficulty,chances,code="Phantom",5,2
			break

	efx.Printer("Opening parchment...")
	word=data.LoadWord(difficulty,wprog)

	if word==None:
		efx.Printer(f'Seems like you have mastered the {difficulty.upper()} level!',pdelay=0.5)
		efx.Printer('Returning to menu...')
		Menu()

	efx.Printer("WORD SELECTED!",pdelay=0.5)
	status=GameMechanics(word,chances,difficulty)

	if status=="completed":
		efx.Printer(man.hangman_display,delay=0.0005)
		efx.Printer(f"Word guessed! It was {word.upper()}!\n\n",clear=False,pdelay=1)
		efx.Printer("Whew.. You managed to escape!",clear=False,pdelay=4)

		wprog[code].append(word)
		data.DataAdder(TPlayer,rmv=sides.Player)
		(sides.Player).update(TPlayer)
	else:
		efx.Printer(man.hangman_display,delay=0.0005)
		efx.Printer(f"GAME OVER!\n\nYou failed to guess the word! The word was: {word.upper()}!",clear=False,pdelay=1)
		efx.Printer("\n\nThe hangman got you!",clear=False,pdelay=2)
		efx.Printer("Hanging...")
		efx.ClearScreen(); sleep(5)

	Menu()


def GameMechanics(word,chances,difficulty):				#Handles the game's mechanics,i.e., how it works
	wrd_display=('_ '*len(word)).rstrip()
	guess=''
	while chances:
		if wrd_display.split()==list(word): return "completed"

		efx.Printer(man.hangman_display,delay=0.0005)
		efx.Printer(f"\tWORD STATUS: {wrd_display}\t\t\t[{wrd_display.count('_')} letters more to guess!]",clear=False,delay=0.005)
		guess=input(efx.Printer(f"\n\nYour Guess ({chances} left): ",clear=False)).lower(); guess=guess.strip()

		if guess==word: return "completed"

		elif len(guess)==len(word) and guess!=word:
			efx.Printer("Incorrect guess!",pdelay=0.5)
			man_dsply(difficulty)
			chances-=1
			continue

		if ""==guess or len(guess)>1:
			efx.Printer("Your guess must contain the whole word or just one letter!",pdelay=0.5)
			efx.Printer("The hangman is watching and there's no escape!",pdelay=0.3)
			continue

		if guess in word:
			efx.Printer("Letter exists!",pdelay=0.5)

			if word.count(guess)==wrd_display.count(guess):
				efx.Printer(f"No more {guess.upper()}'s in the word!",pdelay=0.5)
				continue

			wrd_display=word_dsply(guess,word,wrd_display,difficulty)

		else:
			efx.Printer("Incorect guess!",pdelay=0.5)
			man_dsply(difficulty)
			chances-=1


def word_dsply(guess,word,display,difficulty):				#Changes word display at each correct guess
	for pos,letter in enumerate(word):
		if letter==guess and display[2*pos]=='_':
			display=display[:(2*pos)]+guess+display[(2*pos)+1:]
		if word.count(guess)==display.count(guess): break

	return display


def man_dsply(difficulty):				#Updates hangman display at each incorrect guess
	Nparts=["|","|","_","O","_","/","|","\\","/","\\"]
	pace=1

	if difficulty=='Phantom': pace=2

	status=man.parts.index("")
	man.parts[status:status+pace]=Nparts[status:status+pace]
	man(setup=False)


def Menu():				#Includes the dynamic game menu
	while True:
                        choice=input(efx.Printer(efx.menu%(sides.Player['userid']),delay=0.0005)); choice=(choice.lower()).strip()

                        if choice in ("play game",'1'):
                                efx.Printer("Loading....")
                                LoadGame()

                        elif choice in ("game help",'2'):
                                input(efx.Printer(efx.help,delay=0.0005))

                        elif choice in ("view profile",'3'):
                                sides.Profile()

                        elif choice in ("leaderboard",'4'):
                                sides.Leaderboard()

                        elif choice in ("exit",'5'):
                                choice=efx.Exit()
                                if choice==False: Menu()
