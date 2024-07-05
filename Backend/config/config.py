
from decouple import config
from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus
# username = 'root'
# password = 'Password@12345'
username = config("USER_NAME")
password = config("PASS_WORD")
#for encoding the .env data
# encoded_username = quote_plus(username)
# encoded_password = quote_plus(password)
# uri = f"mongodb+srv://{encoded_username}:{encoded_password}@dbcluster.ynwoblw.mongodb.net/?retryWrites=true&w=majority&appName=DbCluster"
uri = f"mongodb+srv://{username}:{password}@cluster0.iyiykhm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
uri = f"mongodb+srv://{username}:{password}@dbcluster.ynwoblw.mongodb.net/?retryWrites=true&w=majority&appName=DbCluster"
# Create a new client and connect to the server
client = MongoClient(uri)
db=client.Shoppie


customers_collection= db['customers']
# Send a ping to confirm a successful connection
try:

    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)