import uvicorn
from fastapi import FastAPI
import print_csv
from pydantic import BaseModel
from typing import List, Optional
app = FastAPI()

responce = print_csv.p_head()


class Input(BaseModel):
    test: List[str]

@app.post("/")
def input(inp:Input):
    return inp
@app.get("//")
def second():
    return responce


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")