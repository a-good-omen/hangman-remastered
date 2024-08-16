import pickle

def DataAdder(data):				#Appends new player to the database
	with open("PlayerData","wb") as data_file:
		pickle.dump(data,data_file)


def CheckExistence(user):				#Helps check if user
 	pass