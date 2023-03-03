class Aluno:
    def __init__(self, ra, nome, celular):
        self.ra = ra
        self.nome = nome
        self.celular = celular

    def __str__(self):
        super.__str__()

class AlunosManager:

    self.alunos = []

    def insereAluno(self, aluno: Aluno):
        self.alunos.append(aluno)

    def consultarAlunoPorRA(self, ra: str):
        for aluno in self.alunos:
            if ra == aluno.ra:
                return aluno
        return None

    def buscaTodosAlunos(self):
        return self.alunos

if __name__ == '__main__':
    manager = AlunosManager()

    while True:

        print("Bem vindo ao programa")
        print("O que deseja? ")
        print("1 - Consultar \n"
              "2 - Listar Alunos \n"
              "3 - Inserir Alunos \n"
              "Outros - Encerrar \n"
              "-> ")
        option = input()

        if option == 1:
            ra = input("Insira o ra a ser pesquisado: -> ")
            alunoEncontrado = manager.consultarAlunoPorRA(ra)
            if alunoEncontrado == None:
                print("Aluno não encontrado")
                continue

            print(alunoEncontrado)
            continue

        if option == 2:
            for aluno in manager.buscaTodosAlunos():
                print(aluno)
                continue

        if option == 3:
            nomeAluno = input("Insira o nome do aluno: -> ")
            raAluno = input("Insira o ra do aluno: -> ")
            celularAluno = input("Insira o celular do aluno: -> ")

            novoAluno = Aluno(raAluno, nomeAluno, celularAluno)

            manager.insereAluno(novoAluno)
            continue

        print("Fim do programa")

        break

# 1 - Inserir aluno
# 2 - Consultar Aluno
# 3 - Listar Alunos
# 4 - Encerrar