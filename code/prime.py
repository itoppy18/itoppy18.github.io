def prime(n):
	c = 0
	if n <= 2:
		return False
		c = 1
	x = 2
	while c == 0:
		y = n % x
		if y == 0:
			return False
			c = 1
		else:
			x += 1
		if x >= n:
			return True
			c = 1
	z = n / x

def primes(n):
	prime_list = []
	for i in range(n):
		if prime(i):
			prime_list.append(i)
	for i in range(len(prime_list)):
		print(prime_list[i])
			
def dprimes(n):
	for i in range(n):
		if prime(i) and prime(i + 2):
			print(i)
			print(i + 2)
			print("\n")	
		
dprimes(100000)
