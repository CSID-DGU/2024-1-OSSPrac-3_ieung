FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install flask

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
