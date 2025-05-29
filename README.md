# st_light

🎭 **SadTalker を使用したポートレート動画生成ツール**

音声ファイルから口の動きを推定し、静止画像を話している動画に変換するシステムです。Dockerを使用して簡単にセットアップでき、GPU環境での高速推論が可能です。

## ✨ 特徴

- 🖼️ **静止画像から動画生成**: 1枚の顔写真から自然な話している動画を作成
- 🎵 **音声同期**: 音声ファイルに合わせて正確な口の動きを生成
- 🐳 **Docker対応**: 環境構築不要で即座に利用開始
- ⚡ **GPU高速化**: NVIDIA GPU使用時の高速推論をサポート
- 🎯 **簡単操作**: コマンド一つで動画生成

## 📁 プロジェクト構成

```
st_light/
├── 🐳 Docker関連
│   ├── Dockerfile              # コンテナ環境定義
│   ├── docker-compose.yml      # サービス構成
│   └── requirements.txt        # Python依存関係
├── 📂 入出力ディレクトリ
│   ├── input/
│   │   ├── image/              # 入力画像（PNG, JPG）
│   │   └── audio/              # 入力音声（WAV）
│   └── output/                 # 生成動画出力先
├── 🔧 スクリプト
│   ├── scripts/
│   │   └── download_models.sh  # モデルダウンロード
│   ├── generate_video.py       # メイン動画生成スクリプト
│   └── sadtalker.py           # SadTalker実装
└── 🧠 AIモデル・処理部
    └── src/
        ├── audio2exp_models/   # 音声→表情変換
        ├── audio2pose_models/  # 音声→ポーズ変換
        ├── face3d/            # 3D顔モデル処理
        ├── facerender/        # 顔レンダリング
        └── utils/             # ユーティリティ
```

## 🚀 クイックスタート

### 1. 📥 モデルファイルの準備

```bash
bash scripts/download_models.sh
```

### 2. 🏗️ Docker環境のセットアップ

```bash
# イメージをビルド
docker-compose build

# コンテナを起動（バックグラウンド実行）
docker-compose up -d
```

### 3. 🎬 動画生成の実行

```bash
# コンテナに入る
docker-compose exec sadtalker /bin/bash

# 動画生成（コンテナ内で実行）
python3.8 generate_video.py \
  --source_image ./input/image/art_1.png \
  --driven_audio ./input/audio/japanese.wav \
  --result_dir ./output
```

## 💻 使用例とオプション

### 基本的な使用方法

```bash
python3.8 generate_video.py \
  --source_image <画像ファイルのパス> \
  --driven_audio <音声ファイルのパス> \
  --result_dir <出力ディレクトリ>
```

### パラメータ詳細

| パラメータ | 必須 | 説明 | 例 |
|-----------|------|------|-----|
| `--source_image` | ✅ | 変換対象の顔画像 | `./input/image/portrait.png` |
| `--driven_audio` | ✅ | 音声ファイル | `./input/audio/speech.wav` |
| `--result_dir` | ✅ | 出力先ディレクトリ | `./output` |

### サンプル実行結果

このリポジトリに含まれるサンプルデータで生成した動画：  
📹 [サンプル動画](output/generated_video.mp4)

## 🖥️ 動作確認済み環境

### 推奨スペック

| 項目 | 仕様 |
|------|------|
| **GPU** | NVIDIA T4 Tensor Core GPU 以上 |
| **VRAM** | 4GB 以上 |
| **メモリ** | 16GB 以上 |
| **ストレージ** | 50GB 以上の空き容量 |

### 検証済み環境

- **クラウド**: AWS EC2 g4dn.xlarge インスタンス
- **OS**: Ubuntu 20.04 LTS
- **GPU**: NVIDIA T4 Tensor Core GPU × 1
- **メモリ**: 16 GiB
- **ストレージ**: 125 GB NVMe SSD

![実行時の様子](run_screenshot.png)

## 📋 対応ファイル形式

### 入力形式

| 種類 | 形式 | 備考 |
|------|------|------|
| **画像** | `.jpg`, `.png` | 顔が明確に写っている画像を推奨 |
| **音声** | `.wav` | 16kHz, モノラル推奨 |

### 出力形式

| 種類 | 形式 | 備考 |
|------|------|------|
| **動画** | `.mp4` | H.264エンコード |

## 🛠️ トラブルシューティング

### よくある問題

#### GPU関連
```bash
# GPU使用可能か確認
nvidia-smi

# Docker内でGPU認識確認
docker-compose exec sadtalker nvidia-smi
```

#### メモリ不足
```bash
# 使用可能メモリの確認
free -h

# 不要なDockerイメージ削除
docker system prune
```

#### モデルファイルエラー
```bash
# モデルファイルの再ダウンロード
rm -rf checkpoints/
bash scripts/download_models.sh
```

## 🔧 技術仕様

### アーキテクチャ

1. **音声解析**: 音声から感情表現とポーズ情報を抽出
2. **3D顔モデル**: 入力画像から3D顔モデルを構築
3. **アニメーション生成**: 音声情報を基に顔の動きを生成
4. **レンダリング**: 最終的な動画ファイルを出力

### 使用技術

- **深層学習フレームワーク**: PyTorch 1.12.1
- **コンテナ**: Docker & Docker Compose
- **GPU加速**: CUDA 11.3
- **画像処理**: OpenCV, PIL
- **音声処理**: librosa, soundfile

## 📚 関連リンク

- 🔗 **オリジナルプロジェクト**: [SadTalker](https://github.com/OpenTalker/SadTalker)
- 📄 **論文**: [SadTalker: Learning Realistic 3D Motion Coefficients for Stylized Audio-Driven Single Image Talking Face Animation](https://arxiv.org/abs/2211.12194)

## 📄 ライセンス

このプロジェクトは元の [SadTalker](https://github.com/OpenTalker/SadTalker) プロジェクトのライセンスに従います。

---

⭐ **役に立ったらスターをお願いします！**
