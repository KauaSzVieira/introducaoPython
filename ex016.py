# DECLARAR
hora_trab: float; val_hora: float; desconto: float
dependente: int; salario_liq: float; salario_bru: float
# INÍCIO
# LER
hora_trab = float(input("Insira hora_trab: "))
val_hora = float(input("Insira val_hora: "))
desconto = float(input("Insira desconto: "))
dependente = int(input("Insira dependente: "))
salario_bru = hora_trab * val_hora
desconto = salario_bru * (desconto / 100)
salario_liq = salario_bru - desconto
salario_liq = salario_liq + (dependente * 100)
# EXIBIR
print(salario_liq)
# FIM