FROM python:3.8

ADD task_logic.py .
ADD user_input.py .
ADD main.py .

CMD ["python", "./main.py"]

