# produtos.py

produtos = {
    1: ("Camisa", 50.00),
    2: ("Boné", 30.00),
    3: ("Calça", 120.00),
    4: ("Tênis", 250.00),
    5: ("Meias", 10.00)
}

def listar_produtos():
    print("\n--- Lista de Produtos ---")
    for codigo, (nome, preco) in produtos.items():
        print(f"{codigo} - {nome} .... R$ {preco:.2f}")
