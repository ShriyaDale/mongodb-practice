from pymongo import MongoClient, errors
from bson.json_util import dumps
from dotenv import load_dotenv
import os

load_dotenv()
MONGOUSER = os.getenv("MONGOUSER")
MONGOPASS = os.getenv("MONGOPASS")
MONGOHOST = os.getenv("MONGOHOST")
client = MongoClient(MONGOHOST, username=MONGOUSER, password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)

database = client["mmk2yy"]
restaurants = database["restaurants"] #creates a new collection, you don't need to use the create_collection method, mongodb does it automatically

record_1 = {
    "name": "Chipotle",
    "cuisine": "Mexican",
    "items offered": ["bowls", "burritos", "chips", "quesadillas"]
}

record_2 = {
    "name": "Subway",
    "cuisine": "America",
    "items offered": ["subs", "chips", "cookies", "soda"]
}

record_3 = {
    "name": "Uncle Julios",
    "cuisine": "Mexican",
    "items offered": ["nachos", "burritos", "chips", "quesadillas", "fajitas", "enchiladas"]
}

record_4 = {
    "name": "On the Border",
    "cuisine": "Mexican",
    "items offered": ["nachos", "burritos", "chips", "quesadillas", "fajitas", "enchiladas"]
}

record_5 = {
    "name": "Cheesecake Factory",
    "cuisine": "American",
    "items offered": ["nachos", "pasta", "cheesecake", "salads", "burgers", "enchiladas"]
}

restaurants.insert_many([record_1, record_2, record_3, record_4, record_5]) #insert all records at the same time
get_record = restaurants.find({"cuisine":"Mexican"}) #using find w/ the cuisine attribute to return 3 items

print(dumps(get_record, indent=2))





