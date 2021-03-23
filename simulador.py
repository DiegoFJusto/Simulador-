from time import sleep


def linhamenu():
    print('#$#' * 42)


def linhacomum():
    print('--' * 42)


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mERRO: Usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mERRO: Usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def iniciar():
    menu = 'N'
    while menu == 'N':

        linhamenu()
        print('SISTEMA DE CÁLCULOS DE JUROS COMPOSTOS')
        linhamenu()

        capitalOrigin = leiaFloat('Digite o valor do Capital [ $ ] :')
        linhacomum()

        capital = capitalOrigin
        juros = leiaInt('Digite os juros estimados no mês [ % ]:')
        linhacomum()

        corretagem = leiaInt('Digite a corretagem no mês [ % ]:')
        print(f'os cálculos já serão contabilizados com a corretagem de {corretagem} % ')
        corretagem = corretagem / 100
        linhacomum()

        meta = float(input('Digite o alvo [ $ ]:'))
        linhacomum()

        juros = juros / 100
        jrs = juros * corretagem
        mes = 0

        while capital < meta:
            rendimento = capital * jrs
            capital = capital + rendimento
            mes += 1
            print(f'Mes {mes} : Capital R$ {capital:.2f} ')
            linhacomum()
            sleep(0.02)

        print('')
        linhamenu()
        print(f'O total do Capital investido foi : {capitalOrigin}')
        linhacomum()
        ano = (mes // 12)
        sobra = (mes % 12)
        while sobra >= 12:
            anoextra = sobra // 12
            sobra = anoextra
        print(f'O total de meses para a meta foi : {mes} ou seja : {ano} anos e {sobra} meses')
        linhacomum()
        print(f'O total de Lucros no período foi : {(capital - capitalOrigin):.2f}')
        linhacomum()

        linhamenu()

        menu = input('Deseja sair do sistema [ S ] ou [ N ] :').upper().strip()
        while menu != 'S' and menu != 'N':
            print('Opção inválida !')
            menu = input('Deseja sair do sistema [ S ] ou [ N ] :').upper().strip()
        if menu == 'S':
            linhacomum()
            print('Saindo do Sistema')
            linhacomum()
            sleep(1)
            print('Obrigado por usar nosso sistema')
            linhamenu()
            sleep(1)
        elif menu == 'N':
            iniciar()

iniciar()