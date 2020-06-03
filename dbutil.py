from pymongo import MongoClient
from pprint import pprint
import bcrypt
import threading

ACTIVE_NOTIF_STATUS = 'ACTIVE'
CLOSED_NOTIF_STATUS = 'CLOSED'

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

def getTasks():
    return [
        {
            'name': 'Task1',
            'description': 'Simple Task',
            'full': '1 + 2 + 3'
        },
        {
            'name': 'Task2',
            'description': 'Medium Task',
            'full': '1 * 2 * 3'

        },
        {
            'name': 'Task3',
            'description': 'Hard Task',
            'full': '1 ^ 2 ^ 3'
        }
    ]

def insertHelpNotification(username):
    db.notifications.insert_one(
        {'username': username, 'notifStatus': ACTIVE_NOTIF_STATUS})

def updateHelpNotificationStatus(username, notifStatus):
    db.notifications.update_many({'username': username}, [{'$set': {'notifStatus': notifStatus}}])

def getNotifications():
    return list(db.notifications.find({'notifStatus': ACTIVE_NOTIF_STATUS}))


def disableHelpNotification(username):
    updateHelpNotificationStatus(username, CLOSED_NOTIF_STATUS)

# Place of functions below can be discussed. It is not really related to DB functions.
# But TeacherWindow class - is not very good too. If we faced with a lot of such functions, can move them somewhere.
def watchHelpMessages(showUpdates):
    change_stream = db.notifications.watch([{'$match': {'operationType': 'insert'}}])
    print('Watching of help messages started.')
    for _ in change_stream:
        showUpdates()
    print('Watching of help messages finished.')

def startWatchHelpMessages(showUpdates):
    threading.Thread(target=watchHelpMessages, name='HelpMessagesWatch-Thread',
                     args=(showUpdates,), daemon=True).start()
