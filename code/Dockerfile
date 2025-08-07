FROM python:3.12

WORKDIR /app/code

RUN pip install websocket-client

COPY test.py .

CMD [ "python", "test.py" ]