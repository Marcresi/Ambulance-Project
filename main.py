from webbrowser import get
from fastapi import FastAPI
from mapwithlist import generate_mapwithlist

app=FastAPI()

@app.get('/map')
def generate():
    generate_mapwithlist()
    return ""

    
