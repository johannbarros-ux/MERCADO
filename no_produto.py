class NoProduto:
    def __init__(self, codigo, produto, esquerda=None,direita=None):

        self.codigo = codigo # chave da árvore
        self.produto = produto # dict: {"nome":, "preco":,"quantidade":}

        self.esquerda = esquerda
        self.direita = direita