value = float(input())
num = 0

print("NOTAS:")


while(value >= 100.00):
	num = num+1
	value = value - 100
print(str(num) + " nota(s) de R$ 100.00")
num = 0

while(value >= 50.00):
        num = num+1
        value = value - 50
print(str(num) + " nota(s) de R$ 50.00")
num = 0

while(value >= 20.00):
        num = num+1
        value = value - 20
print(str(num) + " nota(s) de R$ 20.00")
num = 0

while(value >= 10.00):
        num = num+1
        value = value - 10
print(str(num) + " nota(s) de R$ 10.00")
num = 0

while(value >= 5.00):
        num = num+1
        value = value - 5
print(str(num) + " nota(s) de R$ 5.00")
num = 0

while(value >= 2.00):
        num = num+1
        value = value - 2
print(str(num) + " nota(s) de R$ 2.00")
num = 0

print("MOEDAS:")

while(value >= 1.00):
        num = num+1
        value = value - 1
print(str(num) + " moeda(s) de R$ 1.00")
num = 0

while(value >= 0.50):
        num = num+1
        value = value - 0.50
print(str(num) + " moeda(s) de R$ 0.50")
num = 0

while(value >= 0.25):
        num = num+1
        value = value - 0.25
print(str(num) + " moeda(s) de R$ 0.25")
num = 0

while(value >= 0.10):
        num = num+1
        value = value - 0.10
print(str(num) + " moeda(s) de R$ 0.10")
num = 0

while(value >= 0.05):
        num = num+1
        value = value - 0.05
print(str(num) + " moeda(s) de R$ 0.05")
num = 0

while(value > 0.00):
        num = num+1
        value = value - 0.01
print(str(num) + " moeda(s) de R$ 0.01")


