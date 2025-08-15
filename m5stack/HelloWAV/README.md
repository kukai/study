# HelloWAV

M5Stackでの音声ファイル再生とトーン生成の実験プロジェクトです。

## 概要

M5Unifiedライブラリを使用してWAVファイルの再生、トーン生成、複数ディスプレイ対応を実装したプログラムです。

## 機能

- WAVファイル再生（ヘッダー付き・なし両対応）
- トーン生成（周波数可変）
- 複数ディスプレイ対応（ATOM Display, Module Display, Unit LCD等）
- メニューUI操作

## 対応ディスプレイ

- M5AtomDisplay
- M5ModuleDisplay
- M5UnitLCD
- M5UnitOLED

## 音声データ

- `wav_unsigned_8bit_click`: 8bit unsigned 44.1kHz mono（WAVヘッダーなし）
- `wav_with_header`: WAVヘッダー付きデータ

## セットアップ

```bash
# PlatformIOでビルド・書き込み
pio run --target upload
```

## 使用方法

1. プログラム書き込み後、M5Stackが起動
2. メニューから以下の機能を選択可能：
   - トーン再生（周波数可変）
   - BGM再生・停止
   - 各種音声ファイル再生

## 学習ポイント

- M5Unifiedライブラリでの音声処理
- 複数ディスプレイ対応の実装方法
- WAVファイル形式の違いと対応方法
- M5Stackでのメニューシステム実装