from pymongo import MongoClient

def main():
	client = MongoClient("localhost", 27017)
    db = client.csci2963
    defs = db.definitions

    #add a new word
    word = { "word": "Jordan",
             "definition": "Haskell irl" }
			 
    #capture word id
	word_id = defs.insert_one(word).inserted_id

	#find a single word
    print( defs.find_one() )
	
	#find a word by name
    print( defs.find_one({"word": "Jordan"}) )
	
	#find a word by id
    print( defs.find_one({"_id": word_id}) )

if __name__ == "__main__":
main()