import uvicorn
from fastapi import FastAPI
from typing import List
import classifier
import tokenizer
app = FastAPI()


class input_list():
    text: List[str]
@app.post("/")
def Hackatone(input:input_list):
    result = []
    for news in input:
        buffer = tokenizer.preprocess_text(news)
        buffer = classifier.classify_text(buffer)
        result.append(buffer)
    return result


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)



