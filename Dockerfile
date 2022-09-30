FROM ubuntu:latest

RUN apt-get update \  
&& apt-get install cron -y && apt-get install vim -y

RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt
RUN python3 -m pip install requests

#*/3 * * * * python3 ./home/tplink-app.py >> ./TPLINK_OUTPUT.txt

COPY ./ ./home

#CMD python3 ./home/tplink-app.py

