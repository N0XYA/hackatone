FROM python:3

ADD print_csv.py .
ADD data.csv .

RUN pip install pandas

CMD ["python", "./print_csv.py"]