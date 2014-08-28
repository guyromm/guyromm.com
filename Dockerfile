FROM ubuntu:14.04
MAINTAINER Guy Romm <guyromm@gmail.com>
RUN apt-get update && apt-get install -y python python-pip apache2 libapache2-mod-wsgi
RUN pip install Pyramid
RUN mkdir -p /opt
ADD guyromm /opt/guyromm.com
ADD test.ini /opt/
ADD apacheconf /etc/apache2/sites-enabled/