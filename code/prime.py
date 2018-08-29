import math

# 0以上整数x「未満」の素数をリストに格納して返す
def primes(x):
    if x < 2: return []

    primes = [i for i in range(x)]
    primes[1] = 0 # 1は素数ではない

    # エラトステネスのふるい
    for prime in primes:
        if prime > math.sqrt(x): break
        if prime == 0: continue
        for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]


# 整数xが素数かどうかを判定する
def is_prime(x):
    if x < 2: return False # 2未満に素数はない
    if x == 2 or x == 3 or x == 5: return True # 2,3,5は素数
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0: return False # 2,3,5の倍数は合成数

    # ためし割り: 疑似素数(2でも3でも5でも割り切れない数字)で次々に割っていく
    prime = 7
    step = 4
    while prime <= math.sqrt(x):
        if x % prime == 0: return False

        prime += step
        step = 6 - step

    return True


if __name__ == '__main__':
    print(primes(30)) #=> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    ls = [x for x in range(10000) if is_prime(x)]
    print(ls) #=> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
   

