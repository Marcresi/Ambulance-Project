from fastapi import FastAPI
from app.mapwithlist import generate_mapwithlist
import pymongo
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

@app.get('/')
def welcome():
    return "Welcome to our Ambulance Booking System"

@app.get('/map')
def generate():
    generate_mapwithlist()
    return "Genrating List of hospitals with ambulance services."

@app.get('/register/name={name}&email={email}&password={password}')
def register(name:str,email:str,password:str):
    client = pymongo.MongoClient("mongodb+srv://hospital:n%40GAmXWZbPr.n3c@ambulance.ymqigbw.mongodb.net/test")
    mydb = client["ambulance"]
    mycol = mydb["userlogin"]
    data = {"Name":f"{name}","Email":f"{email}","Password":f"{password}"}
    if mycol.insert_one(data):
        return True
    else:
        return False

@app.get('/login/name={name}&password={password}')
def login(name:str,password:str):
    client = pymongo.MongoClient("mongodb+srv://hospital:n%40GAmXWZbPr.n3c@ambulance.ymqigbw.mongodb.net/test")
    mydb = client["ambulance"]
    mycol = mydb["userlogin"]
    if mycol.find({},{'Name':f"{name}","Password":f"{password}"}):
        return True
    else:
        return False
    
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)