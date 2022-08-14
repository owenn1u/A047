import random

start = int(input('請決定隨機範圍開始值: '))
end = int(input('請決定隨機範圍結束值: '))

r = random.randint(start, end)
count = 0


while True:
	n = int(input('請猜一個數字: '))
	count += 1
	if r == n:
		print("恭喜猜對了!")
		print('你總共猜了', count, '次')
		break
	elif r > n:
		print("再猜大一點的數字吧!")
	else:
		print("再猜小一點的數字吧!")
	print('這是你猜的第', count, '次')
	


