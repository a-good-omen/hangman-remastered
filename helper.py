import time,sys

def ClearScreen():				#Calling this will clear the terminal window (won't work in the IDLE)
        print("\033[H\033[J",end="")
        

def Exit(opt=False):				#Custom exit function
	if opt==True:
		while True:
			choice=input(Printer("Are you sure you want to exit?(Y/N) ")).upper()
			if choice=='Y':
				Printer("Exiting",dots=2)
				sys.exit()
			elif choice=='N':
				Printer("Exit request terminated!")
				return False
	else:
		Printer("Exitting",dots=3)
		ClearScreen()
		sys.exit()
		
		
def Printer(text,repetitions=1,dots=0,clear=True,delay=0.05):					#Deals with dynamic typing effect
	if clear: ClearScreen()
	
	for i in range(repetitions):
		for j in text: print(j,end='',flush=True); time.sleep(delay)
		for k in range(dots):
			time.sleep(0.5)
			print('.',end='',flush=True)
			time.sleep(0.5)
		
		time.sleep(0.05)
	return ''


def PlayerIntro():					#Deals with intro to the game for first time players
	Printer("Welcome {user}!")
	time.sleep(0.1)
	Printer("""In the late 1900s, a secluded village was haunted by a sinister figure known by the villagers as the Hangman.\nThe legend told of a dark,cursed parchment that appeared in the hands of those who crossed the Hangman’s path.\nThe parchment bore a hidden word that must be guessed to escape.

For each incorrect guess, a spectral figure of the Hangman would draw closer to completion—a noose tightening\naround a ghostly neck. The cursed villagers who failed to guess the word were seized by the Hangman, their\nsouls trapped within the parchment’s dark embrace.

Though the Hangman disappeared centuries ago, whispers of his curse persist. Those who find the cursed \nparchment or hear the chilling challenge are said to risk becoming the Hangman’s next victims, forever bound to\nthe terror of his eternal game.

**This game has been adapted from this lore.""")
	time.sleep(1)


def CreateAccount():					#Deals with account creation
	import data
	while True:
		Printer("""
\t\t/ ` _ _  _ _|_ _    _  _ _ _     _ _|_
\t\t\_,| (/_(_| | (/_  (_|(_(_(_)|_|| | |""",delay=0.004)
		PlayerData={}
		PlayerData['name']=input(Printer("\n\nName: ",clear=False)).title()
		PlayerData['email']=input(Printer("\nEmail: ",clear=False)).lower()
		PlayerData['userid']=input(Printer("\nCreate display name: ",clear=False))
		PlayerData['passwd']=input(Printer("\nCreate password: ",clear=False))

		if '' in PlayerData.values():
			Printer("All fields are mandatory!"); time.sleep(0.5); continue
		
		Printer("Checking data format authenticity",dots=3)
		errors="Seems like the data you entered have the following errors:\n\n"
		if len(PlayerData["name"])<4:
			errors+="~ The name entered doesnt appear to be authentic.\n\n"
		if '@gmail.com' not in PlayerData['email']:
			errors+="~ Email doesn't appear to be authentic.\n\n"
		if len(PlayerData["userid"])<4:
			errors+="Display name must be atleast 4 characters long!\n\n"
		if len(PlayerData["passwd"])<8:
			errors+="Password too weak. Must be atleast 8 characters long!"

		if errors.count('\n')==2:
			Printer("Data format valid!")
			Printer("Checking for duplication with existing records",dots=4)
			if data.Verifier(PlayerData["userid"])==True:
				Printer("User with display name already exists! Try using a different display name!"); time.sleep(0.5); continue
			data.DataAdder(PlayerData)
			Printer("Account created successfully!")
			time.sleep(1)
			break
		else:
			Printer(errors+'Try again i guess?')
			time.sleep(2)


def ExistingLogin(times=0):				#Deals with login for existing players
	import data
	while True:
		Printer("""
\t\t|  _  _ . _
\t\t|_(_)(_||| |
\t\t      _|""",delay=0.004)
		userid=input(Printer("\n\nEnter display name: ",clear=False))
		passwd=input(Printer("\nEnter password: ",clear=False))
		if ''==userid or ''==passwd: Printer("All fields are mandatory!"); time.sleep(1); continue
		
		Printer("Checking datbase for matching records",dots=3)

		if data.Verifier(userid)==True:
			if data.Verifier(userid,passwd)==False:
				Printer("Password appears to be incorrect.")
				Printer("Try again!")
				time.sleep(1)
				continue
			else: break

		else:
			Printer("No matching record found!"); time.sleep(1)
			times+=1
			if times>1:
				Printer("Loading",dots=2)
				while True:
					choice=input(Printer(f"""Since **{userid}** couldn't be found in the database, would you like to\n1. Create Account\n\n2. Try Again\n\n3. Exit\n\nCHOICE: """))
					if choice =='1': CreateAccount(); break
					elif choice=='2': ExistingLogin(times); break
					elif choice=="3": Exit()


def LoginSetup():					#Deals with login part of main program
	while True:
		choice=input(Printer('Are you a new player?(Y/N) '))
		choice=choice.upper()
		if choice=="Y":
			CreateAccount()
			Printer("Loading",dots=4)
			PlayerIntro()
			break
		elif choice=='N':
			ExistingLogin()
			Printer("Login successfull!")
			break