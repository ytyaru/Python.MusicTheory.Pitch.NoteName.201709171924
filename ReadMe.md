# このソフトウェアについて

MIDIノート名からMIDIノート番号を取得する。

`A#4`→`70`のように変換する。

octaveは国際式とYAMAHA式の2種類ある。

国際式|YAMAHA式|最低値0式
------|--------|---------
-1〜9|-2〜8|0〜10

左から順に一般的。国際式が最も普及していると思われる。88鍵盤MIDIキーボードの最低音が`A0`になる（負数にならない）ようにしているらしい。

## 前回まで

* https://github.com/ytyaru/Python.MusicTheory.Chord.Triad.201709071957
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709131752
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709131811
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709132015
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709132015
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709141450
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709141657
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709171254
* https://github.com/ytyaru/Python.MusicTheory.Pitch.Key.201709171300
* https://github.com/ytyaru/Python.MusicTheory.Pitch.NoteNumber.201709171322

# 実行

```sh
$ cd ./src/
$ python TestNoteName.py
```

テストコード|項目数
------------|------
TestPitchClass.py|13
TestAccidental.py|9
TestDegree.py|13
TestInterval.py|16
TestKey.py|7
TestNoteNumber.py|11
TestNoteName.py|12

計81項目。

# 課題

* 各国のKey名を取得したい
* メッセージに統一性を持たせたい
* メッセージを国際化したい
    * 自然言語用と音楽理論用語用の2種類

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [libav](http://ytyaru.hatenablog.com/entry/2018/08/24/000000)
    * [各コーデック](http://ytyaru.hatenablog.com/entry/2018/08/23/000000)
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1
        * [pydub](http://ytyaru.hatenablog.com/entry/2018/08/25/000000)
        * [PyAudio](http://ytyaru.hatenablog.com/entry/2018/07/27/000000) 0.2.11
            * [ALSA lib pcm_dmix.c:1022:(snd_pcm_dmix_open) unable to open slave](http://ytyaru.hatenablog.com/entry/2018/07/29/000000)
        * [matplotlib](http://ytyaru.hatenablog.com/entry/2018/07/22/000000)
            * [matplotlibでのグラフ表示を諦めた](http://ytyaru.hatenablog.com/entry/2018/08/05/000000)

# 参考

感謝。

## Python

### 定数

* http://fakatatuku.hatenablog.com/entry/2015/03/26/233024

### サイン波のスピーカ再生

* http://www.non-fiction.jp/2015/08/17/sin_wave/
* http://aidiary.hatenablog.com/entry/20110607/1307449007
* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442

## 音楽理論

### 和音

* https://ja.wikipedia.org/wiki/%E5%92%8C%E9%9F%B3
* http://www.piano-c.com/
* https://pf-j.sakura.ne.jp/music/chord.htm

### 音程

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E7%A8%8B
* https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1365320628
* https://okwave.jp/qa/q6858420.html

### 440Hz, 432Hz

* http://tabi-labo.com/156689/music-a432

### 和音の生成

* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442
* https://ja.wikipedia.org/wiki/%E4%B8%89%E5%92%8C%E9%9F%B3
* https://ja.wikipedia.org/wiki/%E3%83%91%E3%83%AF%E3%83%BC%E3%82%B3%E3%83%BC%E3%83%89

### 音名

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E5%90%8D%E3%83%BB%E9%9A%8E%E5%90%8D%E8%A1%A8%E8%A8%98

### 音階

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E

#### 五度圏

* http://dn-voice.info/music-theory/godoken/

### 音高の算出

* http://www.asahi-net.or.jp/~HB9T-KTD/music/Japan/Research/DTM/freq_map.html
* http://www.nihongo.com/aaa/chigaku/suugaku/pythagoras.htm

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[pydub](https://github.com/jiaaro/pydub)|[MIT](https://github.com/jiaaro/pydub/blob/master/LICENSE)|[Copyright (c) 2011 James Robert, http://jiaaro.com](https://github.com/jiaaro/pydub/blob/master/LICENSE)
[pygame](http://www.pygame.org/)|[LGPL](https://www.pygame.org/docs/)|[pygame](http://www.pygame.org/)

