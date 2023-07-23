TSP-Visualizer
===

巡回セールスマン問題のシミュレータ

# 使い方

1. pythonでローカルサーバを動かす

```
python base.py
```

CORSエラーが発生するため、サーバを動かす必要がある。

2. run.js内の"dataIsHandmade"のtrue, falseを用途に応じて変更する

trueの場合、あらかじめ作成したデータを用いてシミュレータを行う。
falseの場合、ランダムにデータを作成してシミュレータを行う。

3. Webサイトでページを開ける

[URL] : http://127.0.0.1:8080/

4. データの入力を行う。

"dataIsHandmade"がtrueの場合、「ファイルを選択」ボタンを押してあらかじめ用意したdataを入力する。
"dataIsHandmade"がfalseの場合、都市数を設定することでデータをランダムに作成する。

5. ビジュアライザを行う。

# 補足

検証ツールを用いると、今回の入力データが出力されている。
このデータを用意し"dataIsHandmade"をtrueにすることで、前回の入力データと同じ入力でビジュアライザを行うことができる。

# 参考サイト

https://github.com/Takt29/TSP-Visualizer