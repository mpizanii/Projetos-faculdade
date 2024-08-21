from abc import ABC, abstractmethod


class Produto(ABC):
    quantidade_instancias = 0

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        Produto.quantidade_instancias += 1

    @abstractmethod
    def descricao(self):
        pass

    @abstractmethod
    def calcular_desconto(self, percentual):
        pass

    @classmethod
    def consultar_quantidade_instancias(cls):
        return cls.quantidade_instancias


class Eletronico(Produto):
    def __init__(self, nome, preco, marca):
        super().__init__(nome, preco)
        self.marca = marca

    def descricao(self):
        return f"{self.nome} da marca {self.marca}, preço: R${self.preco:.2f}"

    def calcular_desconto(self, percentual):
        return self.preco * (1 - percentual / 100)


class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor

    def descricao(self):
        return f"{self.nome}, escrito por {self.autor}, preço: R${self.preco:.2f}"

    def calcular_desconto(self, percentual):
        return self.preco * (1 - percentual / 100)


class Roupa(Produto):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def descricao(self):
        return f"{self.nome} (tamanho {self.tamanho}), preço: R${self.preco:.2f}"

    def calcular_desconto(self, percentual):
        return self.preco * (1 - percentual / 100)


eletronico1 = Eletronico("Smartphone", 2000.00, "Samsung")
print(eletronico1.descricao())
print("Preço com 10% de desconto:", eletronico1.calcular_desconto(10))

livro1 = Livro("O Pequeno Príncipe", 50.00, "Antoine de Saint-Exupéry")
print(livro1.descricao())
print("Preço com 20% de desconto:", livro1.calcular_desconto(20))

roupa1 = Roupa("Camiseta", 30.00, "M")
print(roupa1.descricao())
print("Preço com 15% de desconto:", roupa1.calcular_desconto(15))
print("Quantidade de produtos instanciados:",
      Produto.consultar_quantidade_instancias())
