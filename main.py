from fastapi import FastAPI
from data import digimonData
import random


app = FastAPI()

@app.get("/")
async def root():
    return digimonData

    


# Listing Digimons
#GET / -> Ger en lista med alla Digimons
# GET /?sort={hp|sp|defence|attack|intelligence|speed}:{desc|asc} -> Sorted list of Digimons, optionally specify ordering by appending `:asc` for ascending or `:desc` for descending. You decide on the default :slightly_smiling_face:
# GET /?stage=…                                                                                   -> Returns all Digimons of a certain stage
# GET /?type=…                                                                                     -> Returns all Digimons of a certain type
# GET /?attribute=…                                                                              -> Returns all Digimons of a certain attribute

# Getting a specific Digimon
# GET /:number -> Ger Digimon med det numret om den finns, 404 annars

# Getting a random Digimon
# GET /random