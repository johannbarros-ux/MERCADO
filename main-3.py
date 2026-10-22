from sistema_estoque import SistemaEstoque
from constantes import (
    TITULO_SISTEMA,
    MENU_PRINCIPAL,
    LISTA_PRODUTOS,
    MSG_PRODUTO_NAO_ENCONTRADO,
    MSG_PRODUTO_CADASTRADO,
    MSG_PRODUTO_REMOVIDO,
    LINHA
)


def main():
    sistema = SistemaEstoque()

    while True:
        print()
        print(TITULO_SISTEMA)
        print(MENU_PRINCIPAL)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = int(input("Código: "))
            nome = input("Nome: ")
            preco = float(input("Preco: "))
            quantidade = int(input("Quantidade: "))

            sistema.cadastrar_produto(
                codigo,
                nome,
                preco,
                quantidade
            )

            print(MSG_PRODUTO_CADASTRADO)

        elif opcao == "2":
            codigo = int(input(
                "Digite o código do produto que deseja encontrar: "
            ))

            produto = sistema.consultar_produto(codigo)

            if produto is not None:
                print("Produto encontrado!")
                print(f"Nome: {produto['nome']}")
                print(f"Preço: R$ {produto['preco']:.2f}")
                print(f"Quantidade: {produto['quantidade']}")
            else:
                print(MSG_PRODUTO_NAO_ENCONTRADO)

        elif opcao == "3":
            catalogo = sistema.listar_catalogo()

            if not catalogo:
                print("Estoque vazio.")
            else:
                print(LISTA_PRODUTOS)

                for prod in catalogo:
                    print(f"Código: {prod['codigo']}")
                    print(f"Nome: {prod['nome']}")
                    print(f"Preço: R$ {prod['preco']:.2f}")
                    print(f"Quantidade: {prod['quantidade']}")
                    print()

        elif opcao == "4":
            total = sistema.calcular_valor_total_estoque()

            print(f"Valor total do estoque: R$ {total:.2f}")

        elif opcao == "5":
            produtos_baixo = sistema.produtos_estoque_baixo()

            if not produtos_baixo:
                print("Nenhum produto está com estoque baixo.")
            else:
                print("Produtos com estoque baixo:")

                for p in produtos_baixo:
                    print(f"Código: {p['codigo']}")
                    print(f"Nome: {p['nome']}")
                    print(f"Quantidade: {p['quantidade']}")
                    print()

        elif opcao == "6":
            codigo = int(input(
                "Digite o código do produto que deseja remover: "
            ))

            produto = sistema.consultar_produto(codigo)

            if produto is not None:
                sistema.remover_produto(codigo)
                print(MSG_PRODUTO_REMOVIDO)
            else:
                print(MSG_PRODUTO_NAO_ENCONTRADO)

        elif opcao == "7":
            altura = sistema.diagnostico()
            print(f"Altura da árvore: {altura}")

        elif opcao == "8":
            codigo = int(input("Código do produto: "))
            preco = float(input("Novo preço: "))
            quantidade = int(input("Nova quantidade: "))

            atualizado = sistema.atualizar_produto(
                codigo,
                preco,
                quantidade
            )

            if atualizado:
                print("Produto atualizado com sucesso.")
            else:
                print("Produto não encontrado.")

        elif opcao == "9":
            sistema.exportar_catalogo_txt()
            print("Catálogo exportado para catalogo.txt.")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()