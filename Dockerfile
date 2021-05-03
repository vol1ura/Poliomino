FROM python:3.9-alpine

WORKDIR /app
COPY requirements.txt ./

RUN apk update && \
    apk add --virtual build-dep build-base && \
    pip install -r requirements.txt && \
    apk del build-dep

COPY . .

CMD ["python", "example1.py"]