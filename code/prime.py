#create by itoppy

import math
import time

#nが素数かを判定する
def prime(n):	
	c = 0
	if n < 2:
		return False
	rt = int(math.sqrt(n))
	
	x = 2
	if x > rt:
		return True
	y = n % x
	if y == 0:
		return False
	
	x = 3
	if x > rt:
		return True
	y = n % x
	if y == 0:
		return False
	
	x = 5
	while True:
		if x > rt:
			return True
		y = n % x
		if y == 0:
			return False
		else: x += 4 if x % 6 == 1 else 2

#nまでの素数リストを返す
def primes(n):
	prime_list = []
	for i in range(n):
		if prime(i):
			prime_list.append(i)
	for i in range(len(prime_list)):
		print(prime_list[i])
			
#nまでの双子素数リストを返す
def dprimes(n):
	for i in range(n):
		if prime(i) and prime(i + 2):
			print(i)
			print(i + 2)
			print("\n")	
			
print(primes(1000000))
