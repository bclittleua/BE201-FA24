'''
Connects LCD to a Pi-Cobbler via a breadboard.
Displays IP Address and Time on first line of LCD.
Trolls r/news sources and randomly scrolls headlines.
'''

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
    pins_data=[22, 18, 16, 12],
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
        d1 = feedparser.parse('https://www.reddit.com/r/news/.rss')
        d2 = feedparser.parse('https://www.reddit.com/r/space/.rss')
        d3 = feedparser.parse('https://www.reddit.com/r/gamernews/.rss')
        d4 = feedparser.parse('https://www.reddit.com/r/worldnews/.rss')

        lcd.cursor_mode = 'hide'
        write_to_lcd(lcd, framebuffer, 16)

#display time and IP address
        for i in range(1):
            framebuffer[0] = datetime.now().strftime('%b %d  %H:%M:%S\n')
            framebuffer[1] = ' ' + ip_address
            write_to_lcd(lcd, framebuffer, 16)
            time.sleep(3)

#US news
        rrn = random.randrange(len(d1.entries))
        intro = '\r                '
        news_string = d1['entries'][rrn]['title']
        full_string = intro + news_string
        for i in range(len(d1['entries'][rrn]['title']) + 18):
            framebuffer[0] = datetime.now().strftime('%b %d  %H:%M:%S\n')
            framebuffer[1] = full_string[i:i+16]
            write_to_lcd(lcd, framebuffer, 16)
            time.sleep(0.2)

#space news
        rrn = random.randrange(len(d2.entries))
        news_string = d2['entries'][rrn]['title']
        full_string = intro + news_string
        for i in range(len(d2['entries'][rrn]['title']) + 18):
            framebuffer[0] = datetime.now().strftime('%b %d  %H:%M:%S\n')
            framebuffer[1] = full_string[i:i+16]
            write_to_lcd(lcd, framebuffer, 16)
            time.sleep(0.2)

#gamer news
        rrn = random.randrange(len(d3.entries))
        news_string = d3['entries'][rrn]['title']
        full_string = intro + news_string
        for i in range(len(d3['entries'][rrn]['title']) + 18):
            framebuffer[0] = datetime.now().strftime('%b %d  %H:%M:%S\n')
            framebuffer[1] = full_string[i:i+16]
            write_to_lcd(lcd, framebuffer, 16)
            time.sleep(0.2)

#world news
        rrn = random.randrange(len(d4.entries))
        news_string = d4['entries'][rrn]['title']
        full_string = intro + news_string
        for i in range(len(d4['entries'][rrn]['title']) + 18):
            framebuffer[0] = datetime.now().strftime('%b %d  %H:%M:%S\n')
            framebuffer[1] = full_string[i:i+16]
            write_to_lcd(lcd, framebuffer, 16)
            time.sleep(0.2)

except KeyboardInterrupt:
    lcd.clear()
    GPIO.cleanup()
