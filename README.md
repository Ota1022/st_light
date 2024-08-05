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

2. Docker環境を構築します。

```sh
docker-compose up
```

3. Dockerコンテナに入ります。
```sh
docker-compose exec sadtalker /bin/bash
```

## 使用例

次のコマンドを実行して動画を生成します。

```sh
python3.8 generate_video.py --source_image ./input/image/art_1.png --driven_audio ./input/audio/japanese.wav --result_dir ./results
```

## 対応ファイル形式

- 画像: .jpg, .png
- 音声: .wav
- 動画出力: .mp4
