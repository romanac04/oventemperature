import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

MIN_TEMP = 300
MAX_TEMP = 500

class Oven():
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def get_reading(self):
        self.current_temp = random.randrange(self.min, self.max)
        return self.current_temp
         
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def get_temp():
    o = Oven(MIN_TEMP, MAX_TEMP)
    return {"temperature": o.get_reading()}



