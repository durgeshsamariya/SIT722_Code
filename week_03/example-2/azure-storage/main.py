# pip install azure-storage-blob
import os
import io
import uvicorn
from azure.storage.blob import BlobServiceClient
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse

app = FastAPI()

# PORT, VIDEO_STORAGE_HOST and VIDEO_STORAGE_PORT are defined in docker-compose. 
# VIDEO_STORAGE_HOST is container name of azure-storage microservice and 
# VIDEO_STORAGE_PORT is porn for azure-storage microservice.
PORT = os.environ["PORT"]
AZURE_STORAGE_ACCOUNT_NAME = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
AZURE_STORAGE_ACCOUNT_KEY = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")


blob_service_client = BlobServiceClient(
    account_url=f"https://{AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net",
    credential=AZURE_STORAGE_ACCOUNT_KEY
)
container_name = "videos"
container_client = blob_service_client.get_container_client(container_name)


@app.get("/video/{video_path}/")
async def main(video_path: str):
    blob_client = container_client.get_blob_client(video_path)
    if not blob_client.exists():
        raise HTTPException(status_code=404, detail="Video not found")
    stream = blob_client.download_blob().readall()
    return StreamingResponse(io.BytesIO(stream), media_type="video/mp4")
    

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=int(PORT))
