from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Your dictionary of items (replace with your actual data)
items = [
    {"name": "Item 1", "description": "Some description"},
    {"name": "Item 2", "description": "Another description"},
    # Add more items as needed
]

@app.get("/items", response_class=HTMLResponse)
async def read_items(request: Request):
    # Render the HTML template with the dictionary values
    return templates.TemplateResponse("items.html", {"request": request, "items": items})


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
