FROM python:3.8-slim

WORKDIR /opt/w

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src /opt/w/src

CMD python3