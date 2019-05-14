FROM python:3.7-slim

RUN python -m pip install --upgrade pip

COPY . /web/app
COPY requirements.txt /web/app/requirements.txt
COPY cmd.sh /app

RUN python -m pip install -r /web/app/requirements.txt

WORKDIR /web/app/src

CMD ["cmd.sh"]
