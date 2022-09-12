FROM golang:latest

MAINTAINER Sean Jain Ellis <sellis@bandarji.com>

RUN mkdir /99bottles

WORKDIR /99bottles

COPY main.go /99bottles
COPY main_test.go /99bottles
COPY main.sh /99bottles

RUN cd /99bottles && go mod init beerbottles && go mod tidy

ENTRYPOINT ["/99bottles/main.sh"]
CMD [""]
