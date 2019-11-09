import spotipy

client = spotipy.Spotify()

def doSth():
    results = client.search(q='artist:'+'Victoria Justice', type='artist')
    print(results)