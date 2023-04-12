# Builder
FROM python:3.8-slim as builder

COPY ./requirements.txt ./

RUN apt update
RUN apt install -y --no-install-recommends build-essential
RUN pip3 install --user -r requirements.txt

# Executor
FROM python:3.8-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY ./fan.py ./

CMD ["python", "-u", "./fan.py"]
