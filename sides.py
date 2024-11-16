import efx,data

Player=None

def LoginSetup():					#Deals with login part of main program
	while True:
		choice=input(efx.Printer('Are you a new player?(Y/N) ')); choice=choice.upper()

		if choice=="Y":
			CreateAccount()
			efx.Printer("Loading....")
			input(efx.Printer(efx.lore+'\n\n\n\n\n\n↲ Press ENTER to continue!',delay=0.0005))
			efx.Printer("Log in with your account to play.",pdelay=0.5)
			ExistingLogin()
			efx.Printer('Make sure to read HELP before playing!',pdelay=1.25)
			break

		elif choice=='N':
			ExistingLogin()
			break

	efx.Printer('Loading...')


def CreateAccount():					#Deals with account creation
	while True:
		efx.Printer("""
\t\t/ ` _ _  _ _|_ _    _  _ _ _     _ _|_
\t\t\_,| (/_(_| | (/_  (_|(_(_(_)|_|| | |\n\t\t\t\t\t\t\t\t\tTo go back, leave any field empty!""",delay=0.0001)
		PlayerData={'words':([],[],[])}
		PlayerData['name']=input(efx.Printer("\nName: ",clear=False)).title()
		PlayerData['userid']=input(efx.Printer("\nCreate display name: ",clear=False)).strip()
		PlayerData['passwd']=input(efx.Printer("\nCreate password: ",clear=False)).strip()

		if '' in PlayerData.values():
			efx.Printer("All fields are mandatory!",pdelay=0.5)
			continue

		efx.Printer("Checking data format authenticity....")

		errors="Seems like the data you entered have the following errors:\n\n"
		if len(PlayerData["name"])<4:
			errors+="~ The name entered doesnt appear to be authentic.\n\n"
		if len(PlayerData["userid"])<4:
			errors+="~ Display name must be atleast 4 characters long!\n\n"
		if len(PlayerData["passwd"])<6:
			errors+="~ Password too weak. Must be atleast 6 characters long!\n\n"

		if errors.count('\n')==2:
			efx.Printer("Data format valid!",pdelay=0.5)
			efx.Printer("Checking for duplication with existing records....")

			if data.Verifier(PlayerData["userid"])=='user exists':
				efx.Printer("User with display name already exists! Try logging in?",pdelay=0.5)
				continue

			efx.Printer("No duplication found!",pdelay=0.5)
			efx.Printer("Account created successfully!",pdelay=1)
			data.DataAdder(PlayerData)
			break
		else:
			efx.Printer(errors+'Try again I guess?',pdelay=2)


def ExistingLogin():				#Deals with login for existing players
	global Player

	while True:
		efx.Printer("""
\t\t|  _  _ . _
\t\t|_(_)(_||| |
\t\t      _|""",delay=0.0005)
		userid=input(efx.Printer("\n\nEnter display name: ",clear=False)).strip()
		passwd=input(efx.Printer("\nEnter password: ",clear=False)).strip()

		if ''==userid or ''==passwd:
			efx.Printer("All fields are mandatory!",pdelay=1)
			continue

		efx.Printer("Checking database for username....")

		if data.Verifier(userid)=='user exists':
			efx.Printer("Checking password....")
			if data.Verifier(userid,passwd)=='incorrect password':
				efx.Printer("Password is incorrect! Try again!",pdelay=1)
				continue
			else:
				efx.Printer('Login Successfull!',pdelay=1)
				Player=data.LoadData(userid)
				break

		else:
			efx.Printer('No record found!',pdelay=0.5)
			while True:
				choice=input(efx.Printer(
f"""Since **{userid}** couldn't be found in the database, try one of these\n
\t[1] Create an account\n\n\t[2] Try Again\n\n\t[3] Exit\n\nCHOICE: """))

				if choice in ('1','create an account'):
					CreateAccount()
					break

				elif choice in ('2','try again'):
					ExistingLogin()
					break

				elif choice in ("3",'exit'):
					choice=efx.Exit()
					if choice==False: ExistingLogin()


def Profile():					#Deals with Profile related activities
	global Player
	passwd='*'*len(Player['passwd']);text='[sp] See Password\t'

	while True:
		Profile_display=f"""
\t\t _  _  _  _ ___    __
\t\t|_)|_)/ \|_  | |  |_
\t\t|  | \\\\_/|  _|_|__|__
\n\tᑎᗩᗰE : {Player['name']}
\n\tᑌSEᖇᑎᗩᗰE : {Player['userid']}
\n\tᑭᗩSSᗯOᖇᗪ : {passwd}
\n\n\n\n  {text}[edp] Edit Profile\t[cp] Check Progress\t[bk] Back\n
CHOICE: """
		choice=input(efx.Printer(Profile_display,delay=0.001)).lower().strip()

		if choice in ('see password','sp'):
			passwd=Player['passwd']
			text=''

		elif choice in ('edit profile','edp'):
			TPlayer=Player.copy(); txt="What would you like to change?"

			while True:
				choice=input(efx.Printer(f'{txt}\n\n[1] Name\t\t[2] Username\t\t[3] Password\t\t[4] Nothing\n\nCHOICE: ',delay=0.005)).lower().strip()

				if choice in ('1','name'):
					while True:
						name=input(efx.Printer('\nNew Name: '))
						if len(name)>=4: TPlayer['name']=name; break
						else: efx.Printer("Name doesn't appear to be authentic!",pdelay=0.5)

				elif choice in ('2','username'):
					while True:
						userid=input(efx.Printer('\nNew Username: '))
						if Player['userid']==userid or userid=='': efx.Printer('Change to NEW display name!'); continue

						if data.Verifier(userid)!='user exists': TPlayer['userid']=userid; break
						else: efx.Printer('A user with the username already exists!',pdelay=0.5)

				elif choice in ('3','password'):
					while True:
						passwd=input(efx.Printer('\nNew Password: '))
						if len(passwd)>=6: TPlayer['passwd']=passwd; break
						else: efx.Printer('Password must be atleast 6 characters long!',pdelay=0.5)

				elif choice in ('4','nothing'):
					break

				if TPlayer!=Player: txt="Any more changes?"

			if TPlayer!=Player:
				efx.Printer("Applying changes...")
				data.DataAdder(TPlayer,rmv=Player)
				Player.update(TPlayer)

			passwd="*"*len(Player['passwd']);text='[sp] See Password\t'

		elif choice in ('check progress','cp'):
			prog=Player['words']
			efx.Printer(efx.diffics+f"\n\t     {len(prog[0])}/50\t\t\t\t{len(prog[1])}/50\t\t\t\t    {len(prog[2])}/50\n\t      {len(prog[0])*2}%\t\t\t\t {len(prog[1])*2}%\t\t\t\t     {len(prog[2])*2}%",delay=0.0001)
			input(efx.Printer('\n\n\n\n\n\n↲ Press ENTER to continue',clear=False,delay=0.005))

		elif choice in ('back','bk'):
			break


def Leaderboard():				#Responsible for creating and updating the Leaderboard
	LB=data.LoadData()

	if len(LB) in range(2,6):
		final=''
		for num in range(len(LB)):
			list=f"\n{num+1:>19}       {LB[num]['userid']:>25}     {sum(len(LB[num]['words'][i]) for i in range(3)):>20}\n"
			final+=list
	else:
		final="\n\nCannot display Leaderboard!"
	efx.Printer(efx.Lboard+final,delay=0.0005)
	input('\n\n\n\n\n↲')
