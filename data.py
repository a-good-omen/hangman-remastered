import pickle
from helper import Printer

PlayerCount=2

def DataAdder(data):				#Appends new player to the database
	global PlayerCount
	with open("PlayerData","ab") as data_file:
		pickle.dump(data,data_file)


def Verifier(user,password=None):				#Helps verify player credentials
	global PlayerCount
	with open("PlayerData","rb") as data_file:
 		for i in range(PlayerCount):
 			PlayerData=pickle.load(data_file)
 			if PlayerData['userid']==user:
 			#	Printer("User found!")
 				if password:
 					Printer("Checking password",dots=3)
 					if PlayerData['passwd']==password: return True
 					else: return False
 				else: return True
 			else: return False