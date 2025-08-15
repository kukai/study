from m5stack import *
from m5ui import *
from uiflow import *

def button_A_wasPressed():
  lcd.clear()
  lcd.print("Button A Pressed", 0, 0, 0xFFFFFF)

def button_B_wasPressed():
  lcd.clear()
  lcd.print("Button B Pressed", 0, 0, 0x00FF00)

def button_C_wasPressed():
  lcd.clear()
  lcd.print("Button C Pressed", 0, 0, 0x0000FF)

setScreenColor(0x111111)
lcd.setTextColor(0xFFFFFF, 0x111111)

while True:
  if btnA.wasPressed():
    button_A_wasPressed()
  if btnB.wasPressed():
    button_B_wasPressed()
  if btnC.wasPressed():
    button_C_wasPressed()
  wait_ms(2)
