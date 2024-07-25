FROM python:3.12

COPY . /app
WORKDIR /app


RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

EXPOSE 8000

CMD ["python3", "main.py"]