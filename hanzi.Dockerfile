FROM python:3
RUN apt-get update -y
RUN apt-get install -y texlive-full
RUN pip3 install cairosvg