# DECLARAR
deposito: float; vf: float
# INÍCIO
# LER
deposito = float(input("Insira o valor do deposito: "))
rendimento = 1.013
vf = deposito * rendimento
# EXIBIR
print(vf)
# FIM