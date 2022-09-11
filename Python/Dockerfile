FROM python:latest

MAINTAINER Sean Jain Ellis <sellis@bandarji.com>

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install pytest
RUN mkdir /99bottles

WORKDIR /99bottles

COPY main.py /99bottles
COPY test_main.py /99bottles
COPY main.sh /99bottles

ENTRYPOINT ["/99bottles/main.sh"]
CMD [""]
