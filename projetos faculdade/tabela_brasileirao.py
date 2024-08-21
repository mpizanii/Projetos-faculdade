import time


class Time:
    def __init__(self, nome, posicao, pontos, jogos):
        self.nome = nome
        self.posicao = posicao
        self.pontos = pontos
        self.jogos = jogos

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_posicao(self):
        return self.posicao

    def set_posicao(self, nova_posicao):
        self.posicao = nova_posicao

    def get_pontos(self):
        return self.pontos

    def set_pontos(self, novos_pontos):
        self.pontos = novos_pontos

    def get_jogos(self):
        return self.jogos

    def set_jogos(self, novos_jogos):
        self.jogos = novos_jogos

    def return_data(self):
        data = f'{self.nome} está na {self.posicao}° posição com {
            self.pontos} pontos, jogando {self.jogos} jogos'
        return data


time1 = Time('Botafogo', 1, 51, 21)
time2 = Time('Palmeiras', 2, 40, 21)
time3 = Time('Grêmio', 3, 36, 20)
time4 = Time('Flamengo', 4, 36, 21)
time5 = Time('Fluminense', 5, 35, 21)
time6 = Time('Bragantino', 6, 35, 21)

print(f'{time1.return_data()}\n{time2.return_data()}\n{time3.return_data()}\n{
      time4.return_data()}\n{time5.return_data()}\n{time6.return_data()}')

time.sleep(5)
