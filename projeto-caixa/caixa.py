# caixa.py

from produtos import produtos, listar_produtos
from cliente import mostrar_saldo

def comprar(cliente):
    while cliente["saldo"] > 0:
        listar_produtos()
        mostrar_saldo(cliente)

        try:
            cod = int(input("Escolha o código do produto (ou 0 para sair): "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if cod == 0:
            print("Compra encerrada!")
            break
        
        if cod not in produtos:
            print("Produto inválido!")
            continue

        nome_prod, preco_prod = produtos[cod]

        try:
            quantidade = int(input("Quantidade: "))
        except ValueError:
            print("Quantidade inválida!")
            continue

        total = preco_prod * quantidade

        print(f"\nVocê escolheu {quantidade}x {nome_prod} → Total: R$ {total:.2f}")

        if total > cliente["saldo"]:
            print("Saldo insuficiente!\n")
            continue

        cliente["saldo"] -= total
        print(f"Compra de {nome_prod} realizada com sucesso!")

    print("\nNão é possível continuar: saldo zerado ou cliente saiu.")
    mostrar_saldo(cliente)

  