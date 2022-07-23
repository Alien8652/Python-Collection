# coding: latin-1

# Pergunta em loop ao usu�rio com uma mensagem espec�fica.
def perguntar(acoes,opcoes,mensagem=''):
    if (len(acoes)!=len(opcoes)):
        return 'Erro! A quantidade de a��es deve ser igual a de op��es!'
    pergunta=input(mensagem)
    for i in range(0,len(acoes)):
        if pergunta==opcoes[i]:
            return eval(acoes[i])
    return perguntar(acoes,opcoes,mensagem)


# Defina as fun��es primeiro
def funcao0():
    print('Ola Mundo!')
    return 'Fim da funcao0'

def funcao1():
    print(7+7)
    return 'Fim da funcao1'

#Uso:
def exemplo():
    #acoes=['funcao0()','funcao1()']
    #opcoes=['0','1']                   # IMPORTANTE: � melhor usar uma string pra n dar erro
    #mensagem='Digite algum n�mero para executar alguma fun��o\n 0 = funcao0()\n 1 = funcao1()\n>'
    resultado=perguntar(['funcao0()','funcao1()'],
                        ['0','1'],
                        'Digite algum n�mero para executar alguma fun��o\n 0 = funcao0()\n 1 = funcao1()\n>')
    print(resultado)

exemplo()
