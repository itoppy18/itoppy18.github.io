#!/usr/bin/python3
#coding:utf-8
#kanto kor pirka nociw AI system α0.0.0.0a source code
#data.py:各種データやログなどを記録
#一度しかないこの人生で、自分の夢を追いかけないでいつ追いかけるのだろう。-孫正義
#created by @itoppy18

#会話ログ
class Log:
	pass

#入力対応出力辞書「kantoーかんとー」
class Kanto:
	#バージョン
	version = "α0.0"
	#本体
	kanto = [
					{"こんにちは|こんちは" : [[0.00, 0.00, 0.00, 0.00, "%pat%"][0.00, 0.00, 0.00, 0.00, "久しぶり"]]}
					{"さようなら|さよなら" : [[0.00, 0.00, 0.00, 0.00, "%pat%"], [0.00, 0.00, 0.00, 0.00, "えーやだよ"]]}
					]
					
#入力形態素意味発音解析辞書「nociwーのちうー」
class Nociw:
	#β0.0.0.0aにて追加予定
	pass

class Pirka:
	version = "kanto kor pirka nociw AI system α0.0.0.0a"

