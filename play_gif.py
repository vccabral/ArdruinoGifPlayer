from PIL import Image
from neopixel import *
from itertools import product

# LED strip configuration:
LED_COUNT      = 750      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

im = Image.open("giphy.gif")

frame_count = 0
try:
    while 1:
        im.seek(im.tell()+1)
        resized = im.resize((30,30)).convert('RGB')

        for x in range(0, resized.size[0]):
            for y in range(0, resized.size[1]):
                location = (x,y)
                color = im.getpixel(location)
                strip.setPixelColor(i, color)
        strip.show()

except EOFError:
    pass # end of sequence

