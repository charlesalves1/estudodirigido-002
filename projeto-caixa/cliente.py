# cliente.py

def criar_cliente():
    nome = input("Digite o nome do cliente: ")
    
    while True:
        try:
            saldo = float(input("Digite o saldo disponível: "))
            break
        except ValueError:
            print("Valor inválido! Digite um número.")
    
    return {"nome": nome, "saldo": saldo}


def mostrar_saldo(cliente):
    print(f"Saldo atual de {cliente['nome']}: R$ {cliente['saldo']:.2f}\n")
