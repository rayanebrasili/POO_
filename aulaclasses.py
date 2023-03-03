# class Pessoa:
#     nome = "Rayane"
#     email = "teste@gmail.com"
#
#     p = Pessoa()
#     print(p.nome)
#     print(p.email)
#
#     class Pessoa:
#         def exibir(self):
#             print(self.nome)

#####################################################################

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

        def exibir(self):
            print(self.nome)

            p = Pessoa ('Renata')
            p.exibir()
            n = input('digite um nome>> ')
            a = Pessoa(n)
            a.exibir()


