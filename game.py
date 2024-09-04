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
		efx.Printer("\n\t     [1] Cursed\t\t\t           [2] Ghost\t\t\t    [3] Phantom",delay=0.005,clear=False)
		choice=input(efx.Printer("\n\nCHOICE: ",clear=False)); choice.lower()
		if choice in ("cursed","1"): diffic="Cursed"; chances=10; break
		elif choice in ("ghost","2"): diffic="Ghost"; chances=8;break
		elif choice in ("phantom","3"): diffic="Phantom";chances=6; break

	efx.Printer("Opening parchment...")
	efx.Printer("REMEMBER: Lose, and its the end. The hangman shows no mercy and there's no escape!"); time.sleep(0.5)
	word="hello"
	status=GameMechanics(word,chances)
	if status=="completed":
		efx.Printer("Word guessed!")
		efx.Printer("Hangman is withdrawing...")
	else:
		efx.Printer("You failed to guess the word!")
		efx.Printer("Hanging...")
	efx.Menu()

def GameMechanics(word,chances):
	wrd_display=('_ '*len(word)).rstrip()
	
	while chances:
		efx.ClearScreen(); time.sleep(0.1)
		efx.Printer(hangman_display,delay=0.0005 )
		efx.Printer(f"\n\n\tWORD STATUS: {wrd_display}",clear=False,delay=0.005)
		guess=input(efx.Printer(f"\n\nYour Guess ({chances} left): ",clear=False)).lower(); guess=guess.strip()
		if guess==word: return "completed"
		if ""==guess or len(guess)>1:
			efx.Printer("Your guess must contain the whole word or just one letter!")
			efx.Printer("The hangman is watching and there's no escape!"); time.sleep(0.5)
			continue
		if guess in word:
			...
		else:
			efx.Printer("Incorect guess!")
			#update_man()
			chances-=1