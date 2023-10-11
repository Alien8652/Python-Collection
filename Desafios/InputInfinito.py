#coding:latin-1

def inputMap(funcao,mensagem,msg_erro='Erro:\n Entrada inv�lida! Insira um valor v�lido pro tipo de dado requerido!\n'):
    try:
        valor=funcao(input(mensagem))
    except ValueError: # Exception:
        if msg_erro!=''or msg_erro!=None:print(msg_erro,end='')
        valor=inputMap(funcao,mensagem,msg_erro)
    return valor

#Poss�veis tipos de dados:int,str(esse daqui n�o precisa),bool,float ou uma fun��o pr�pria definida:
#Fun��o pr�pria: converte entrada pra inteiro e se n�o for um n�mero par volta um erro(ValueError).
#def intPar(entrada):
# n=int(entrada)
# if n%2!=0:raise ValueError()
# return n
#inputMap(intPar,'....
resultado=inputMap(int,'Digite um n�mero: ',msg_erro='\nInsira somente n�meros inteiros(0-9)!\n\n')
print(resultado)
print(type(resultado))
