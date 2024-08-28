import efx,sides

def main():
	efx.Printer(\
"""	  	       _   _    _    _   _  ____ __  __    _    _   _ 
	  	      | | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
		      | |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
		      |  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
		      |_| |_/_/   \_|_| \_|\____|_|  |_/_/   \_|_| \_|
                                                
                         ----------Created By a-good-omen----------""",delay=0.0005)

	input(efx.Printer('\n\n\t\t\t\t  ↲ Press ENTER to start',clear=False))

	sides.LoginSetup()

	efx.Printer("Loading....")
	def Menu():
		while True:
			choice=input(efx.Printer(
f"""                .___  ___.  _______ .__   __.  __    __  
                |   \/   | |   ____||  \ |  | |  |  |  |                                  ■ USER: {sides.Player} ■
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
				sides.LoadGame()
			elif choice in ("game help",'2'):
				...
			elif choice in ("view profile",'3'):
				...
			elif choice in ("leaderboard",'4'):
				pass
			elif choice in ("exit",'5'):
				choice=efx.Exit(opt='menu')
				if choice==False: Menu()
	Menu()

main()