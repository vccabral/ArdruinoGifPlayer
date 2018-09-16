import os
import random

pixels = ""
for file in os.listdir("."):
    if file.endswith(".mp4"):
        mp4 = os.path.join(".", file)


        for i in range(750):
            pixels = pixels + "10,1,1"+","

        for i in range(750):
            pixels = pixels + "2,10,2"+","

        for i in range(750):
            pixels = pixels + "3,3,10"+","

print(pixels[:-1])