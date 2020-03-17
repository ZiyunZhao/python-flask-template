FROM openfaas/of-watchdog:0.7.2 as watchdog
#FROM python:3.7-alpine
FROM ubuntu:latest

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

#ARG ADDITIONAL_PACKAGE
# Alternatively use ADD https:// (which will not be cached by Docker builder)
#RUN apk --no-cache add ${ADDITIONAL_PACKAGE}


#ADDED:
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt update
RUN apt install -y git

# Add non root user
#RUN addgroup -S app && adduser app -S -G app
#RUN chown app /home/app

#USER app

ENV PATH=$PATH:/home/app/.local/bin

WORKDIR /home/app/


RUN git clone https://github.com/tensorflow/nmt.git


COPY index.py           .
COPY requirements.txt   .
#USER root
RUN pip install -r requirements.txt
#USER app

RUN mkdir -p function
RUN touch ./function/__init__.py
WORKDIR /home/app/function/
COPY function/requirements.txt	.
RUN pip install --user -r requirements.txt

WORKDIR /home/app/

#USER root
COPY function   function
#RUN chown -R app:app ./
#USER app

# Set up of-watchdog for HTTP mode
ENV fprocess="python index.py"
ENV cgi_headers="true"
ENV mode="http"
ENV upstream_url="http://127.0.0.1:5000"

HEALTHCHECK --interval=5s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
