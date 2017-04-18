from pymongo import MongoClient
import datetime

def main():
	client = MongoClient("localhost", 27017)
    db = client.csci2963
    defs = db.definitions
	
	#find a random word
    randomWord = defs.find_one()
	print(randomWord)
	
	#increment word dates list	
	curTime = datetime.datetime.now()
	defs.update({name: randomWord}, {$push: {dates: {curTime} } }

if __name__ == "__main__":
main()