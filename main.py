import efx,sides,game

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
	
	efx.Menu()

main()