FROM rust:latest

MAINTAINER Sean Jain Ellis <sellis@bandarji.com>

RUN mkdir /99bottles

WORKDIR /99bottles

RUN cd /99bottles && cargo new beer

COPY main.rs /99bottles/beer/src/
COPY main.sh /99bottles/

ENTRYPOINT ["/99bottles/main.sh"]
CMD [""]
