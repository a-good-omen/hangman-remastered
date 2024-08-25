import efx,sides

def main():
	efx.Printer(\
"""	  	       _   _    _    _   _  ____ __  __    _    _   _ 
	  	      | | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
		      | |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
		      |  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
		      |_| |_/_/   \_|_| \_|\____|_|  |_/_/   \_|_| \_|
                                                
                            ----------Created By Imu$ak----------""",delay=0.0005)

	input(efx.Printer('\n\n\t\t\t\t  ↲ Press ENTER to start',clear=False))

	sides.LoginSetup()

	efx.Printer("Loading....")
	def Menu():
		while True:
			efx.ClearScreen()
			print(\
f"""		.___  ___.  _______ .__   __.  __    __  
		|   \/   | |   ____||  \ |  | |  |  |  | 		 		■USER: {sides.Player}■
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
                
                [5] Exit""")
        
			choice=input(efx.Printer("CHOICE: ",delay=0.005,clear=False))
			efx.ClearScreen() 
			if choice=='1':
				efx.Printer("Loading....")
				sides.LoadGame()
			elif choice=='2':
			   pass
			elif choice=='3':
				pass
			elif choice=='4':
				pass
			elif choice=='5':
				choice=efx.Exit(opt='menu')
				if choice==False: Menu()
	Menu()		

main()
