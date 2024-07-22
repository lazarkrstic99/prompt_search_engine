from web_server import app
import uvicorn


def run():
    """
    TODO
    """

    uvicorn.run(app, host="0.0.0.0", port=8000)


