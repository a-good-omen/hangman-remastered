import time,efx,data

Player=None

def LoginSetup():					#Deals with login part of main program
	while True:
		choice=input(efx.Printer('Are you a new player?(Y/N) '))
		choice=choice.upper()

		if choice=="Y":
			CreateAccount()
			efx.Printer("Loading....")
			input(efx.Printer(efx.lore+'\n\n\n\n\n\n↲ Press ENTER to continue!',delay=0.005))
			efx.Printer("Log in with your account to play."); time.sleep(0.5)
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
		PlayerData={'data':[0,0,0],'words':[]}
		PlayerData['name']=input(efx.Printer("\n\nName: ",clear=False)).title()
		PlayerData['userid']=input(efx.Printer("\nCreate display name: ",clear=False)).strip()
		PlayerData['passwd']=input(efx.Printer("\nCreate password: ",clear=False)).strip()

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
			efx.Printer("Data format valid!");time.sleep(0.5)
			efx.Printer("Checking for duplication with existing records....")
			if data.Verifier(PlayerData["userid"])=='user exists':
				efx.Printer("User with display name already exists! Try logging in?"); time.sleep(0.5); continue
			data.DataAdder(PlayerData)
			efx.Printer("No duplication found!"); time.sleep(0.5)
			efx.Printer("Account created successfully!"); time.sleep(1)
			break
		else:
			efx.Printer(errors+'Try again i guess?'); time.sleep(2)


def ExistingLogin():				#Deals with login for existing players
	global Player
	while True:
		efx.Printer("""
\t\t|  _  _ . _
\t\t|_(_)(_||| |
\t\t      _|""",delay=0.004)
		userid=input(efx.Printer("\n\nEnter display name: ",clear=False)).strip()
		passwd=input(efx.Printer("\nEnter password: ",clear=False)).strip()
		if ''==userid or ''==passwd: efx.Printer("All fields are mandatory!"); time.sleep(1); continue

		efx.Printer("Checking database for matching records....")

		if data.Verifier(userid)=='user exists':
			efx.Printer("Checking password...")
			if data.Verifier(userid,passwd)=='incorrect password':
				efx.Printer("Password is incorrect!"); time.sleep(0.5)
				efx.Printer("Try again!"); time.sleep(1)
				continue
			else:
				Player=data.LoadData(userid)
				break

		else:
			efx.Printer("No matching record found!"); time.sleep(1)

			while True:
				choice=input(efx.Printer(
f"""Since **{userid}** couldn't be found in the database you must choose to,\n
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


def Profile():
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
\n\n\n\n\t{text}[edp] Edit Profile\t[sgp] See Game Progress\t\t[ng] Do Nothing(go back)\n
CHOICE: """
		choice=input(efx.Printer(Profile_display,delay=0.005)).lower().strip()

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
						else: efx.Printer("Name doesn't appear to be authentic!"); time.sleep(0.5)
				elif choice in ('2','username'):
					while True:
						userid=input(efx.Printer('\nNew Username: '))
						if data.Verifier(userid)!='user exists': TPlayer['userid']=userid; break
						else: efx.Printer('A user with the username already exists!'); time.sleep(0.5)
				elif choice in ('3','password'):
					while True:
						passwd=input(efx.Printer('\nNew Password: '))
						if len(passwd)>=8: TPlayer['passwd']=passwd; break
						else: efx.Printer('Password must be atleast 8 characters long!'); time.sleep(0.5)
				elif choice in ('4','nothing'):
					break

				txt="Any more changes?"

			if TPlayer!=Player:
				efx.Printer("Applying changes...")
				data.DataAdder(TPlayer,rmv=Player)
				Player.update(TPlayer)

			passwd="*"*len(Player['passwd']);text='[sp] See Password\t'


		elif choice in ('see game progress','sgp'):
			efx.Printer(efx.diffics_display,delay=0.0005)
			prog=Player['data']
			efx.Printer(f"\n\t     {prog[0]}/50\t\t\t\t{prog[1]}/50\t\t\t\t    {prog[2]}/50",clear=False,delay=0.005)
			efx.Printer(f"\n\t      {prog[0]*2}%\t\t\t\t {prog[1]*2}%\t\t\t\t     {prog[2]*2}%",clear=False,delay=0.005)
			input(efx.Printer('\n\n\n\n\n\n↲ Press ENTER to continue',clear=False,delay=0.005))

		elif choice in ('do nothing','ng'): break
