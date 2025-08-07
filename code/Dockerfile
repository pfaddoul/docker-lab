FROM python:3.12

WORKDIR /app/code

RUN pip install -r requirements.txt

COPY test.py .

CMD [ "python", "test.py" ]