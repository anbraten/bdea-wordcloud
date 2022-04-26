FROM mcr.microsoft.com/vscode/devcontainers/python:3.8

RUN apt update && apt install -y default-jdk

WORKDIR /workspace

COPY ./requirements.txt /workspace/

RUN ls -la

RUN pip install -r ./requirements.txt
