from m5stack import *
from m5ui import *
from uiflow import *

options = ['A', 'B', 'C']
current_index = 0

def draw_menu():
    lcd.clear()
    for i, option in enumerate(options):
        if i == current_index:
            lcd.print('> ' + option, 10, 20 + i * 30, 0xFFFFFF)
        else:
            lcd.print('  ' + option, 10, 20 + i * 30, 0xAAAAAA)

def button_A_wasPressed():
    global current_index
    current_index = (current_index - 1) % len(options)
    draw_menu()

def button_B_wasPressed():
    lcd.clear()
    lcd.print("Selected: {}".format(options[current_index]), 10, 100, 0x00FF00)

def button_C_wasPressed():
    global current_index
    current_index = (current_index + 1) % len(options)
    draw_menu()

setScreenColor(0x111111)
lcd.setTextColor(0xFFFFFF, 0x111111)

draw_menu()

while True:
    if btnA.wasPressed():
        button_A_wasPressed()
    if btnB.wasPressed():
        button_B_wasPressed()
    if btnC.wasPressed():
        button_C_wasPressed()
    wait_ms(2)
