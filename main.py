from fastapi import FastAPI, status
from starlette.responses import Response, JSONResponse
from pydantic import BaseModel
from typing import List
import json


app = FastAPI()

players_db = []

class Player(BaseModel):
    Number: int
    Name: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def hello():
    with open("hello.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    return Response(
        content=html_content,
        status_code=200,
        media_type="text/html"
    )
@app.get("/welcome")
def welcome(name: str):
    message = f"Welcome {name}"
    return JSONResponse(content={"message": message}, status_code=200)

@app.post("/players")
def add_players(players: List[Player]):
    players_db.extend(players)
    return Response(content=json.dumps([player.dict() for player in players_db]), media_type="application/json", status_code=201)

# @app.post("/players", status_code=status.HTTP_201_CREATED)
# def add_players(players: List[Player]):
#     players_db.extend(players)
#     return players_db