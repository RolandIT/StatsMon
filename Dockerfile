FROM alpine

LABEL Name Roland 
LABEL Surname Szarka 
LABEL email roland.szarka.it@gmail.com

RUN apk add python3-dev --no-cache
RUN apk add py3-pip --no-cache
RUN apk add py3-psutil --no-cache
RUN apk add git --no-cache
RUN git clone https://github.com/RolandIT/StatsMon.git
RUN pip install -r StatsMon/requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "StatsMon/src/app.py"]