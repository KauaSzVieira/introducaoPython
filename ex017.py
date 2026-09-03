# DECLARAR
tempo: float; velocidade: float
distancia: float; litros: float
# INÍCIO
# LER
tempo = float(input("Insira o valor de tempo: "))
velocidade = float(input("Insira o valor de velocidade: "))
distancia = tempo * velocidade
litros = distancia / 12
# EXIBIR
print(litros)
# FIM