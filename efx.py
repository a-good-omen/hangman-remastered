import time,sys

def ClearScreen():				#Calling this will clear the terminal window (won't work in Python's' IDLE)
	screen=sys.stdout
	time.sleep(0.01)
	screen.write("\033[2J\033[H")
	screen.flush

     
def Printer(text,repetitions=1,clear=True,delay=0.05):					#Deals with dynamic typing effect
	dot="..." in text
	if clear: ClearScreen()
	for i in range(repetitions):
		for j in text:
			time.sleep(0.9 if dot and j=='.' else delay)
			print(j,end='',flush=True)
		time.sleep(0.05)
	return ''


def Exit(opt=False):				#Custom exit function
	if opt:
		while True:
			choice=input(Printer("Are you sure you want to exit?(Y/N) ")).upper()
			if choice=='Y':
				Printer("Exiting...")
				sys.exit()
			elif choice=='N':
				Printer("Exit request terminated!")
				return False
	else:
		Printer("Exitting...")
		ClearScreen()
		sys.exit()
