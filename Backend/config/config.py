
from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus
username = 'root'
password = 'Password@12345'
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)
uri = f"mongodb+srv://{encoded_username}:{encoded_password}@dbcluster.ynwoblw.mongodb.net/?retryWrites=true&w=majority&appName=DbCluster"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)