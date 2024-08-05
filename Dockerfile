FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
  apt-get install -y python3.8 python3.8-distutils ffmpeg && \
  python3.8 -m pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113 && \
  python3.8 -m pip install -r requirements.txt

COPY . .
