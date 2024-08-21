class DispositivoEletronico:
    def __init__(self, nome='Desconhecido', marca='Desconhecido', qtd_armazenamento=0):
        self.nome = nome
        self.marca = marca
        self.qtd_armazenamento = qtd_armazenamento

    def get_nome(self):
        return self.nome

    def set_nome(self):
        novo_nome = str(input('Digite o novo nome:'))
        while isinstance(novo_nome, int):
            novo_nome = str(input('Digite o novo nome:'))
        self.nome = novo_nome

    def get_marca(self):
        return self.marca

    def set_marca(self):
        nova_marca = str(input('Digite a nova marca:'))
        while isinstance(nova_marca, int):
            nova_marca = str(input('Digite a nova marca:'))
        self.marca = nova_marca

    def get_qtd_armazenamento(self):
        return self.qtd_armazenamento

    def set_qtd_memoria(self):
        nova_qtd_armazenamento = int(
            input('Digite a nova quantidade de memória (em GB):'))
        while nova_qtd_armazenamento < 0:
            nova_qtd_armazenamento = int(
                input('Digite a nova quantidade de memória:'))
        self.qtd_armazenamento = nova_qtd_armazenamento

    def dados(self):
        return f'O produto {self.marca} {self.nome} tem {self.qtd_armazenamento} GB de armazenamento.'


class Smartphone(DispositivoEletronico):
    def __init__(self, nome, marca, qtd_armazenamento, qtd_cameras=1):
        super().__init__(nome, marca, qtd_armazenamento)
        self.qtd_cameras = qtd_cameras

    def get_qtd_cameras(self):
        return self.qtd_cameras

    def set_qtd_cameras(self):
        nova_qtd_cameras = int(
            input('Digite quantas câmeras o smartphone tem:'))
        while nova_qtd_cameras < 0:
            nova_qtd_cameras = int(
                input('Digite quantas câmeras o smartphone tem:'))
        self.qtd_cameras = nova_qtd_cameras

    def dados(self):
        return f'O smartphone {self.marca} {self.nome} possui {self.qtd_armazenamento} GB de armazenamento e tem {self.qtd_cameras} câmeras.'


class Notebook(DispositivoEletronico):
    def __init__(self, nome, marca, qtd_armazenamento, placa_video):
        super().__init__(nome, marca, qtd_armazenamento)
        self.placa_video = placa_video

    def get_placa_video(self):
        return self.placa_video

    def set_placa_video(self):
        nova_placa_video = input('Digite a nova placa de vídeo:')
        self.placa_video = nova_placa_video

    def dados(self):
        return f'O notebook {self.marca} {self.nome} possui {self.qtd_armazenamento} GB de armazenamento e sua placa de vídeo é a {self.placa_video}.'


if __name__ == '__main__':
    a1 = DispositivoEletronico('Galaxy Tab S6', 'Samsung', 128)
    a2 = Smartphone('Iphone 13', 'Apple', 256, 2)
    a3 = Smartphone('Galaxy S23', 'Samsung', 128, 3)
    a4 = Notebook('G15-i1200-A20P', 'Dell', 512, 'RTX 3050')
    a5 = Notebook('AN515-57-585H', 'Acer', 1000, 'GTX 1650')

    print(a1.dados())
    print(a2.dados())
    print(a3.dados())
    print(a4.dados())
    print(a5.dados())
