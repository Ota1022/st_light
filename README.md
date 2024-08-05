# sd_light

Dockerを使用してSadTalkerモデルを設定し、画像と音声ファイルから動画を生成します。

## ファイル構成

```
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── scripts
│   └── download_models.sh
├── input
│   ├── image
│   │  └── art_1.png
│   └── audio
│      └── japanese.wav
├── output
├── src
│   ├── audio2exp_models
│   ├── audio2pose_models
│   ├── face3d
│   ├── facerender
│   ├── utils
│   ├── generate_batch.py
│   ├── generate_facerender_batch.py
│   └── test_audio2coeff.py
├── sadtalker.py
└── generate_video.py

```

## セットアップ

1. 必要なモデルファイルをダウンロードし、`models`ディレクトリに配置します。

```sh
bash scripts/download_models.sh
```

2. Dockerイメージをビルドし、コンテナを実行します。

```sh
docker-compose up --build
```

## 使用方法

Dockerコンテナ内でスクリプトを実行します。

```sh
docker-compose run app python generate_video.py input/image/art_1.jpg input/audio/japanese.wav output/video.mp4
```

## 対応ファイル形式

- 画像: .jpg, .png
- 音声: .wav
- 動画出力: .mp4
