FROM python:3.11

WORKDIR /apex

COPY . /apex

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
