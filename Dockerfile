FROM python:3.7

RUN mkdir /opt/sfia1/

COPY . /opt/sfia1/

WORKDIR /opt/sfia1/

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]