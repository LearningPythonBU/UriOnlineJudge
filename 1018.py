val = int(input())

print(str(val))

stack = [100,50,20,10,5,2,1]

for x in stack:
	num = 0
	while(val >= x):
		num = num+1
		val = val - x
	print(str(num) + " nota(s) de R$ %i,00" % x )
