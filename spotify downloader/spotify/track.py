def track(url,sp):
    track_uri = url.split("/")[-1].split("?")[0]

    track = [f"{sp.track(f'spotify:track:{track_uri}')['name']} {sp.track(f'spotify:track:{track_uri}')['artists'][0]['name']}"]
    print('Getting track!!')
    return track