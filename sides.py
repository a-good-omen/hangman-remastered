import time,sys,efx,data

Player=None

def PlayerIntro(Player):					#Deals with intro to the game. Only for first time players
	efx.Printer("Welcome {Player}!")
	time.sleep(0.1)
	efx.Printer("""In the late 1900s, a secluded village was haunted by a sinister figure known by the villagers as the Hangman.\nThe legend told of a dark,cursed parchment that appeared in the hands of those who crossed the Hangman’s path.\nThe parchment bore a hidden word that must be guessed to escape.
 
For each incorrect guess, a spectral figure of the Hangman would draw closer to completion—a noose tightening\naround a ghostly neck. The cursed villagers who failed to guess the word were seized by the Hangman, their\nsouls trapped within the parchment’s dark embrace.

Though the Hangman disappeared centuries ago, whispers of his curse persist. Those who find the cursed \nparchment or hear the chilling challenge are said to risk becoming the Hangman’s next victims, forever bound to\nthe terror of his eternal game.

**This game has been adapted from this lore.""")
	time.sleep(1)


def CreateAccount():					#Deals with account creation
	while True:
		efx.Printer("""
\t\t/ ` _ _  _ _|_ _    _  _ _ _     _ _|_
\t\t\_,| (/_(_| | (/_  (_|(_(_(_)|_|| | |""",delay=0.004)
		PlayerData={}
		PlayerData['name']=input(efx.Printer("\n\nName: ",clear=False)).title()
		PlayerData['email']=input(efx.Printer("\nEmail: ",clear=False)).lower()
		PlayerData['userid']=input(efx.Printer("\nCreate display name: ",clear=False))
		PlayerData['passwd']=input(efx.Printer("\nCreate password: ",clear=False))

		if '' in PlayerData.values():
			efx.Printer("All fields are mandatory!"); time.sleep(0.5); continue
		
		efx.Printer("Checking data format authenticity....")
		errors="Seems like the data you entered have the following errors:\n\n"
		if len(PlayerData["name"])<4:
			errors+="~ The name entered doesnt appear to be authentic.\n\n"
		if '@gmail.com' not in PlayerData['email']:
			errors+="~ Email doesn't appear to be authentic.\n\n"
		if len(PlayerData["userid"])<4:
			errors+="~ Display name must be atleast 4 characters long!\n\n"
		if len(PlayerData["passwd"])<8:
			errors+="~ Password too weak. Must be atleast 8 characters long!\n\n"

		if errors.count('\n')==2:
			efx.Printer("Data format valid!");time.sleep(0.05)
			efx.Printer("Checking for duplication with existing records....")
			if data.Verifier(PlayerData["userid"])==True:
				efx.Printer("User with display name already exists! Try using a different display name!"); time.sleep(0.5); continue
			data.DataAdder(PlayerData)
			efx.Printer("No duplication found!")
			efx.Printer("Account created successfully!")
			time.sleep(1)
			break
		else:
			efx.Printer(errors+'Try again i guess?')
			time.sleep(2)


def ExistingLogin(times=0):				#Deals with login for existing players
	import data
	while True:
		efx.Printer("""
\t\t|  _  _ . _
\t\t|_(_)(_||| |
\t\t      _|""",delay=0.004)
		userid=input(efx.Printer("\n\nEnter display name: ",clear=False))
		passwd=input(efx.Printer("\nEnter password: ",clear=False))
		if ''==userid or ''==passwd: efx.Printer("All fields are mandatory!"); time.sleep(1); continue
		
		efx.Printer("Checking datbase for matching records....")

		if data.Verifier(userid)==True:
			if data.Verifier(userid,passwd)==False:
				efx.Printer("Password is incorrect!")
				efx.Printer("Try again!")
				time.sleep(1)
				continue
			else: return userid

		else:
			efx.Printer("No matching record found!"); time.sleep(1)
			times+=1
			if times>1:
				efx.Printer("Hmmm...")
				while True:
					choice=input(efx.Printer(f"""Since **{userid}** couldn't be found in the database, would you like to\n\n1. Create Account\n\n2. Try Again\n\n3. Exit\n\nCHOICE: """))
					if choice =='1': CreateAccount(); break
					elif choice=='2': ExistingLogin(times); break
					elif choice=="3":
						choice=efx.Exit(opt='login_page')
						if choice==False: ExistingLogin(times)


def LoginSetup():					#Deals with login part of main program
	global Player
	while True:
		choice=input(efx.Printer('Are you a new player?(Y/N) '))
		choice=choice.upper()

		if choice=="Y":
			CreateAccount()
			efx.Printer("Loading....")
			Player=ExistingLogin()
			PlayerIntro(Player)
			break

		elif choice=='N':
			Player=ExistingLogin()
			efx.Printer("Login successfull!"); time.sleep(1)
			break
			
		else:break
		
		
def LoadGame():
	while True:
		efx.Printer("Choose Difficulty level\n\n")
		print(\
"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣧⠀⢀                                                                  ⡠⠄⠀⠀⠄⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⠃⠻⣧⠈⣦                                                                ⠊⢀⣤⣞⣔⢤⡈⠆
⠀⠀⠀⠀⠀⠀⠀⠤⠴⠶⠿⢿⣿⡿⠁⠀⠀⠈⠆⠘⣷⡄                                                            ⠄⢠⣿⣧⣿⣿⣟⠇⠈⠢⡀
⠀⠀⣤⣤⣤⣤⣤⣤⠤⠆⠂⣸⠟⠀⢀⣐⠒⠶⢶⣤⣽⣿⣦⣤⣤⣤⣀⣀⣀⠀			 ⣀⣀                            ⠌⠀⣿⠿⠿⠿⠿⣿⡀⢰⠒⠊
⠀⠀⠈⠛⢿⣿⣷⡄⠀⠀⢠⠋⢠⣾⡟⠻⣷⣄⠀⠀⠈⠉⠛⠻⢿⣿⡿⠋                   ⠰⣿⣿⣿⣿⠆                        ⠌⢀⡾⠁⠀⠀⠀⠀⡈⣇⠀⢆
⠀⠀⠀⠀⠀⠙⢻⣿⣦⠀⠁⢠⣿⣿⠁⠀⣿⣿⣆⠀⣇⠀⠀⣴⠟⠁                  ⢀⣀⣠⣇⣙⣻⣟⣋⣸⣄⣀⣀                  ⣀⠄⠃⠘⠇⠀⠈⠀⠀⠉⠀⣸⠆⡈⠢⢀
⠀⠀⠀⠀⠀⠀⢸⣿⠹⣷⡄⠸⣿⣿⡄⠀⣿⣿⠏⠀⣿⡀⠊⢀⡴⠃                  ⠙⠟⣿⣿⠋⠋⠙⠙⣿⣿⠻⠋                 ⠸⡀⢰⣎⠀⠀⠀⠀⠀⢀⡴⠎⠁⠀⢐⠄⠀⡕
⠀⠀⠀⠀⠀⠀⢸⡇⢰⠀⠙⢆⠈⠻⢷⡴⠟⠋⠀⠀⣿⣷⣾⠟                    ⣠⣴⢿⣿⠺⣶⣷⠗⣿⡿⣧⣄                   ⠑⠀⠪⡢⡀⠀⠀⠀⠈⠀⣀⢀⡴⠅⠀⠈
⠀⠀⠀⠀⠀⠀⠸⠀⣸⠀⠀⠀⢀⣀⣠⣤⠶⠊⠁⠀⢹⣿⡃                            ⠈⠁                           ⢄⠑⠯⢞⣪⡀⣴⣾⡗⠋⠀⡀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⣴⣶⣿⣿⣿⣭⡀⠂⢤⣄⣀⢸⣿⣇                                                          ⠑⠂⠄⡈⠙⠈⢁⡠⠔⠂
⠀⠀⠀⠀⠀⠀⠀⣼⣿⠿⠛⠉⠀⠉⠙⠛⠲⠤⠈⠙⠿⣿⣿⡄                                                             ⠈⠀⠐⠁
⠀⠀⠀⠀⠀⠀⠰⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧""")
		efx.Printer("\n\t     [1] Cursed\t\t\t           [2] Ghost\t\t\t    [3] Phantom",delay=0.005,clear=False)
		choice=input(efx.Printer("\n\nCHOICE: ",clear=False)); choice.lower()
		if choice in ("cursed","1"):
			diffic="Cursed"; break
		elif choice in ("ghost","2"):
			diffic="Ghost"; break
		elif choice in ("phantom","3"):
			diffic="Phantom"; break
