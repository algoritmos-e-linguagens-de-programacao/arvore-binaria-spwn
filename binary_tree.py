from node import Node

ROOT = "root"

class BinaryTree:

    def __init__(self):
        self.root = None

    def adicionar(self, value):
        pai = None
        aux = self.root
        while(aux):
            pai = aux
            if value < aux.data:
                aux = aux.esquerda
            else:
                aux = aux.direita
        if pai is None:
            self.root = Node(value)
        elif value < pai.data:
            pai.esquerda = Node(value)
        else:
            pai.direita = Node(value)
        
    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.esquerda:
            node = node.esquerda
        return node.data

    def buscar(self, value, node = ROOT):
        if node == ROOT:
            node = self.root
            if node == self.root:
                return self.root
            elif (node < self.root):
                return self.buscar(node.esquerda, value)
            else:
                return self.buscar(node.direita, value)

    def minimo(self, node = ROOT):
        if node == ROOT:
            node = self.root
        while node.esquerda:
            node = node.esquerda
        return node

    def remover(self, value, node = ROOT):
        if node == ROOT:
            node = self.root
        if node is None:
            return node
        if value < node.data:
            node.esquerda = self.remover(value, node.esquerda)
        elif value > node.data:
            node.direita = self.remover(value, node.direita)
        else:
            if node.esquerda is None:
                return node.direita
            elif node.direita is None:
                return node.esquerda
            else:
                substituto = self.minimo(node.direita)
                node.data = substituto
                node.direita = self.remover(substituto, node.direita)

        return node

    #impressão de arvores

        # pre ordem 
    def preOrdem(self, node = None):
        if node is None:
            node = self.root
            print(node.data)
            self.preOrdem(node.esquerda)
            self.preOrdem(node.direita)

    # em ordem 
    def emOrdem(self, node = None):
        if node is None:
            node = self.root
        if node.esquerda:
            self.emOrdem(node.esquerda)
        print(node.data)
        if node.direita:
            self.emOrdem(node.direita)

    # pos ordem
    def posOrdem(self, node = None):
        if node is None:
                node = self.root
        if node.esquerda:
                self.posOrdem(node.esquerda)
        if node.direita:
            self.posOrdem(node.direita)
        print(node.data)
