    from ControleRemoto import Televisor

    smartTV = Televisor(5, 20, 10, 100)
    smartTV.exibir()
    smartTV.LigaDesliga()
    smartTV.exibir()

    while True:
        op = input('1. Liga/Desliga   \n'
                   '/n2. Canal +      \n'
                   '/n3 Canal -       \n'
                   '/n4 Exibir        \n'
                   '/n5 Encerrar      \n'
                   '/n0 opção >>')

        if op == 1:
            smartTV.LigaDesliga()

        elif op == 2:
            smartTV.canalAcima()

        elif op == 3:
            smartTV.canalAbaixo()

        elif op == 4:
            smartTV.exibir()

        elif op == 5:

            break
















