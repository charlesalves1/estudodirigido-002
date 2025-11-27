# Peça o nome e idade da pessoa e diga se ela pode entrar ou não
nome = input("Nome: ") 
idade = int(input("Idade: ")) 
if idade >= 18:
 print(f"{nome}, você pode entrar.") 
else:
 print(f"{nome}, você não pode entrar.") 