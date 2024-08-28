import pickle

def DataAdder(data):				#Appends new player to the database
	global PlayerCount
	with open("PlayerData.dat","ab") as data_file:
		pickle.dump(data,data_file)


def Verifier(user,password=None):				#Helps verify player credentials
	data_file=None

	try:
		data_file=open("PlayerData.dat","rb")
		while True:
			PlayerData=pickle.load(data_file)
			if PlayerData['userid']==user:
 				if password:
	 				if PlayerData['passwd']==password: return 'password verified'
	 				else: return 'incorrect password'
	 			else: return 'user exists'

	except EOFError: return False
	except FileNotFoundError: return 'FileNotFound'
	finally:
		if data_file: data_file.close()


def DataLoader(user):
	data_file=open("PlayerData.dat","rb")
	try:
		while True:
			PlayerData=pickle.load(data_file)
			if Verifier(user): return PlayerData
	except EOFError: data_file.close()

def LoadWord(user,difficulty):
	...