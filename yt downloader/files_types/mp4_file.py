import pytube as pt
import os
def mp4(link):
    yt = pt.YouTube(link)
    yt.streams.get_highest_resolution().download()
    print('Downloaded')