from pytube import YouTube


streams = YouTube('https://www.youtube.com/watch?v=K27hfpW5onU&t=204s').streams
streams.filter(progressive=True, file_extension='mp4').filter(progressive=True, file_extension='mp4').first().download()



import os
for file in os.listdir("."):
    if file.endswith(".mp4"):
        print(os.path.join(".", file))