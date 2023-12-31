## Install dependencies
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip

COPY . /
    
RUN make install