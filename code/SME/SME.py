#! /usr/bin/python3
# by itoppy18
import time

def sme(number, fo):
    m = number
    cicadas_dict = {         #セミの出現周期と初期個体数の辞書
        12: m,
        13: m,
        14: m,
        15: m,
        16: m,
        17: m,
        18: m, }
    years = 0
    n = fo

    for i in range(n):
    	ac = 0
    	index = []
    	years += 1
    	for key in cicadas_dict:
    		int(cicadas_dict[key])
    		if cicadas_dict[key] <= 0:
    			cicadas_dict[key] = 0
    	for key in cicadas_dict:
    		int(key)
    		if years % key == 0:
    			index.append(key)
    	for value in cicadas_dict:
    		if value in index:
    			ac += value			
    	for i in range(len(index)):
    		cicadas_dict[key] = cicadas_dict[key] * (cicadas_dict[key] / ac) 
    	for key in cicadas_dict:
    		int(cicadas_dict[key])
    		if cicadas_dict[key] <= 0:
    			cicadas_dict[key] = 0
    	str(years)
    	print(years)
    	print(cicadas_dict)
    	print("\n")
    	if years % 100 == 0 and n > 100 and n != years:
    		print("midstream simulation result:")
    		for k, v in sorted(cicadas_dict.items(), key=lambda x: -x[1]):
    			print(str(k) + ": " + str(v))
    	print("final simulation result:")
    	for k, v in sorted(cicadas_dict.items(), key=lambda x: -x[1]):
    		print(str(k) + ": " + str(v))

sme(300, 300)
