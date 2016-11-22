lineIn = input()
a,b,c = lineIn.split()

a = int(a)
b = int(b)
c = int(c)

largest = a

if(b > largest):
	largest = b
if(c > largest):
	largest = c

print(str(largest) + " eh o maior")


