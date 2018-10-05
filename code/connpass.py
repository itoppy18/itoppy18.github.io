#create by itoppy

import requests
import bs4

def main():
	name = None
	while name != "":
		name = input("検索したいユーサー名を入力してください。")
		userSearch(name)
	

def userSearch(nickname):
	url = "https://connpass.com/api/v1/event?nickname=" + nickname
	data = requests.get(url).json()
	events = data["events"]
	print(nickname + "は以下のイベントに参加、もしくは予約しました。\n")
	for event in events:
		for k, v in event.items():
			if k == "owner_nickname":
				print("開催者：")
				print(v)
			if k == "place":
				print("場所：")
				print(v)
			if k == "title":
				print("イベント名：")
				print(v)
		print("\n")
		
main()
