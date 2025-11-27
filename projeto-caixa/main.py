# main.py

from cliente import criar_cliente
from caixa import comprar

def main():
    cliente = criar_cliente()
    comprar(cliente)

main()
