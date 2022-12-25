from spotify import playlist,track,sp,download

url = input('Enter spotify url: ')
tracks = playlist(url,sp) if 'playlist' in url else track(url,sp)

if __name__ == '__main__':
    download(tracks)