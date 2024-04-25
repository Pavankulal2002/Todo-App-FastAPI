from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
database = client["Todo_fastapi"]
collection = database["todos"]
