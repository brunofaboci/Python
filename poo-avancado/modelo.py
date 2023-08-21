class ProgramaTV:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return "{} - {} - {}".format(self._nome, self.ano, self._likes)


class Filme(ProgramaTV):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return "{} - {} - {} min - {} Likes".format(self._nome, self.ano, self.duracao, self._likes)


class Serie(ProgramaTV):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return "{} - {} - {} temporadas - {} Likes".format(self._nome, self.ano, self.temporadas, self._likes)


vingadores = Filme('vingadores - guerra infinita', 2018, 120)
vingadores.like()

got = Serie('GoT', 2014, 7)
got.like()

filmes_e_series = [vingadores, got]

for programa in filmes_e_series:
    print(programa)
