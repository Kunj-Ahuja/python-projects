import pytube as pt
import os
def mp3(link):
    yt = pt.YouTube(link)
    a = yt.streams.filter(only_audio=True)[0].download()
    os.rename(a, a.replace('.mp4','.mp3'))
    print(f'Downloaded: {a}')