import pickle
from random import choice

def DataAdder(data,rmv=None):				#Appends new player to the database
	data_file=open("PlayerData.dat","rb+")

	try:
		recs=pickle.load(data_file)
		recs.append(data)

		if rmv!=None: recs.remove(rmv)

		recs.sort(key=lambda x: x["name"])
		data_file.seek(0)
		pickle.dump(recs,data_file)
		data_file.truncate()

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

	except FileNotFoundError: data_file=open("PlayerData.dat","wb")

	finally: data_file.close()


def LoadWord(difficulty,Glist):				#Selects the word to guess
	with open("Words.dat","rb") as word_file:
		times={"Cursed":0,"Ghost":1,"Phantom":2}

		for count in range(times[difficulty]+1):
			words=pickle.load(word_file)
			if count==times[difficulty]:
				while True:
					word=choice(words)
					if word not in Glist[times[difficulty]]: return word


def LoadData(userid):			#Loads "userid's" data from the database
	with open("PlayerData.dat","rb") as data_file:
		PlayerData=pickle.load(data_file)

	for player in PlayerData:
		if player['userid']==userid: return player
