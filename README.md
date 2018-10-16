# 機械学習でμ’sの声を識別する

コミックマーケット91(2016年冬)の「SunPro会誌 2017」で書いた「機械学習でμ’sの声を識別する」のソースコードです。

コードの内容自体は誌面と同一ですが、改行の仕方は誌面とは異なります。
(誌面では、幅の限られた紙面への掲載という都合上こまめに改行を挟んでいましたが、本リポジトリのコードでは、よほど長くない限り改行していません。)

## 記事

* [Web(hideo54の記事のみ、HTML)](https://sunpro.io/c91/hideo54.html)
* [Web(hideo54の記事のみ、PDF)](https://sunpro.io/c91/hideo54.pdf)
* [Web(HTML, PDF, EPUB, Kindle)](https://booth.pm/ja/items/396886)
* [booth(PDF, EPUB, Kindle)](https://booth.pm/ja/items/396886)
* [SunProの他の作品(PDF等)](https://sunpro.booth.pm/)

## 必要な環境

* Python 3系 (検証済: 3.5.2)
* numpy (言わずと知れた計算お役立ちライブラリ)
* librosa (音声処理用)
* requests (サンプル集める用にAPIを叩く時に使用)
* ffmpeg (音声ファイル変換用)
* scikit-learn (機械学習用)

## 実行方法

1. `python download_sample_music.py`: iTunes APIを利用して試聴用音楽ファイル(.m4a)(99本)をダウンロードします。
1. `./separate.sh`: ffmpegを使って.m4aを.wavに変換した後、音楽ファイルからBGMを除去し、音声のみを抽出します。(-voice.wav)
1. `python learn.py`: 「No brand girls」以外の曲を使って歌手を学習させた後、「No brand girls」の音声を与えて、歌手を推測させ、結果を出力します。
