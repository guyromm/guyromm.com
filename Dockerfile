FROM ubuntu:14.04
MAINTAINER Guy Romm <guyromm@gmail.com>
RUN apt-get update && apt-get install -y python python-pip
RUN pip install Pylons
ADD guyromm /guyromm
ADD cfg /cfg
RUN python cfg/setup.py develop
EXPOSE 5000
CMD paster serve /cfg/production.ini 