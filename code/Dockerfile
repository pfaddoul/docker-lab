FROM python:3.12

WORKDIR /app/code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY test.py .

CMD [ "python", "test.py" ]