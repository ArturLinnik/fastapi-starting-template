import uvicorn

from app.main import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("run:app", host="localhost", port=8000, reload=True)
