FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY /api .

EXPOSE 8080

CMD ["python3", "wsgi.py"]