import time,os

def ClearScreen():				#Calling this will clear the terminal window (won't work in the IDLE)
        print("\033[H\033[J")
        os.system('cls' if os.name == 'nt' else 'clear')
      
          
def Printer(text,delay=0.5):				#Helps create dynamic typing effect
	for i in text:
		print(i,end="",flush=True)
		time.sleep(delay)
	return ''
	

def Loader():						#Creates the loading effect
	for i in range(3):
		Printer("LOADING",delay=0.05)
		for i in range(4):
			time.sleep(0.5)
			print('.',end="",flush=True)
		time.sleep(0.5)
		print('\r'+' '*11+'\r',end="")
		
																						
def LoginSetup():				#Deals with login part of main program
	choice=input(Printer('Are you a new player?(Y/N) ',delay=0.05))
	choice=choice.upper(); ClearScreen()
	if choice=="Y":
		pass
	elif choice=='N':
		user=input(Printer("Enter Username: ",delay=0.05))			
		passwd=input(Printer("\nEnter Password: ",delay=0.05))