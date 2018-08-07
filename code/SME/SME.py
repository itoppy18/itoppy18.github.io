#! /usr/bin/python3
# by itoppy18
#覚書。１匹のメスは４００個の卵を産卵する。
import time

def sme(number, fo):
    m = number
    cicadas_dict = {         #セミの出現周期と初期個体数の辞書
        2: m,
        3: m,
        4: m,
        5: m,
        6: m,
        7: m,
        8: m,
        9: m,
        10: m,
        11: m,
        12: m,
        13: m,
        14: m,
        15: m,
        16: m,
        17: m,
        18: m,
        19: m,
        20: m      }
    years = 1
    n = fo
    minus = 1


    for i in range(n - 1):
        index = []
        for key in cicadas_dict:
            int(cicadas_dict[key])
            if cicadas_dict[key] <= 0:
                cicadas_dict[key] = 0
        years += 1
        for key in cicadas_dict:
            int(key)
            if years % key == 0:
                index.append(cicadas_dict[key])
                for i in range(len(index)):
                    cicadas_dict[key] -= minus

        for key in cicadas_dict:
            if key >=18:
                cicadas_dict[key] -= 10
                
        for key in cicadas_dict:
            int(cicadas_dict[key])
            if cicadas_dict[key] <= 0:
                    cicadas_dict[key] = 0
        str(years)
        print(years)
        print(cicadas_dict)
        print("\n")
        
        if years % 100 == 0 and n > 100:
            print("midstream simulation result:")
            for k, v in sorted(cicadas_dict.items(), key=lambda x: -x[1]):
                print(str(k) + ": " + str(v))
        
    print("final simulation result:")
    for k, v in sorted(cicadas_dict.items(), key=lambda x: -x[1]):
        print(str(k) + ": " + str(v))

sme(10, 10)
