import time,sys,efx,data,game

Player=None

def PlayerIntro():					#Outputs the lore of the game. Exclusively for first time players
	time.sleep(0.1)
	efx.Printer(efx.lore)
	time.sleep(1)


def LoginSetup():					#Deals with login part of main program
	global Player,PlayerData
	while True:
		choice=input(efx.Printer('Are you a new player?(Y/N) '))
		choice=choice.upper()

		if choice=="Y":
			CreateAccount()
			efx.Printer("Loading....")
			PlayerIntro()
			efx.Printer("Log in with your account to play."); time.sleep(0.1)
			ExistingLogin()
			break

		elif choice=='N':
			Player=ExistingLogin()
			efx.Printer("Login successfull!"); time.sleep(1)
			break


def CreateAccount():					#Deals with account creation
	while True:
		efx.Printer("""
\t\t/ ` _ _  _ _|_ _    _  _ _ _     _ _|_
\t\t\_,| (/_(_| | (/_  (_|(_(_(_)|_|| | |""",delay=0.004)
		PlayerData={}
		PlayerData['name']=input(efx.Printer("\n\nName: ",clear=False)).title()
		PlayerData['userid']=input(efx.Printer("\nCreate display name: ",clear=False))
		PlayerData['passwd']=input(efx.Printer("\nCreate password: ",clear=False))

		if '' in PlayerData.values():
			efx.Printer("All fields are mandatory!"); time.sleep(0.5); continue

		efx.Printer("Checking data format authenticity....")
		errors="Seems like the data you entered have the following errors:\n\n"
		if len(PlayerData["name"])<4:
			errors+="~ The name entered doesnt appear to be authentic.\n\n"
		if len(PlayerData["userid"])<4:
			errors+="~ Display name must be atleast 4 characters long!\n\n"
		if len(PlayerData["passwd"])<8:
			errors+="~ Password too weak. Must be atleast 8 characters long!\n\n"

		if errors.count('\n')==2:
			efx.Printer("Data format valid!");time.sleep(0.05)
			efx.Printer("Checking for duplication with existing records....")
			if data.Verifier(PlayerData["userid"])=='user exists':
				efx.Printer("User with display name already exists! Try logging in?"); time.sleep(0.5); continue
			data.DataAdder(PlayerData)
			efx.Printer("No duplication found!")
			efx.Printer("Account created successfully!")
			time.sleep(1)
			break
		else:
			efx.Printer(errors+'Try again i guess?')
			time.sleep(2)


def ExistingLogin(times=0):				#Deals with login for existing players
	while True:
		efx.Printer("""
\t\t|  _  _ . _
\t\t|_(_)(_||| |
\t\t      _|""",delay=0.004)
		userid=input(efx.Printer("\n\nEnter display name: ",clear=False)); userid.strip()
		passwd=input(efx.Printer("\nEnter password: ",clear=False)); passwd.strip()
		if ''==userid or ''==passwd: efx.Printer("All fields are mandatory!"); time.sleep(1); continue

		efx.Printer("Checking database for matching records....")

		if data.Verifier(userid)=='user exists':
			efx.Printer("Checking password...")
			if data.Verifier(userid,passwd)=='incorrect password':
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

def Menu():
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
                                game.LoadGame()
                        elif choice in ("game help",'2'):
                                ...
                        elif choice in ("view profile",'3'):
                                ...
                        elif choice in ("leaderboard",'4'):
                                ...
                        elif choice in ("exit",'5'):
                                choice=efx.Exit(opt='menu')
                                if choice==False: Menu()
