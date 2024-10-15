'''
Connects LCD to a Pi-Cobbler via a breadboard.
Displays TIME, DATE, and IP Address
https://pimylifeup.com/wp-content/uploads/2016/09/Raspberry-Pi-LCD-16x2-Circuit-Diagram-v1.png
'''
#! /usr/bin/env python
import time, feedparser, random
import RPi.GPIO as GPIO
from RPLCD import CharLCD
from subprocess import Popen, PIPE
from datetime import datetime

GPIO.setwarnings(False)

lcd = CharLCD(
    numbering_mode = GPIO.BOARD,
    cols=16,
    rows=2,
    pin_rs=15,
    pin_e=11,
    pins_data=[22, 18, 16, 12],  #d4, d5, d6, d7 respectively on LCD pinout.
    auto_linebreaks=True)

framebuffer = ['', '']

def find_interface():
    find_device = "ip addr show"
    interface_parse = run_cmd(find_device)
    for line in interface_parse.splitlines():
        if "state UP" in line:
            dev_name = line.split(':')[1]
    return dev_name

def parse_ip():
    find_ip = "ip addr show %s" % interface
    find_ip = "ip addr show %s" % interface
    ip_parse = run_cmd(find_ip)
    for line in ip_parse.splitlines():
        if "inet " in line:
            ip = line.split(' ')[5]
            ip = ip.split('/')[0]
    return ip

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output.decode('ascii')

def write_to_lcd(lcd, framebuffer, num_cols):
    lcd.home()
    for row in framebuffer:
        lcd.write_string(row.ljust(num_cols)[:num_cols])
        lcd.write_string('\r\n')

interface = find_interface()
ip_address = parse_ip()
lcd.clear()

try:
    while True:
        lcd.cursor_mode = 'hide'
        write_to_lcd(lcd, framebuffer, 16)

#display time and IP address
        for i in range(1):
            framebuffer[0] = datetime.now().strftime('%b %d  %H:%M:%S\n')
            framebuffer[1] = ' ' + ip_address
            write_to_lcd(lcd, framebuffer, 16)
            time.sleep(3)

except KeyboardInterrupt:
    lcd.clear()
    GPIO.cleanup()
