FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
COPY . /mysql
RUN apt-get update && \
    apt-get install -y ngrep curl python3 ipython3 python3-pip protobuf-compiler python3-protobuf mysql-client

# Compile *.proto files
# RUN cd /mysql && \
#     protoc -I=protobuf --python_out=lib protobuf/*.proto

ENV PYTHONPATH /mysql/lib
WORKDIR /mysql
