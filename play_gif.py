from PIL import Image
from neopixel import *
from itertools import product
import sys

# LED strip configuration:
LED_COUNT      = int(sys.argv[1])      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
DOWNLED = int(sys.argv[2])

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

def zig_zagged_line_to_plane(n):
    y = n // 30
    if (n // 30) % 2 == 0:
        return (y, n - y * 30)
    else:
        return (y, 29 - (n - y * 30))

def plane_to_zig_zagged_line(x,y):
    if y % 2 == 1:
        return x + y * 30
    else:
        return y * 30 + (30 - x)

while True:
    im = Image.open("giphy.gif")
    try:
        while 1:
            im.seek(im.tell()+1)
            resized = im.resize((30,30)).convert('RGB')

            for x in range(0, resized.size[0]):
                for y in range(0, resized.size[1]):
                    r, g, b = resized.getpixel((x, y))
                    strip.setPixelColor(plane_to_zig_zagged_line(x, y), Color(r//DOWNLED, g//DOWNLED, b//DOWNLED))
            strip.show()

    except EOFError:
        pass # end of sequence

