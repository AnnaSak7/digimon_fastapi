from fastapi import FastAPI, status, HTTPException
from data import digimonData
from typing import Optional
import random
import operator


app = FastAPI()

#GET / -> Ger en lista med alla Digimons
# @app.get("/")
# async def root():
#     return digimonData


# GET /?sort={hp|sp|defense|attack|intelligence|speed}:{desc|asc} -> Sorted list of Digimons, optionally specify ordering by appending `:asc` for ascending or `:desc` for descending. You decide on the default :slightly_smiling_face:

sort_options = {"hp": "lv50HP", "sp": "lv50SP", "defense":"lv50Def", "attack":"lv50Atk", "intelligence": "lv50Int", "speed": "lv50Spd" }

def sort(dataset, level):
    list = {}
    for digimon_id in digimonData:
        list[digimon_id] = dataset[digimon_id][level]
    
    sorted_list = sorted(list.items(), key=operator.itemgetter(1))
    
    index = []
    for item in sorted_list:
        index.append(item[0])
        
    sorted_digimons = {}
    for number in index:
        sorted_digimons[number] = dataset[number]
    
    return sorted_digimons

@app.get("/")
async def root(*, sort: Optional[str] = None, stage: Optional[str] = None, type: Optional[str] = None):
    # 'Optional & None is making query as optional since by default it is required
    
    if not sort and not type and not stage:
        return digimonData
    
    if sort not in sort_options:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sort option not found')

    else:
        category = sort_options[sort]
        sort(digimonData, category)
        
    





@app.get("/get-by-name")
def get_digimon(name: Optional[str] = None):
    for digimon_id in digimonData:
        if digimonData[digimon_id]["digimon"] == name:
            return digimonData[digimon_id]
    return {"Data": "Not found"}



# Getting a specific Digimon
# GET /:number -> Ger Digimon med det numret om den finns, 404 annars
@app.get("/{digimon_id}", status_code=status.HTTP_200_OK)
async def specific_digimon(digimon_id):
    # if int(digimon_id) < 1 or int(digimon_id) > 249:
    if digimon_id not in digimonData:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Digimon id does not exist')
        
    return digimonData[digimon_id]


# Getting a random Digimon
# GET /random
@app.get("/random")
async def random_digimon():
    num = random.randint(1, 249)
    print(f'num is {num}')
    number = str(num)
    digimon = digimonData[number]
    print(f'digimon : {digimon}')
    return digimon
    


# Listing Digimons

# GET /?stage=…                                                                                   -> Returns all Digimons of a certain stage
# GET /?type=…                                                                                     -> Returns all Digimons of a certain type
# GET /?attribute=…                                                                              -> Returns all Digimons of a certain attribute


