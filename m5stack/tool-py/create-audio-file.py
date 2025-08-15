import numpy as np
from scipy.io import wavfile

# パラメータ設定
sample_rate = 16000  # サンプリング周波数 16000Hz
duration = 1  # 音の長さ（秒）
frequency = 440  # 音の高さ（Hz）

# 時間配列の生成
t = np.linspace(0, duration, int(sample_rate * duration), False)

# サイン波の生成
audio = np.sin(2 * np.pi * frequency * t)

# 音量の正規化（-1 から 1 の範囲に）
audio = audio / np.max(np.abs(audio))

# 16ビット整数に変換
audio = (audio * 32767).astype(np.int16)

# WAVファイルとして保存
wavfile.write('test_tone.wav', sample_rate, audio)

print("WAVファイルが生成されました: test_tone.wav")
