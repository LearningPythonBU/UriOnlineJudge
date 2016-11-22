val = float(input())

stack = [100,50,20,10,5,2]
print("NOTAS:")

for x in stack:
	num = val * x
	num = num % x
	num = int(num)
	print(str(num) + " nota(s) de R$ %0.2f" % x )
	
print("MOEDAS:")
stack2 = [1.00,0.50, 0.25, 0.10, 0.05, 0.01]

for x in stack2:
	num = val * x
	num = num % x
	num = int(num)
	print(str(num) + " moeda(s) de R$ %0.2f" % x )


	
