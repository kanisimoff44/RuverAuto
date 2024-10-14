FROM python:3.11

RUN mkdir /ruverauto

WORKDIR /ruverauto

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /ruverauto/docke/*.sh