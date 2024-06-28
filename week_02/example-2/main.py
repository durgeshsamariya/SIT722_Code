from fastapi import FastAPI
import uvicorn


app = FastAPI()


# Add about yourself.
about_me = {
    "student_id": 11111111,
    "name": "My Name",
    "unit_code": "SIT722",
    "campus": "My Campus"
}


@app.get("/")
async def root():
    return about_me


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
