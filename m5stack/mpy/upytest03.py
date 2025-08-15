import machine
from m5stack import *
from m5ui import *
from uiflow import *

def micro_start():
    lcd.clear(lcd.BLACK)
    adc = machine.ADC(34)
    adc.atten(adc.ATTN_11DB)
    buffer = [0] * 320
    return {'adc': adc, 'buf': buffer}

def micro_loop(obj):
    adc = obj['adc']
    buffer = obj['buf']
    
    # 新しい値を読み取り
    val = 0
    for _ in range(32):
        raw = adc.read() - 1845
        val += raw
    val = val // 32
    
    # 値を増幅して見やすくする
    val = val // 5

    # バッファを更新
    buffer.pop()
    buffer.insert(0, val)

    # 波形を描画（矩形で前回の波形を消去）
    lcd.fillRect(0, 0, 320, 240, lcd.BLACK)  # 描画領域を黒で塗りつぶす
    
    for i in range(319):
        y1 = 120 - buffer[i]
        y2 = 120 - buffer[i + 1]
        y1 = max(0, min(y1, 239))  # Y座標を画面内に制限
        y2 = max(0, min(y2, 239))
        lcd.line(i, y1, i + 1, y2, lcd.WHITE)

# メインの実行部分
obj = micro_start()
while True:
    micro_loop(obj)
    wait_ms(10)
