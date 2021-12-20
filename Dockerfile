# Docker file for building the required system starting from Ubuntu 20.04 image
FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y curl apt-utils apt-transport-https debconf-utils \
    gcc build-essential libsasl2-dev python-dev libldap2-dev libssl-dev ldap-utils python3-pip \
    netcat net-tools  libpq-dev 

ENV PYTHONUNBUFFERED=1
WORKDIR /appinternships
COPY requirements.txt /reqs/
RUN pip install -r /reqs/requirements.txt
COPY ./ThesisTracker /appinternships
CMD python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8001
