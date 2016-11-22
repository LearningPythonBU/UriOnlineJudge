lineIn = input()
A,B,C = lineIn.split()

A = float(A)
B = float(B)
C = float(C)

triangle = A * C / 2
circle = 3.14159 * C * C
trapezoid = (A+B) * C / 2
square = B * B
rectangle = A * B

print("TRIANGULO: %0.3f" % triangle)
print("CIRCULO: %0.3f" % circle)
print("TRAPEZIO: %0.3f" % trapezoid)
print("QUADRADO: %0.3f" % square)
print("RETANGULO: %0.3f" % rectangle)


