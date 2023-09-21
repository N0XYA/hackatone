<<<<<<< HEAD
FROM python:3.10

WORKDIR /hackatone

COPY requirements.txt .
COPY ./src ./src

RUN pip install -r requirements.txt

CMD ["python", "/hackatone/src/main.py"]
=======
FROM python:3

ADD print_csv.py .
ADD data.csv .

RUN pip install pandas

CMD ["python", "./print_csv.py"]
>>>>>>> 2e38e0f (фвфывф)
