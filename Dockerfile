FROM python:3.9-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app1.py .
COPY app2.py .

ARG APP=app1
ENV APP=$APP

EXPOSE 5001 5002

CMD ["sh", "-c", "python ${APP}.py"]
