from pymongo import MongoClient, errors
from bson.json_util import dumps #NEVER PUT BSON IN YOUR REQUIREMENTS.TXT
#bson = binary json --> makes it smaller and faster
import os

#export MONGOPASS='' in your bashrc (use cluster address in your shell part of atlas)

# mongohost should look something like 'mongodb+srv://cluster0.xxxxx.mongodb.net/'
MONGOUSER = os.getenv('MONGOUSER')
MONGOPASS = os.getenv('MONGOPASS')
MONGOHOST = os.getenv('MONGOHOST')
client = MongoClient(MONGOHOST, username=MONGOUSER, password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
sampler = client.sample_restaurants
restaurants = sampler.restaurants