import dill
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# from ..core.search_engine import PromptSearchEngine


class Query(BaseModel):
    prompt: str
    n: int = 5


app = FastAPI()

with open('./engine.pickle', 'rb') as file:
    serialized_engine = file.read()

prompt_search_engine = dill.loads(serialized_engine)


@app.post("/search/")
async def search(query: Query):
    """
    TODO
    """

    try:
        if not isinstance(query.prompt, str):
            raise ValueError("Prompt must be a string")

        if not isinstance(query.n, int):
            raise ValueError("Prompt must be a string")

        results = prompt_search_engine.most_similar(query.prompt, query.n)
        formatted_results = [{"score": float(score), "description": desc} for score, desc in results]

        return formatted_results

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
