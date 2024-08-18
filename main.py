import helper

def main():
	helper.Printer("""
	  	       _   _    _    _   _  ____ __  __    _    _   _ 
	  	      | | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
		      | |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
		      |  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
		      |_| |_/_/   \_|_| \_|\____|_|  |_/_/   \_|_| \_|
                                                
                            ---------Created By Imu$ak----------""",delay=0.0005)

	input(helper.Printer('\n\n\t\t\t\t  ↲ Press ENTER to start',clear=False))

	helper.LoginSetup()

	helper.Printer("Loading",dots=4,repetitions=1)
    
	while True:
		helper.Printer("""
                 ##   ##  ######   ##  ##   ##  ##
                 ### ###  ##       ### ##   ##  ##
                 #######  ##       ######   ##  ##
                 ## # ##  ####     ######   ##  ##
                 ##   ##  ##       ## ###   ##  ##
                 ##   ##  ##       ##  ##   ##  ##
                 ##   ##  ######   ##  ##    ####\n\n""",delay=0.0005)
		choice=input(helper.Printer("""
                1. Play Game                      _________
                                                           |
                2. Game Help                               0
                                                          /|\\
                3. View Profile                           / \\
                                                 ______________
                4. Leaderboard
                
                5. Exit
        """,delay=0.005,clear=False))
		if choice=='1':
			pass
		elif choice=='2':
		   pass
		elif choice=='3':
			pass
		elif choice=='4':
			pass
		elif choice=='5':
			helper.Exit()

main()