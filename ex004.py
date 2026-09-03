# DECLARAR
temp_C: float; temp_F: float
# INÍCIO
# LER
temp_C = float(input("Insira o valor de temp_C: "))
temp_F = (9 * temp_C + 160) / 5
# EXIBIR
print(temp_F)
# FIM