FROM python:3.14.4-slim

WORKDIR /app

COPY requeriments.txt .

RUN pip install --no-cache-dir -r requeriments.txt

COPY . .

CMD ["python", "./src/main.py"]