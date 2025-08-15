# M5Stack音声ファイル生成ツール

M5Stack用の音声ファイルを生成するPythonツールです。

## 概要

指定した周波数のサイン波を生成してWAVファイルとして保存します。M5Stackでの音声実験用のテストファイル作成に使用できます。

## 機能

- 指定周波数（デフォルト440Hz）のサイン波生成
- 16000Hzサンプリングレート（M5Stack最適化）
- 16bit WAVファイル出力
- 音量正規化処理

## 必要なライブラリ

```bash
pip install numpy scipy
```

または

```bash
pip install -r requirements.txt
```

## 使用方法

```bash
python create-audio-file.py
```

実行すると`test_tone.wav`ファイルが生成されます。

## 設定可能パラメータ

```python
sample_rate = 16000  # サンプリング周波数
duration = 1         # 音の長さ（秒）
frequency = 440      # 音の高さ（Hz）
```

これらの値を変更することで、異なる音声ファイルを生成できます。

## 出力ファイル

- **test_tone.wav**: 440Hz、1秒間のサイン波
- 16bit PCM、16000Hz サンプリングレート
- M5Stackで再生可能な形式

## 学習ポイント

- NumPyでのデジタル信号生成
- SciPyでの音声ファイル処理
- M5Stack用音声形式の理解
- WAVファイル形式の基礎