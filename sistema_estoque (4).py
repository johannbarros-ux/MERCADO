from no_produto import NoProduto
from constantes import ESTOQUE_MINIMO_PADRAO


class SistemaEstoque:

    def __init__(self):
        self.raiz = None

    def esta_vazio(self):
        return self.raiz is None

    def cadastrar_produto(self, codigo, nome, preco, quantidade):
        dados_produto = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        novo_no = NoProduto(codigo, dados_produto)

        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._cadastrar(self.raiz, novo_no)

    def _cadastrar(self, atual, novo_no):
        if novo_no.codigo < atual.codigo:

            if atual.esquerda is None:
                atual.esquerda = novo_no
            else:
                self._cadastrar(atual.esquerda, novo_no)

        elif novo_no.codigo > atual.codigo:

            if atual.direita is None:
                atual.direita = novo_no
            else:
                self._cadastrar(atual.direita, novo_no)

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
        self._listar_catalogo(self.raiz, produtos)
        return produtos

    def _listar_catalogo(self, no, produtos):
        if no is not None:
            self._listar_catalogo(no.esquerda, produtos)
            produtos.append(no.produto)
            self._listar_catalogo(no.direita, produtos)

    def calcular_valor_total_estoque(self):
        return self._calcular_valor_total_estoque(self.raiz)

    def _calcular_valor_total_estoque(self, no):
        if no is None:
            return 0.0

        valor_esquerda = self._calcular_valor_total_estoque(no.esquerda)
        valor_direita = self._calcular_valor_total_estoque(no.direita)

        valor_atual = no.produto["preco"] * no.produto["quantidade"]

        return valor_esquerda + valor_atual + valor_direita

    def produtos_estoque_baixo(self, minimo=ESTOQUE_MINIMO_PADRAO):
        produtos_baixo_estoque = []

        self._produtos_estoque_baixo(
            self.raiz,
            produtos_baixo_estoque,
            minimo
        )

        return produtos_baixo_estoque

    def _produtos_estoque_baixo(self, no, produtos, minimo):
        if no is not None:

            self._produtos_estoque_baixo(
                no.esquerda,
                produtos,
                minimo
            )

            if no.produto["quantidade"] < minimo:
                produtos.append(no.produto)

            self._produtos_estoque_baixo(
                no.direita,
                produtos,
                minimo
            )

    def remover_produto(self, codigo):
        self.raiz = self._remover_produto(self.raiz, codigo)

    def _remover_produto(self, no, codigo):
        if no is None:
            return None

        if codigo < no.codigo:
            no.esquerda = self._remover_produto(
                no.esquerda,
                codigo
            )

        elif codigo > no.codigo:
            no.direita = self._remover_produto(
                no.direita,
                codigo
            )

        else:
            # Caso 1: não possui filho à esquerda
            if no.esquerda is None:
                return no.direita

            # Caso 2: não possui filho à direita
            elif no.direita is None:
                return no.esquerda

            # Caso 3: possui dois filhos
            min_no = self._encontrar_minimo(no.direita)

            no.codigo = min_no.codigo
            no.produto = min_no.produto

            no.direita = self._remover_produto(
                no.direita,
                min_no.codigo
            )

        return no

    def _encontrar_minimo(self, no):
        atual = no

        while atual.esquerda is not None:
            atual = atual.esquerda

        return atual

    def diagnostico(self):
        if self.esta_vazio():
            return 0

        return self._altura(self.raiz)

    def _altura(self, no):
        if no is None:
            return 0

        altura_esquerda = self._altura(no.esquerda)
        altura_direita = self._altura(no.direita)

        return 1 + max(altura_esquerda, altura_direita)