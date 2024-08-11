import time

def ClearScreen():				#Calling this will clear the terminal window (won't work in the IDLE)
        print("\033[H\033[J")
      
          
def Printer(text,delay=0.5,repetitions=1,dots=0,clear=True):					#Major role in program. Deals with dynamic typing effect.
	if clear: ClearScreen() 
	for i in range(repetitions):
		for j in text: print(j,end='',flush=True); time.sleep(delay)
		for k in range(dots):
			time.sleep(0.5)
			print('.',end='',flush=True)
			time.sleep(0.5)
		if dots>0: ClearScreen() 
		time.sleep(0.05)
	return ''
		

def PlayerIntro(user):					#Deals with intro to the game for first time players
	for i in range(3): Printer(f"Welcome {user}!",delay=0.05)
	time.sleep(1)
	input(Printer("""In the late 1900s, a secluded village was haunted by a sinister figure known by the villagers as the Hangman.\nThe legend told of a dark,cursed parchment that appeared in the hands of those who crossed the Hangman’s path.\nThe parchment bore a hidden word that must be guessed to escape.

For each incorrect guess, a spectral figure of the Hangman would draw closer to completion—a noose tightening\naround a ghostly neck. The cursed villagers who failed to guess the word were seized by the Hangman, their\nsouls trapped within the parchment’s dark embrace.

Though the Hangman disappeared centuries ago, whispers of his curse persist. Those who find the cursed \nparchment or hear the chilling challenge are said to risk becoming the Hangman’s next victims, forever bound to\nthe terror of his eternal game.

**This game has been adapted from this lore.""",delay=0.05))


def CreateAccount():					#Deals with account creation
	while True:
		Printer("\t\t\t--------CREATE ACCOUNT--------",delay=0.005)
		PlayerData={}
		PlayerData['name']=input(Printer("\n\nName: ",delay=0.05,clear=False)).title()
		PlayerData['email']=input(Printer("\nEmail: ",delay=0.05,clear=False)).lower()
		PlayerData['userid']=input(Printer("\nCreate display name: ",delay=0.05,clear=False))
		PlayerData['passwd']=input(Printer("\nCreate password: ",delay=0.05,clear=False))
		
		Printer('Checking data format authenticity',dots=4,delay=0.05)
		
		errors="Hmm.. Seems like the data you entered have the following errors:\n\n"
		if '' in PlayerData.values():
			errors+="~ All fields are mandatory! No field can be empty.\n\n"
		if '@' not in PlayerData['email']:
			errors+="~ Email doesn't appear to be authentic.\n\n"
	
		if errors.count('\n')==2:
			Printer("Hmm",delay=0.05,dots=2)
			Printer("Data format valid!",delay=0.05)
			Printer("Account created successfully!",delay=0.05)
			time.sleep(1)
			break
		else:
			Printer(errors+'Try again i guess?',delay=0.05)
			time.sleep(1)
			ClearScreen()

																				
def LoginSetup():					#Deals with login part of main program
	choice=input(Printer('Are you a new player?(Y/N) ',delay=0.05))
	choice=choice.upper(); ClearScreen()
	if choice=="Y":
		Printer("Loading",delay=0.05,dots=4)
		CreateAccount()
		PlayerIntro('new')
		time.sleep(1)
	elif choice=='N':
		pass