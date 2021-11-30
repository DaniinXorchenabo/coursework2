from os.path import join, split
from typing import Type
import enum

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from arrays import SortedArray, UnsortedArray, ReverseSortedArray, ArrayClassType
from worker import Worker

app = FastAPI()


class ArrayTypeEnum(str, enum.Enum):
    sorted = "sorted"
    unsorted = "unsorted"
    reverse_sorted = "reverse_sorted"


enum_to_array: dict[ArrayTypeEnum, Type[ArrayClassType]] = {
    ArrayTypeEnum.sorted: SortedArray,
    ArrayTypeEnum.unsorted: UnsortedArray,
    ArrayTypeEnum.reverse_sorted: ReverseSortedArray
}


@app.get("/", response_class=FileResponse)
async def get_ui():
    return "public/main.html"


@app.get("/get_graphs_data")
async def get_graphs_data(array_type: ArrayTypeEnum, start: int, end: int, setup_count: int = 10):
    data =  Worker(setup_count).graphs(enum_to_array[array_type], start=start, end=end)
    print(data)
    return {cl.name: val for [val, cl] in data}


app.mount("/public", StaticFiles(directory=join(split(__file__)[0], 'public')), name="static")

if __name__ == "__main__":
    uvicorn.run("web_gui:app", host="localhost", port=9010, reload=True)
