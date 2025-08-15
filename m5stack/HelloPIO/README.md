# HelloPIO

PlatformIOを使ったM5Stack開発の基本例です。

## 概要

PlatformIO環境でのM5Stack開発の基本的な「Hello World」プログラムです。

## 機能

- M5Stackの画面に「Hello World」と「PlatformIO Macintosh」を表示
- M5Stack開発の基本的な構成

## 必要なライブラリ

- M5Stack (v0.4.6)
- ESP32 Lite Pack Library (v1.3.2)

## セットアップ

```bash
# PlatformIOでビルド
pio run

# M5Stackに書き込み
pio run --target upload
```

## 設定ファイル

`platformio.ini`で以下が設定済み：
- ターゲットボード: m5stack-core-esp32
- プラットフォーム: espressif32
- フレームワーク: arduino

## 学習ポイント

- PlatformIOでのM5Stack開発環境構築
- 基本的なM5Stack APIの使用方法
- Arduino フレームワークでのESP32開発