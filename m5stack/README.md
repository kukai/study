# M5Stack 学習プロジェクト

M5Stackを使った各種実験・学習プロジェクトです。

## プロジェクト一覧

### [HelloM5Avatar](./HelloM5Avatar/)
M5Stack用Avatarライブラリの基本実装

- **技術スタック**: Arduino C++, M5Avatar
- **機能**: M5Stackに表情豊かなアバターを表示
- **学習内容**: M5Avatarライブラリの基本的な使い方

### [HelloPIO](./HelloPIO/)
PlatformIOを使ったM5Stack開発の基本

- **技術スタック**: Arduino C++, PlatformIO
- **機能**: 基本的なHello World表示
- **学習内容**: PlatformIOでのM5Stack開発環境構築

### [HelloWAV](./HelloWAV/)
M5Stackでの音声ファイル再生実験

- **技術スタック**: Arduino C++, M5Unified
- **機能**: WAVファイル再生、トーン生成、複数ディスプレイ対応
- **学習内容**: M5Stackでの音声処理

### [mpy](./mpy/)
MicroPythonを使ったM5Stack開発実験

- **技術スタック**: MicroPython, UIFlow
- **機能**: 
  - ボタン制御 (upytest01.py)
  - メニューUI (upytest02.py)
  - マイク入力波形表示 (upytest03.py)
- **学習内容**: MicroPythonでのM5Stack制御

### [tool-py](./tool-py/)
M5Stack用音声ファイル生成ツール

- **技術スタック**: Python, NumPy, SciPy
- **機能**: 指定周波数のWAVファイル生成
- **学習内容**: Pythonでの音声ファイル生成

## 開発環境

### Arduino/PlatformIO プロジェクト
- PlatformIO Core
- M5Stack ライブラリ
- M5Avatar ライブラリ (HelloM5Avatar)
- M5Unified ライブラリ (HelloWAV)

### MicroPython プロジェクト
- M5Stack UIFlow
- MicroPython firmware

### Python ツール
```bash
pip install numpy scipy
```

## 使用方法

各プロジェクトディレクトリには個別の設定ファイルが含まれています：

- **Arduino/PlatformIO**: `platformio.ini`で設定済み
- **MicroPython**: UIFlowまたはMicroPython環境で実行
- **Python**: requirements.txtに従ってライブラリをインストール