#!/usr/bin/python3
#coding:utf-8
#kanto kor pirka nociw AI system ver.1.0.0.0's source code
#made by @itoppy18

#Pirka内部のモジュール読み込み
import feelings	#感情を計算
import config		#設定ファイル
import gui			#GUI生成
import responce#応答作成
import apps			#アプリケーション
import tokenize	#形態素解析
import data			#ログなど

class Main:
	def main():
		feelings.Init()
		config.Init()
		gui.Init()
		responce.Init()
		apps.Init()
		tokenize.Init()
		data.Init()
		
Main.main()
