FROM ubuntu:18.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        unzip \
        wget && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /opt/dana && \
    cd /opt/dana && \
    wget --no-check-certificate https://www.projectdana.com/download/ubu64 -O dana_dist && \
    unzip dana_dist && \
    rm dana_dist && \
    chmod +x dana dnc

ENV DANA_HOME=/opt/dana \
    PATH=$PATH:/opt/dana
