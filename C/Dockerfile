FROM gcc:latest

MAINTAINER Sean Jain Ellis <sellis@bandarji.com>

RUN mkdir /99bottles

WORKDIR /99bottles

RUN cd /99bottles

COPY main.c /99bottles/

RUN gcc main.c

ENTRYPOINT ["/99bottles/a.out"]
CMD [""]
