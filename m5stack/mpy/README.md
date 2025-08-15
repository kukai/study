# MicroPython M5Stack実験

M5StackでMicroPython（UIFlow）を使った各種実験です。

## プログラム一覧

### upytest01.py - ボタン制御基本
基本的なボタン制御プログラム

**機能:**
- ボタンA/B/C押下でそれぞれ異なる色のメッセージを表示
- 基本的なイベント駆動プログラミング

**学習内容:**
- MicroPythonでのボタン入力処理
- LCD表示制御
- イベントハンドラーの実装

### upytest02.py - メニューUI
シンプルなメニューシステム

**機能:**
- ボタンA/C: メニュー選択（上下移動）
- ボタンB: 選択実行
- 選択中の項目をハイライト表示

**学習内容:**
- メニューシステムの実装
- 状態管理
- UIデザインパターン

### upytest03.py - マイク入力波形表示
リアルタイム音声波形表示

**機能:**
- ADC（34番ピン）からマイク入力を取得
- リアルタイムで波形を画面に描画
- 32回平均化によるノイズ除去
- 増幅処理で波形を見やすく調整

**学習内容:**
- ADC（Analog-to-Digital Converter）の使用
- リアルタイムデータ処理
- グラフィック描画
- デジタル信号処理基礎

## セットアップ

### 1. UIFlow環境
1. M5StackにUIFlowファームウェアをインストール
2. ブラウザまたはUIFlowアプリでコードを編集
3. M5Stackにプログラムを転送

### 2. MicroPython環境
```bash
# MicroPythonファームウェアのインストール
esptool.py --chip esp32 erase_flash
esptool.py --chip esp32 write_flash -z 0x1000 firmware.bin

# プログラムの転送
ampy -p /dev/ttyUSB0 put upytest01.py main.py
```

## 必要なライブラリ

- m5stack
- m5ui  
- uiflow
- machine（upytest03.pyのみ）

## 学習ポイント

- MicroPythonでのハードウェア制御
- リアルタイム処理の実装
- ユーザーインターフェース設計
- 信号処理とデータ可視化