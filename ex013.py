# DECLARAR
ali_kg: float; ali_g: float; dias: float
# INÍCIO
# LER
ali_kg = float(input("Insira o alimento em kg: "))
ali_g = ali_kg * 1000
dias = ali_g / 50
# EXIBIR
print(dias)
# FIM