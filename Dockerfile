#Dockerfile
#JJ
FROM python:3.12-slim
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --default-timeout=120 --retries 10 -r ./requirements.txt
COPY ./app.py .
COPY ./model ./model
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]

