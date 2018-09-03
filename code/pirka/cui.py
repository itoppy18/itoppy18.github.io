kanto = [
					{"こんにちは|こんちは" : [[0.00, 0.00, 0.00, 0.00, "%pat%"], [0.00, 0.00, 0.00, 0.00, "久しぶり"]]}, 
					{"さようなら|さよなら" : [[0.00, 0.00, 0.00, 0.00, "%pat%"], [0.00, 0.00, 0.00, 0.00, "えーやだよ"]]}
				]

for i in range(len(kanto)):
	nowDict = kanto[i]
	for key in nowDict:
		nowList = nowDict[key]
		respList = []
		for j in range(len(nowList)):
			response = nowList[i][4]
			respList.append(response)
			for ii in range(len(respList)):
				if respList[ii] == "%pat%":
					respList[ii] = respList[ii].replace("%pat%", response)
		print(respList)
