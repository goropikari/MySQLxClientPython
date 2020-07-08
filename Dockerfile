FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y ngrep curl python3 ipython3 python3-pip protobuf-compiler python3-protobuf mysql-client && \
    mkdir -p /mysql && \
    cd /mysql && \
    curl -Lo mysql-server.tar.gz https://github.com/mysql/mysql-server/archive/mysql-8.0.20.tar.gz && \
    tar xf mysql-server.tar.gz && \
    cp -r mysql-server-mysql-8.0.20/plugin/x/protocol/protobuf . && \
    rm -rf mysql-* && \
    mkdir lib && \
    protoc -I=protobuf --python_out=lib protobuf/*.proto

COPY sample.py /mysql/sample.py
COPY ex.sql /mysql/ex.sql

ENV PYTHONPATH /mysql/lib
WORKDIR /mysql
