from pymongo import MongoClient
from pprint import pprint
import bcrypt

MONGODB_URL = 'mongodb+srv://admin:StudyHelper-1@studyclaster-0lftw.mongodb.net/test?retryWrites=true&w=majority'
client = MongoClient(MONGODB_URL)
db = client.studyHelperDB

def printDbServerStatus():
    pprint(db.command('serverStatus'))
    print('Collection names: ', db.list_collection_names())

def insertUser(user):
    user['password'] = bcrypt.hashpw(user['password'], bcrypt.gensalt())
    db.users.insert_one(user)

def findUser(username):
    return db.users.find_one({'username': username})