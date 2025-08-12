FROM ubuntu:latest

RUN apt-get update && apt-get install -y bash coreutils grep sed awk curl && rm -rf /var/lib/apt/lists/*

WORKDIR /task

COPY countword.sh /task/countword.sh
COPY createfile.sh /task/createfile.sh

RUN chmod +x /task/*.sh