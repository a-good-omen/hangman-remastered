import efx
from sides import LoginSetup
from game import Menu

def main():				#THE ORIGIN
	input(efx.Printer(efx.intro,delay=0.0005))

	LoginSetup()

	Menu()

main()
