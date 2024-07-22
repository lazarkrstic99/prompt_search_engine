from .web_server import app
import uvicorn


def run():
    """
    Start the FastAPI web server using Uvicorn.
    """

    uvicorn.run(app, host="0.0.0.0", port=7860)


