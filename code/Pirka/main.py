#! /usr/bin/python3
# coding:utf-8
# Pirka AI
#made by @itoppy18

import os
import time
import math
import json
import requests
import datetime
from mcpi import minecraft
	
class App:
	def google():
		if mode == "グーグル":
			url = "https://www.google.co.jp/search?q={0}".format(user_input)
			print("Googleで," + user_input + "を検索しています。")
			os.system("./aquestalkpi/AquesTalkPi " + "\"" + "グーグルで," + user_input + "を検索しています。" + "\"" + "| aplay")
			os.system("chromium-browser --app " + url)
	def youtube():
		if mode == "ユーチューブ":
			url = "https://www.youtube.com/results?search_query={0}".format(user_input)
			print("YouTubeで," + user_input + "を検索しています。")
			os.system("./aquestalkpi/AquesTalkPi " + "\"" + "ユーチューブで," + user_input + "を検索しています。" + "\"" + "| aplay")
			os.system("chromium-browser --app " + url)
	def wikipedia():
		if mode == "ウィキペディア":
			url = "https://ja.wikipedia.org/wiki/{0}".format(user_input)
			print("Wikipediaで," + user_input + "を検索しています。")
			os.system("./aquestalkpi/AquesTalkPi " + "\"" + "ウィキペディアで," + user_input + "を検索しています。 " + "\"" + "| aplay")
			os.system("chromium-browser --app " + url)
	def math():
		if mode == "計算":
			pass
	def story():
		if mode == "小説":
			print("Carbon Libraryから," + user_input + "を朗読します。")
			os.system("./aquestalkpi/AquesTalkPi " + "\"" + "カーボンライブラリから," + user_input + "を朗読します。" + "\"" + "| aplay")
			os.system("./aquestalkpi/AquesTalkPi -f " + user_input + ".txt" + " | aplay")
	def jp_to_en():
		if mode == "英訳":
			url = "https://translate.google.co.jp/#ja/en/{0}".format(user_input)
			print("Google翻訳で," + user_input + "を英訳しています。")
			os.system("./aquestalkpi/AquesTalkPi " + "\"" + "グーグル翻訳で," + user_input + "を英訳しています。 " + "\"" + "| aplay")
			os.system("chromium-browser --app " + url)
	def en_to_ja():
		if mode == "和訳":
			url = "https://translate.google.co.jp/#en/ja/{0}".format(user_input)
			print("Google翻訳で," + user_input + "を和訳しています。")
			os.system("./aquestalkpi/AquesTalkPi " + "\"" + "グーグル翻訳で," + user_input + "を和訳しています。" + "\"" + "| aplay")
			os.system("chromium-browser --app " + url)
	def talk():
		if mode == "会話":
			print("会話を始めましょう。")
			os.system("./aquestalkpi/AquesTalkPi \"会話を始めましょう。\" | aplay")
			user_input = ""
			while user_input != "終了。":
				user_input = input("入力待ち…")
				if user_input == "あなたの名前は。":
					print("私の名前はぴりか,アイヌ語で「輝く」という意味です。")
					os.system("./aquestalkpi/AquesTalkPi \"私の名前はぴりか,アイヌ語で「輝く」という意味です。\" | aplay")
				elif user_input == "今は何時。":
					now = datetime.datetime.now()
					date = "現在の時刻は{0}時{1}分です。".format(now.hour, now.minute)
					print(date)
					os.system("./aquestalkpi/AquesTalkPi \"" + date + "\" | aplay")
				elif user_input == "明日の天気は。":
					url = "http://weather.livedoor.com/forecast/webservice/json/v1"
					payload = {"city": "130010"}
					data = requests.get(url, params = payload).json()
					title = data["title"]
					print(title)
					for weather in data["forecasts"]:
						print(weather["dateLabel"] + ':' + weather["telop"])
						dateLabel = weather["dateLabel"]
						if dateLabel == "明日":
							telop = weather["telop"]
					os.system("./aquestalkpi/AquesTalkPi " + " \"明日の" + title + "は,"+ telop + "でしょう。" + "\"" + " | aplay")
			os.system("./aquestalkpi/AquesTalkPi \"会話を終了します。\" | aplay")
			print("会話を終了します。")
			Main.main()	
			
class Main:
	def main():
		while True:
			mode = ""
			global mode
			global user_input
			os.system("./aquestalkpi/AquesTalkPi \"" + "モードを入力してください\" | aplay")
			mode = input("モードを入力…")
			if mode != "会話":
				os.system("./aquestalkpi/AquesTalkPi \"" + "検索文を入力してください\" | aplay")
				user_input = input("検索文を入力…")
			App.google()
			App.youtube()
			App.wikipedia()
			App.talk()
			App.story()
			App.jp_to_en()
			App.en_to_ja()

Main.main()	
