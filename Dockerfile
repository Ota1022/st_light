FROM ubuntu:20.04

WORKDIR /app

RUN apt-get update && \
  apt-get install -y software-properties-common && \
  add-apt-repository ppa:deadsnakes/ppa && \
  apt-get update && \
  apt-get install -y python3.8 python3.8-distutils python3-pip ffmpeg

RUN python3.8 -m pip install --upgrade pip

COPY requirements.txt .
RUN python3.8 -m pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113 && \
  python3.8 -m pip install -r requirements.txt

COPY . .
