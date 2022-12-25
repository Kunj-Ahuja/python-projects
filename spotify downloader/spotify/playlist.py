def playlist(url,sp):
    playlist_URI = url.split("/")[-1].split("?")[0]

    tracks = []
    print('Getting tracks!!')
    for track in sp.playlist_tracks(playlist_URI)["items"]:
        track_name = track["track"]["name"]
        artist_name = track["track"]["artists"][0]["name"]
        tracks.append(track_name + ' ' + artist_name)

    return tracks