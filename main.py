from sistema_estoque import SistemaEstoque
from constantes import TITULO_SISTEMA, MENU_PRINCIPAL
def main():
    sistema = SistemaEstoque()
    while True:
        print(TITULO_SISTEMA)
        print(MENU_PRINCIPAL)
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            codigo = input("Código ")
            nome = input("Nome ")
            preco = float(input("Preco "))
            quantidade = int(input("Quantidade "))
            sistema.cadastrar_produto(codigo, nome, preco, quantidade)
            pass # TODO: chamar sistema.cadastrar_produto(...)
        elif opcao == "2":
            codigo = input("Digite o código do produto que deseja encontrar")

            sistema.consultar_produto(codigo)
            pass # TODO: chamar sistema.consultar_produto(...)
        elif opcao == "3":

            produtos = sistema.listar_catalogo()

            pass # TODO: chamar sistema.listar_catalogo()
        elif opcao == "4":
            pass # TODO: chamar
            sistema.calcular_valor_total_estoque()
        elif opcao == "5":
            pass # TODO: chamar sistema.produtos_estoque_baixo()
        elif opcao == "6":
            pass # TODO: chamar sistema.remover_produto(...)
        elif opcao == "7":
            pass # TODO: chamar sistema.diagnostico()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
if __name__ == "__main__":
    main()