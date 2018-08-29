def main(f, n):
	cicadas_dict = {
									12 : n,
									13 : n,
									14 : n,
									15 : n,
									16 : n,
									17 : n,
									18 : n
								}
	years = 0
	for i in range(f):
		years += 1
		index = []
		ac = 0
		for key in cicadas_dict:
			if years % key == 0 and years > 12:
				index.append(key)
		for key in cicadas_dict:
			if key in index:
				ac += cicadas_dict[key]
		for i in range(len(index)):
			cicadas_dict[index[i]] *= (cicadas_dict[index[i]] // ac)
		print(years)
		print(cicadas_dict)
		print("\n")
	for k, v in sorted(cicadas_dict.items(), key=lambda x: -x[1]):
		print(str(k) + ": " + str(v))

main(100, 10000)
