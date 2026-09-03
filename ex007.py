# DECLARAR
larg: float; comp: float; alt: float; vol: float
# INÍCIO
# LER
comp = float(input("Insira o valor de comp: "))
larg = float(input("Insira o valor de larg: "))
alt = float(input("Insira o valor de alt: "))
vol = comp * larg * alt
# EXIBIR
print(vol)
# FIM