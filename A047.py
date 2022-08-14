import random

r = random.randint(1, 100)



while True:
	n = int(input('請猜一個界在1~100的數字: '))
	if r == n:
		print("恭喜猜對了!")
		break
	elif r > n:
		print("再猜大一點的數字吧!")
	else:
		print("再猜小一點的數字吧!")
	


