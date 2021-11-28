from os.path import join, split

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/", response_class=FileResponse)
async def get_ui():
    return "public/main.html"

app.mount("/public", StaticFiles(directory=join(split(__file__)[0], 'public')), name="static")

if __name__ == "__main__":
    uvicorn.run("web_gui:app", host="localhost", port=9010, reload=True)
