import pickle,efx

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
 					efx.Printer("Checking password....")
	 				if PlayerData['passwd']==password: return 'True'
	 				else: return False
	 			else: return 'True'
	except EOFError: return False
	except FileNotFoundError: return True
	finally:
		if data_file: data_file.close()