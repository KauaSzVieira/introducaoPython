# DECLARAR
y: float; x: float; yex: float
# INÍCIO
# LER
x = float(input("Insira o valor de x: "))
y = float(input("Insira o valor de y: "))
yex = x
x = y
y = yex
# EXIBIR
print(x)
print(y)
# FIM