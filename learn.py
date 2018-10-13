import scipy.io.wavfile as wav
import librosa
from sklearn.svm import SVC
import numpy

def getMfcc(filename):
    y, sr = librosa.load(filename)
    return librosa.feature.mfcc(y=y, sr=sr)

artists = ['HONOKA', 'ELI', 'KOTORI', 'UMI', 'RIN', 'MAKI', 'NOZOMI', 'HANAYO', 'NICO']
songs = [
    'もぎゅっとloveで接近中-short',
    '愛してるばんざーい',
    'Wonderful-Rush',
    'Oh-Love-and-Peace',
    '僕らは今のなかで',
    'WILD-STARS',
    'きっと青春が聞こえる',
    '輝夜の城で踊りたい',
    'Wonder-zone',
    'START-DASH'
]

song_training = []
artist_training = []
for artist in artists:
    print('Reading data of %s...' % artist)
    for song in songs:
        mfcc = getMfcc('%s/%s-voice.wav' % (artist, song))
        song_training.append(mfcc.T)
        label = numpy.full((mfcc.shape[1], ), artists.index(artist), dtype=numpy.int)
        artist_training.append(label)
song_training = numpy.concatenate(song_training)
artist_training = numpy.concatenate(artist_training)

clf = SVC(C=1, gamma=1e-4)
clf.fit(song_training, artist_training)
print('Learning Done')

counts = []

for artist in artists:
    mfcc = getMfcc('%s/No-brand-girls-voice.wav' % artist)
    prediction = clf.predict(mfcc.T)
    counts.append(numpy.bincount(prediction))

counts = numpy.vstack(counts)

for artist, count in zip(artists, counts):
    result = artists[numpy.argmax( count - count.mean(axis=0) )]
    original_title = 'No brand girls(%s Mix)' % artist
    print('%s recognized as sung by %s.' % (original_title, result))
