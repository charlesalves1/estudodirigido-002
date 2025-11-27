'''programa que simula pedidos em uma lanchonete. Só aceita:
 Cartão (se valor > 20),
 Pix (qualquer valor),
 Dinheiro (somente valor exato. 10).'''
forma = input("Forma de pagamento: ").lower()
valor = float(input("Valor: ")) 
if forma == "cartao" and valor > 20: 
    print("Aceito!")
elif forma == "pix":
    print("Aceito!")
elif forma == "dinheiro" and valor == 10: 
    print("Aceito!")
else:
    print("Não aceito.")
    