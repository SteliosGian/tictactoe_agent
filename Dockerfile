FROM ubuntu

RUN apt-get update && \
    apt-get -y dist-upgrade && \
    apt-get install -y gcc make apt-transport-https ca-certificates build-essential && \
    apt-get install -y --no-install-recommends wget python3-pip libpython3-dev

RUN python3 --version
RUN pip3 --version


WORKDIR /usr/src

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY src .
RUN ls -la .
