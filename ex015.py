# DECLARAR
cat1: float; cat2: float; hip: float
# INÍCIO
# LER
cat1 = float(input("Insira o valor de cat1: "))
cat2 = float(input("Insira o valor de cat2: "))
hip = (cat1 * cat1 + cat2 * cat2) ** 0.5
# EXIBIR
print(hip)
# FIM