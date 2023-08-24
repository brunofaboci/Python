class Funcionario:
    def __init__(self, nome):
        self.nome = nome
    def registra_horas(self, horas):
        print("{} registradas".format(horas))

    def mostra_tarefas(self):
        print("mostrou")


class Caelum(Funcionario):
    def mostra_tarefas(self):
        print("mostrou")

    def busca_curso_do_mes(self, mes=None):
        print("Cursos {}".format(mes) if mes else "Curso do mês atual")


class Alura(Funcionario):
    def mostra_tarefas(self):
        print("mostrou")

    def buscar_perguntas_sem_resposta(self):
        print("buscando...")


class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'


class Junior(Alura):
    pass


class Pleno(Alura, Caelum):
    pass


class Senior(Alura, Caelum, Hipster):
    pass


jose = Junior('jose')
jose.mostra_tarefas()

joao = Pleno('joao')
joao.busca_curso_do_mes()
joao.buscar_perguntas_sem_resposta()

maria = Senior('maria')
print(maria)
