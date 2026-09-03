# DECLARAR
A: int; B: int; C: int
delta: int; x1: int; x2: int
# INÍCIO
# LER
A = int(input("Insira o valor de A: "))
B = int(input("Insira o valor de B: "))
C = int(input("Insira o valor de C: "))
delta = B * B - 4 * A * C
x1 = (-B + delta ** 0.5) / (2 * A)
x2 = (-B - delta ** 0.5) / (2 * A)
# EXIBIR
print(x1)
print(x2)