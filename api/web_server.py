import dill
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.search_engine import PromptSearchEngine


class Query(BaseModel):
    prompt: str
    n: int = 5


app = FastAPI()

with open('../core/engine.pickle', 'rb') as file:
    serialized_engine = file.read()

prompt_search_engine = dill.loads(serialized_engine)


@app.post("/search/")
async def search(query: Query):
    try:
        results = prompt_search_engine.most_similar(query.prompt, query.n)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
