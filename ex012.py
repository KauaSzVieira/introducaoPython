# DECLARAR
ano_nas: int; ano_atual: int
idade: int; idade_fut: int
# INÍCIO
# LER
ano_nas = int(input("Insira o ano de nascimento: "))
ano_atual = int(input("Insira o ano atual: "))
idade = ano_atual - ano_nas
idade_fut = idade + 17
# EXIBIR
print(idade)
print(idade_fut)
# FIM