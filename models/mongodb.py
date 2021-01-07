import pymongo
from urllib import parse

class MongoDB:
    def __init__(self):
        self.dbConn,self.db = self.connect()

    def connect(self):
        user = 'Harish'
        password = parse.quote('Password@0123')
        db_name = 'movie_reviews'
        try:
            dbConn = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@cluster0.dgk5j.mongodb.net/{db_name}?retryWrites=true&w=majority")
            db = dbConn[db_name]
            return dbConn,db
        except Exception as e:
            print(str(e))

    def saveData(self, collectionName, data):
        try:
            collection = self.db[collectionName]
            collection.insert_one(data)
            return True
        except Exception as e:
            print(str(e))
            return False

    def saveMany(self, collectionName, data):
        try:
            collection = self.db[collectionName]
            collection.insert_many(data)
            return True
        except Exception as e:
            print(str(e))
            return False

    def fetchData(self, collectionName):
        try:
            return list(self.db[collectionName].find())
        except Exception as e:
            print(str(e))
            return False


    def updateData(self):
        pass

    def deleteData(self):
        pass
