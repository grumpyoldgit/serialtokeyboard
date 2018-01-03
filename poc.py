#!/usr/bin/python

import keyboard
import serial
import hexdump

ser = serial.Serial('COM1', 9600, timeout=1) # blocking for now as my messages happen to be 9 chars wide

# left is 0x4C 0x46
# right is 0x52 0x49
# up is 0x55 0x50
# down is 0x44 0x4e
# ok is 0x4f 0x4b
# cancel is 0x43 0x43
# coin is SC which is 0x53 0x43

left = [0x4C, 0x46, "left", "Left"]
right = [0x52, 0x49, "right", "Right"]
up = [0x55, 0x50, "up", "Up"]
down = [0x44, 0x4e, "down", "Down"]
ok = [0x4f, 0x4b, "ok", "Ctrl"]
cancel = [0x43, 0x43, "cancel", "Alt"]
coin = [0x53, 0x43, "COIN!!!", "5"]

commands = [up, down, left, right, ok, cancel, coin]

while True:
  data = ser.read(9)
  hexdump.hexdump(data)
  for command in commands:
    if data:
      if command[0] == data[1] and command[1] == data[2]:
        print (command[2])
        keyboard.press_and_release(command[3])
