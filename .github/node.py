class Node:

    def __init__(self, value, direita=None, esquerda=None):
        self.value = value
        self.direita = direita
        self.esquerda = esquerda

    def Direita(self, direita):
        self.direita = direita

    def Esquerda(self, esquerda):
        self.esquerda = esquerda

    def Esquerda(self):
        return self.esquerda

    def Direita(self):
        return self.direita