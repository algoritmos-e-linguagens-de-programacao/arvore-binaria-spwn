from node import Node


class BinaryTree:

    def __init__(self):
        self.root = None

    def adicionar(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node

        else:
            aux = self.root
            while (True):
                if aux <= value:
                    father = aux
                    aux = aux.Esquerda()
                    son_esquerda = True
                else:
                    father = aux
                    aux = aux.Direita()
                    son_esquerda = False

                if aux is None:
                    break
            if son_esquerda is False:
                father.Direita(node)
            else:
                father.Esquerda(node)

    def remover(self, value, node):
        if node == self.root:
            node = self.root
        if node is None:
            return node
        if value < node.value:
            node.esquerda = self.remover(value, node.esquerda)
        elif value > node.value:
            node.direita = self.remover(value, node.direita)
        else:
            if node.esquerda is None:
                return node.direita
            elif node.direita is None:
                return node.esquerda
            else:
                substituto = self.min(node.direita)
                node.value = substituto
                node.direita = self.remover(substituto, node.direita)

        return node

    #impressão de arvores

        # pre ordem 
    def preordem(self, inicio, string):
        if inicio:
            string += (str(inicio.value) + "-")
            string = self.preordem(inicio.esquerda, string)
            string = self.preordem(inicio.direita, string)
        return string

    # em ordem 
    def emOrdem(self, inicio, string):
        if inicio:
            string = self.emOrdem(inicio.esquerda, string)
            string += (str(inicio.value) + "-")
            string = self.emOrdem(inicio.direita, string)
        return string

    # pos ordem
    def posOrdem(self, inicio, string):
        if inicio:
            string = self.posOrdem(inicio.esquerda, string)
            string = self.posOrdem(inicio.direita, string)
            string += (str(inicio.value) + "-")
        return string

    def print_arvore(self, arvore):
        if arvore == "pre":
            return print(self.preordem(self.root, ""))
        elif arvore == "em":
            return print(self.emOrdem(self.root, ""))
        elif arvore == "pós":
            return print(self.posOrdem(self.root, ""))
