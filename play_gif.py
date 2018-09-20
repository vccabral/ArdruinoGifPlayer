from PIL import Image
# from neopixel import *
from itertools import product

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

