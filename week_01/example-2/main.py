from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import uvicorn

some_file_path = "../videos/SampleVideo_1280x720_1mb.mp4"

app = FastAPI()


@app.get("/")
def main():
    def iterfile():
        with open(some_file_path, mode="rb") as file_like:
            yield from file_like
            
    return StreamingResponse(iterfile(), media_type="video/mp4")

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)