FROM alpine

LABEL Name Roland 
LABEL Surname Szarka 
LABEL email roland.szarka.it@gmail.com

RUN apk add python3-dev --no-cache
RUN apk add py3-pip --no-cache
RUN apk add py3-psutil --no-cache
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "app.py"]