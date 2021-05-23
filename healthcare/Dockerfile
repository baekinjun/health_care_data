# Base Image
FROM python:3.8

ENV PYTHONBUFFERED 1

# Set locale
ENV LC_ALL=C.UTF-8
ENV TZ=Asia/Seoul

# Upgrading pip
RUN python -m pip install pip==21.0.1

# Setup Folders
RUN mkdir -p /healthcare

# Move to working directory
WORKDIR /healthcare

COPY requirements.txt .
RUN pip install -r requirements.txt

#코드 복사
COPY . .

CMD ["gunicorn", "-w" ,"2", "-b" ,"0.0.0.0:8000" ,"--access-logfile","-" ,"--timeout=90" ,"-k" ,"gevent","--log-level","debug","server:app"]
