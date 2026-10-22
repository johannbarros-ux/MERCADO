from no_produto import NoProduto
from constantes import ESTOQUE_MINIMO_PADRAO


class SistemaEstoque:

    def __init__(self):
        self.raiz = None

    def esta_vazio(self):
        return self.raiz is None

    def _consultar_recursivo(self, no_atual, codigo):
        if no_atual is None:
            return None

        if codigo == no_atual.codigo:
            return no_atual.produto

        if codigo < no_atual.codigo:
            return self._consultar_recursivo(
                no_atual.esquerda,
                codigo
            )

        return self._consultar_recursivo(
            no_atual.direita,
            codigo
        )

    def cadastrar_produto(self, codigo, nome, preco, quantidade):
        dados_produto = {
            "codigo": codigo,
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        novo_no = NoProduto(codigo, dados_produto)

        if self.esta_vazio():
            self.raiz = novo_no
            return

        atual = self.raiz

        while True:
            if codigo < atual.codigo:
                if atual.esquerda is None:
                    atual.esquerda = novo_no
                    break

                atual = atual.esquerda

            elif codigo > atual.codigo:
                if atual.direita is None:
                    atual.direita = novo_no
                    break

                atual = atual.direita

            else:
                atual.produto = dados_produto
                break

    def consultar_produto(self, codigo):
        atual = self.raiz

        while atual is not None:
            if codigo == atual.codigo:
                return atual.produto

            elif codigo < atual.codigo:
                atual = atual.esquerda

            else:
                atual = atual.direita

        return None

    def listar_catalogo(self):
        produtos = []

        def percorrer(no):
            if no is not None:
                percorrer(no.esquerda)
                produtos.append(no.produto)
                percorrer(no.direita)

        percorrer(self.raiz)

        return produtos

    def calcular_valor_total_estoque(self):
        total = 0
        produtos = self.listar_catalogo()

        for produto in produtos:
            total += produto["preco"] * produto["quantidade"]

        return total

    def produtos_estoque_baixo(
        self,
        minimo=ESTOQUE_MINIMO_PADRAO
    ):
        produtos_baixo = []
        produtos = self.listar_catalogo()

        for produto in produtos:
            if produto["quantidade"] < minimo:
                produtos_baixo.append(produto)

        return produtos_baixo

    def remover_produto(self, codigo):

        def remover(no, codigo):
            if no is None:
                return None

            if codigo < no.codigo:
                no.esquerda = remover(
                    no.esquerda,
                    codigo
                )

            elif codigo > no.codigo:
                no.direita = remover(
                    no.direita,
                    codigo
                )

            else:
                if no.esquerda is None and no.direita is None:
                    return None

                if no.esquerda is None:
                    return no.direita

                if no.direita is None:
                    return no.esquerda

                sucessor = no.direita

                while sucessor.esquerda is not None:
                    sucessor = sucessor.esquerda

                no.codigo = sucessor.codigo
                no.produto = sucessor.produto

                no.direita = remover(
                    no.direita,
                    sucessor.codigo
                )

            return no

        self.raiz = remover(self.raiz, codigo)

    def diagnostico(self):

        def altura(no):
            if no is None:
                return -1

            altura_esquerda = altura(no.esquerda)
            altura_direita = altura(no.direita)

            return 1 + max(
                altura_esquerda,
                altura_direita
            )

        return altura(self.raiz)

    def atualizar_produto(
        self,
        codigo,
        preco=None,
        quantidade=None
    ):
        no = self._buscar_no(
            self.raiz,
            codigo
        )

        if no is None:
            return False

        if preco is not None:
            no.produto["preco"] = preco

        if quantidade is not None:
            no.produto["quantidade"] = quantidade

        return True

    def _buscar_no(self, no_atual, codigo):
        if no_atual is None:
            return None

        if codigo == no_atual.codigo:
            return no_atual

        if codigo < no_atual.codigo:
            return self._buscar_no(
                no_atual.esquerda,
                codigo
            )

        return self._buscar_no(
            no_atual.direita,
            codigo
        )

    def exportar_catalogo_txt(
        self,
        nome_arquivo="catalogo.txt"
    ):
        catalogo = self.listar_catalogo()

        with open(
            nome_arquivo,
            "w",
            encoding="utf-8"
        ) as arquivo:

            arquivo.write(
                "=== CATÁLOGO DE ESTOQUE ===\n\n"
            )

            for produto in catalogo:
                arquivo.write(
                    f'Código: {produto["codigo"]}\n'
                    f'Nome: {produto["nome"]}\n'
                    f'Preço: R$ {produto["preco"]:.2f}\n'
                    f'Quantidade: {produto["quantidade"]}\n'
                    f'-------------------------\n'
                )