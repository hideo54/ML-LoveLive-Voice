import os
import requests

artists = ['HONOKA', 'ELI', 'KOTORI', 'UMI', 'RIN', 'MAKI', 'NOZOMI', 'HANAYO', 'NICO']
songs = [
    ['もぎゅっと"love"で接近中!', 'もぎゅっとloveで接近中'],
    ['愛してるばんざーい!', '愛してるばんざーい'],
    ['Wonderful Rush', 'Wonderful-Rush'],
    ['Oh,Love&Peace!', 'Oh-Love-and-Peace'],
    ['僕らは今のなかで', '僕らは今のなかで'],
    ['WILD STARS', 'WILD-STARS'],
    ['きっと青春が聞こえる', 'きっと青春が聞こえる'],
    ['輝夜の城で踊りたい', '輝夜の城で踊りたい'],
    ['Wonder zone', 'Wonder-zone'],
    ['No brand girls', 'No-brand-girls'],
    ['START:DASH!!', 'START-DASH']
]

def download(url, filename):
    res = requests.get(url, timeout=10)
    with open(filename, 'wb') as f:
        f.write(res.content)

timeouts = []

for artist in artists:
    os.mkdir(artist)
    for song in songs:
        print('Downloading: %s(%s Mix)' % (song[0], artist))
        baseurl = 'https://itunes.apple.com/search'
        params = {
            'term': '%s(%s Mix)' % (song[0], artist),
            'country': 'JP',
            'media': 'music',
            'entry': 'song'
        }
        res = requests.get(baseurl, params=params)
        result = res.json()['results'][0]
        previewUrl = result['previewUrl']
        try:
            download(previewUrl, '%s/%s.m4a' % (artist, song[1]))
        except requests.exceptions.ReadTimeout:
            print('Timeout: %s(%s Mix)' % (song[0], artist))
            timeouts.append({
                'url': previewUrl,
                'song': song,
                'artist': artist
            })

for timeout in timeouts:
    url = timeout['url']
    original_title = timeout['song'][0]
    short_title = timeout['song'][1]
    artist = timeout['artist']
    print('Downloading again: %s(%s Mix)' % (original_title, artist))
    try:
        song = download(url, '%s/%s.m4a' % (artist, short_title))
    except requests.exceptions.ReadTimeout:
        print('Timeout again, download manually: ' + timeout['url'])
