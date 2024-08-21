import pickle

def DataAdder(data):				#Appends new player to the database
	with open("PlayerData","ab") as data_file:
		pickle.dump(data,data_file)


def Verifier(user,password=None):				#Helps verify player credentials
	from helper import Printer
	try:
		data_file=open("PlayerData","rb")
		while True:
			PlayerData=pickle.load(data_file)
			if PlayerData['userid']==user:
 				if password:
 					Printer("Checking password",dots=3)
 					if PlayerData['passwd']==password: return True
 					else: return False
 				else: return True
	except EOFError:
			return False
	finally: data_file.close()