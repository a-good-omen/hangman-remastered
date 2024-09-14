import pickle

def DataAdder(data):				#Appends new player to the database
	data_file=open("PlayerData.dat","rb+")
	try:
		recs=pickle.load(data_file)
		recs.append(data)
		recs.sort(key=lambda x: x["name"])
		data_file.seek(0)
		pickle.dump(recs,data_file)
	except EOFError:
		recs=[]; recs.append(data)
		pickle.dump(recs,data_file)
	finally: data_file.close()


def Verifier(user,password=None):				#Helps verify player credentials
	try:
		data_file=open("PlayerData.dat","rb+")
		PlayersData=pickle.load(data_file)
		for Player in PlayersData:
			if Player["userid"]==user:
				if password:
					if Player["passwd"]==password: return "verified password"
					else: return 'incorrect password'
				else: return 'user exists'
	except EOFError: return False
	except FileNotFoundError:
		data_file=open("PlayerData.dat","wb")
	finally: data_file.close()


def LoadWord(user,difficulty):
	...


'''with open("PlayerData.dat","rb") as data_file:
	data=pickle.load(data_file)
	print(data)
'''