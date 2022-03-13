FROM python:3.8-alpine

ADD main.py .
ADD task_logic.py .
ADD text .

CMD ["python", "./main.py"]

