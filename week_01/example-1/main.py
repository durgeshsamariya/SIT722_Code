from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return "Hello, Welcome to SIT722!"


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)