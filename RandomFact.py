pip install fastapi uvicorn

from fastapi import FastAPI, HTTPException, Query, Path
from pydantic import BaseModel

app = FastAPI()

facts = [
    {"id": 0, "fact": "Honey never spoils."},
    {"id": 1, "fact": "Bananas are berries, but strawberries aren’t."},
    {"id": 2, "fact": "The dot over the letter 'i' is called a tittle."},
    {"id": 3, "fact": "Octopuses have three hearts."},
    {"id": 4, "fact": "A day on Venus is longer than a year on Venus."},
]

class Fact(BaseModel):
    fact: str

def home():
    return{"Welcome to the Random Fact API!"}

def get_random_fact(id: int = Query(None, description = "Optional fact ID to retrieve")):
    if id is not None:
        if 0 <= id < len(facts):
            return facts[id]
        else:
            raise HTTPException(status_code=404, detail="Fact ID not found")

    import random 
    randon_fact = random.choice(facts)
    return random_fact

def get_fact_by_id(id: int = Path(..., description="Fact ID to retrieve")):
    if 0 <= id < len(facts):
        return facts[id]
    else:
        raise HTTPException(status_code=404, detail="Fact ID not found")
        
def add_fact(new_fact: Fact):
    new_id = len(facts)
    fact_object = {"id": new_id, "fact": new_fact.fact}
    facts.append(fact_object)
    return {"Fact added successfully", "fact": fact_object}
