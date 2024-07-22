import dill
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Query(BaseModel):
    prompt: str
    n: int = 5


app = FastAPI()

with open("./engine.pickle", "rb") as file:
    serialized_engine = file.read()

prompt_search_engine = dill.loads(serialized_engine)


@app.post("/search/")
async def search(query: Query):
    """
    Find the most similar prompts to a given query prompt using the pre-trained PromptSearchEngine.

    This endpoint accepts a query prompt and returns a specified number of the most similar prompts
    from the corpus. It performs the following steps:
    1. Validates the input types.
    2. Uses the pre-loaded PromptSearchEngine to find the most similar prompts.
    3. Formats the results into a list of dictionaries containing the similarity score and prompt text.

    Args:
        query (Query): The query model containing the prompt text and the number of similar prompts to return.

    Returns:
        List[Dict[str, Union[float, str]]]: A list of dictionaries where each dictionary contains the similarity score and the corresponding prompt.

    Raises:
        HTTPException: If an error occurs during the processing of the query, an HTTP 500 error is raised with the error details.
    """

    try:
        if not isinstance(query.prompt, str):
            raise ValueError("Prompt must be a string")

        if not isinstance(query.n, int):
            raise ValueError("Prompt must be a string")

        results = prompt_search_engine.most_similar(query.prompt, query.n)
        formatted_results = [
            {"score": float(score), "description": desc} for score, desc in results
        ]

        return formatted_results

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
