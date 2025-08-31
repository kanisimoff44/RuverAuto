FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /ruverauto
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod a+x /ruverauto/docker/*.sh