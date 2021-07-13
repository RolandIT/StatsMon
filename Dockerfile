FROM alpine
LABEL Name Roland 
LABEL Surname Szarka 
LABEL email roland.szarka.it@gmail.com
RUN apk add python3.8 --no-cache
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD [ "python", "./StatMon.py" ]
COPY src/ .