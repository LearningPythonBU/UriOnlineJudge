val = float(input())

stack = [100,50,20,10,5,2]
print("NOTAS:")

for x in stack:
	num = 0
	while(val >= x):
		num = num+1
		val = val - x
	print(str(num) + " nota(s) de R$ %0.2f" % x )

print("MOEDAS:")

# this is necessary because fractional subtraction
# was providing rounding errors, especially with
# the smaller fractions, i.e. 0.05, 0.01
# this problem is circumvented by multiplying the
# original value by 100 and then using integer
# subtraction instead of float/double subtraction
# this eliminates the rounding errors

val = 100 * val
stack2 = [100,50,25,10,5,1]

for x in stack2:
	num = 0
	while(val >= x):
		num = num+1
		val = val - x
	print(str(num) + " moeda(s) de R$ %0.2f" % (x/100) )

