str0 = input("")
code0, num0, prc0 = str0.split()
num0 = int(num0)
prc0 = float(prc0)

str2 = input("")
code2, num2, prc2 = str2.split()
num2 = int(num2)
prc2 = float(prc2)

total = num0*prc0 + num2*prc2
print("VALOR A PAGAR: R$ %0.2f" % total)
