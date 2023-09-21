FROM python:3.11

WORKDIR /hackatone

COPY requirements.txt .
COPY ./src ./src

RUN pip install -r requirements.txt

CMD ["python", "/hackatone/src/main.py"]