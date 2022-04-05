FROM python:3.11-rc-bullseye

RUN mkdir /app
ADD . /app
WORKDIR /app
#666
#RUN pip install -r requirements.txt
#CMD ["python", "main.py"]
