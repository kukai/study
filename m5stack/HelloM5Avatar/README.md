# HelloM5Avatar

M5Stack用Avatarライブラリの基本実装例です。

## 概要

M5Avatarライブラリを使用してM5Stackの画面に表情豊かなアバターを表示するプログラムです。

## 機能

- M5Stackの画面にアバターを表示
- 表情や動きは自動的に変化
- 別スレッドでの描画更新

## 必要なライブラリ

- M5Unified
- M5Avatar

## セットアップ

1. PlatformIOまたはArduino IDEを使用
2. 必要なライブラリをインストール
3. M5Stackに書き込み

## 使用方法

```bash
# PlatformIOの場合
pio run --target upload
```

プログラムを書き込むと、M5Stackの画面にアバターが表示され、自動的に表情や動きが変化します。

## 学習ポイント

- M5Avatarライブラリの基本的な使い方
- M5Stackでのグラフィック表示
- マルチスレッド処理（描画は別スレッドで実行）