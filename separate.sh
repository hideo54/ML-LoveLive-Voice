members=(HONOKA ELI KOTORI UMI RIN MAKI NOZOMI HANAYO NICO)
songs=(
    'もぎゅっとloveで接近中'
    '愛してるばんざーい'
    'Wonderful-Rush'
    'Oh-Love-and-Peace'
    '僕らは今のなかで'
    'WILD-STARS'
    'きっと青春が聞こえる'
    '輝夜の城で踊りたい'
    'Wonder-zone'
    'No-brand-girls'
    'START-DASH'
)

for member in "${members[@]}"
do
    for song in "${songs[@]}"
    do
        ffmpeg -i "$member/$song.m4a" "$member/$song.wav"
        python rpca_svs/separation.py "$member/$song.wav" \
            "$member/$song-voice.wav" /dev/null
    done
done
for member in "${members[@]}"
do
    ffmpeg -i "$member/もぎゅっとloveで接近中-voice.wav" -ss 15 -t 15 \
        "$member/もぎゅっとloveで接近中-short-voice.wav"
done
