import pandas
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
import classifier
import tokenizer
import json
import pandas as pd


app = FastAPI()

class input_list(BaseModel):
    list: List[str]



@app.post("/uploadcsv/")
def upload_csv(csv_file: UploadFile = File(...)):
    dataframe = pd.read_csv(csv_file.file)
    print(type(dataframe))
    channel_id = dataframe["channel_id"].tolist()
    news = dataframe["text"].tolist()
    result = {}
    labels = []
    refactored_text = []

    for i in range(len(dataframe)):
        buffer = tokenizer.preprocess_text(news[i])
        label = classifier.classify_text(buffer)
        labels.append(label)
        result[channel_id[i]] = {label : news[i]}
    output = {"text": news, "channel_id": channel_id, "category": labels}
    df = pd.DataFrame(output)
    output = df.to_csv("output_Data.csv", index=False)
    file_path = "output_Data.csv"
    response = FileResponse(file_path, media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=downloaded_file.csv"
    return response

# @app.get("/download")
# def download():
#
@app.post("/")
def Hackatone(input:input_list):
    for item in input.list:
        print(item)
        print(type(item))
    result = {}
    for news in input.list:
        buffer = tokenizer.preprocess_text(news)
        label = classifier.classify_text(buffer)
        result[label] = buffer
        print(label, buffer)
    return json.dumps(result)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)


