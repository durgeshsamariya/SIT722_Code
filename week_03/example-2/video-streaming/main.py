import os
import requests
import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

# PORT, VIDEO_STORAGE_HOST and VIDEO_STORAGE_PORT are defined in docker-compose. 
# VIDEO_STORAGE_HOST is container name of azure-storage microservice and 
# VIDEO_STORAGE_PORT is porn for azure-storage microservice.
PORT = os.environ["PORT"]
VIDEO_STORAGE_HOST = os.environ["VIDEO_STORAGE_HOST"]
VIDEO_STORAGE_PORT = os.environ["VIDEO_STORAGE_PORT"]

@app.get("/")
async def forward_video_request():
    # Video path is hard-coded for now
    video_path = "/video/SampleVideo_1280x720_1mb.mp4"
    res = requests.get(f"http://{VIDEO_STORAGE_HOST}:{VIDEO_STORAGE_PORT}{video_path}", stream=True)

    # Stream the video content
    return StreamingResponse(res.raw, media_type="video/mp4")

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=int(PORT))
