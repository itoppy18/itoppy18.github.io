#!/usr/bin/python3
#coding:utf-8

import os
import time

def recording():
	file_name = "example"
	while file_name != "":
		file_name = input("\n" + "ファイル名を入力してください。(何も入力しなければ終了,過去と同一のファイル名を入力すると上書きされます。)→  ")
		str(file_name)
		if file_name != "":
			print("録音を開始します。(Ctrl + Cキーで終了)")
			print("3")
			time.sleep(1)
			print("2")
			time.sleep(1)
			print("1")
			time.sleep(1)
			os.system("arecord -D plughw:1 -c1 -r 48000 -f S32_LE -t wav -V mono -v /home/pi/Music/" + file_name + ".wav")
		else:
			print("録音を終了しました")

recording()
