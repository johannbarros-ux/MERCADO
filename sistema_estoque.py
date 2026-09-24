from no_produto import NoProduto
from constantes import ESTOQUE_MINIMO_PADRAO


class SistemaEstoque:
    def __init__(self):
        self.raiz = None
        
    def esta_vazio(self):
        return self.raiz is None

    def cadastrar_produto(self, codigo, nome, preco, quantidade):
        dados_produto = {
            "código": codigo,
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade}

        
        # Criação do nó com o código e o dicionário de dados
        novo_no = NoProduto(codigo, dados_produto)

        # Se a árvore estiver vazia, o novo nó vira a raiz
        if self.esta_vazio():
            self.raiz = novo_no
            return

        # Inserção na Árvore Binária de Busca (BST)
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
                # Se o código já existe, atualiza os dados do produto existente
                atual.dados = dados_produto
                break        

    def consultar_produto(self, codigo):
        atual = self.raiz
        while atual is not None:
            if codigo == atual.codigo:
                return atual.produto
            elif codigo < atual.codigo:
                atual = atual.esquerda
    
           
                             
             


    # TODO: retornar os dados do produto com esse código,
    # ou None se o código não existir no estoque.
        pass
    def listar_catalogo(self):
    # TOD for produto in produtos:

                print("Produto encontrado:")
                print(f"Nome: {produto['nome']}")
                print(f"Preço: R$ {produto['preco']:.2f}")
                print(f"Quantidade: {produto['quantidade']}")
    def calcular_valor_total_estoque(self):
    # TODO: retornar o valor total do estoque
    # (soma de preco * quantidade de todos os produtos).
        pass
    def produtos_estoque_baixo(self, minimo=ESTOQUE_MINIMO_PADRAO):
    # TODO: retornar a lista de produtos cuja quantidade


    # é menor que 'minimo'.
        pass
    def remover_produto(self, codigo):
    # TODO: remover o produto com esse código, mantendo
    # a propriedade da ABP para os produtos restantes.
        pass
    def diagnostico(self):
    # TODO: retornar a altura da árvore.
    # Serve para monitorar se o estoque está bem distribuído
    # (uma árvore muito "torta" deixa a busca mais lenta).
        pass
    





























    