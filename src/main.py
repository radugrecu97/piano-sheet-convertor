from uvicorn import run
from api import app

if __name__ == "__main__":
    run("main:app", host="127.0.0.1", port=8000, reload=True)
