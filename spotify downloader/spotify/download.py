import os
import pytube as pt
from youtubesearchpython import VideosSearch
def download(tracks):
    links=[]
    print('Getting track(s) link!!')
    for i in tracks:
        videosSearch = VideosSearch(i) 
        if len(videosSearch.result()['result']) < 1:
            pass
        links.append(videosSearch.result()['result'][0]['link'])

        print(f'Total track(s): {len(links)}')

        for link in links:
            yt = pt.YouTube(link)
            t = yt.streams.filter(only_audio=True)
            a = t[0].download()
            os.rename(a, a.replace('.mp4','.mp3'))
            print(f'{links.index(link)+1} : {t[0].title} : Downloaded')