#coding:latin-1

# Utils - Gabriel Matheus de Castro(2020)
# Tem boas utilidades, outras n�o t�o ut�is mas que podem servir para o aprendizado, este � um script que mostra como us�-las,
# recomendo para quem est� aprendendo analisar o script Utils.py tamb�m.

#Exemplos de usos abaixo:

from Utils import Texto
#Ou Utils.Texto()


# Chame a classe primeiramente:
tfun=Texto()


# Verificar se um texto � um pal�ndromo
tfun.palindromo('Socorram-me, Subi No �nibus em Marrocos!')

# Inverter um texto
tfun.inverter('Ola Mundo')

# Aumentar, diminuir, transformar em t�tulo o texto inserido
tfun.maiusculo('Ola Mundo')
tfun.minusculo('Ola Mundo')
tfun.titulo('ola mundo')

# Filtra o texto inserido permitindo somente os caracteres do filtro
tfun.filtrar('Testando123','0123456789') # Obt�m somente os n�meros do texto

# � poss�vel definir um filtro dessa forma tamb�m para automatizar a tarefa
tfun.FILTRO='aeiou' # Somente vogais ser�o v�lidas
tfun.filtrar('Ola Mundo')


# Obter uma lista de palavras em um texto
lista_palavras=tfun.getPalavras('Ola mundo, testando 123(Isso � um teste!), palavra-chave')

# Obt�m a quantidade de palavras em um texto inserido
tfun.contar_palavras('Ola mundo, testando 123(Isso � um teste!), palavra-chave')

# Obt�m todos os caracteres da tabela ASCII
AsciiTable=tfun.getAsciiTable()


#Corta o texto a cada numero de caracteres
tfun.cortar_texto('abcdefghijklmnopqrstuv',3)

#Corta o texto a cada caractere-chave
tfun.cortar_texto_por_chave('Ola-Mundo','-')

# Remove caracteres duplicados de um texto
tfun.removerCharDuplicado('aaabbbcccccddefghijkklmnopp')

# Retorna uma tupla com duas listas de palavras mais comuns(repetidas no texto) e quantidade da repeti��o
maisComuns=tfun.mais_comum(lista_palavras)
maisComuns[0] # Palavras
maisComuns[1] # Contagem

# Tamb�m � poss�vel limitar a sa�da, exemplo, as 3 palavras mais comuns do texto
tfun.mais_comum(lista_palavras,3)




# Junta uma lista em uma �nica string
tfun.sJoin(['Ola',' ','Mundo'])

# Remove acentos num texto inserido
tfun.removerAcentos('Ol� M�nd�!')

# � poss�vel limitar para apenas alguns acentos
tfun.removerAcentos('Ol� M�nd�!','��','uo')

# Remove caracteres especiais de um texto
tfun.removerCaracteresEspeciais(':^`[Ola]--{Mundo}')

# Remove n�meros do texto
tfun.removerNumeros('Testando 123')

# Extrai dados de um texto retornando uma array de letras de acordo com a express�o REGEX inserida
tfun.extrairDados('ABCDEFGHI',r'[AEI]')


# Gerador de WordList, sem libs, gera palavras come�ando com a, b, c, aa, ab, ac, etc...
tfun.wordlist('abc',3) # Caracteres, Profundidade



from Utils import TradutorRapido

tr=TradutorRapido()

# Para criar uma tradu��o insira uma array como as chaves e outra array bidimensional com as arrays de tradu��es(Devem ter o mesmo tamanho).
tr.genTrad(['msg_ola'],[['Hello World','Ola Mundo']])
#             Chave       Tradu��o 0    Tradu��o 1

# Mensagem em ingl�s
print(tr.traduzir('msg_ola'))#Padr�o tr.LINGUA.PADRAO=0

# Configure a tradu��o manualmente
tr.LINGUA.PORTUGUES=1
tr.setLingua(tr.LINGUA.PORTUGUES)

# Mensagem em portugu�s.
print(tr.traduzir('msg_ola')) #Caso ocorra algum erro na tradu��o, seja por m� configura��o das linguagens ou a tradu��o n�o exista, retornar� ''.

# Vari�veis acess�veis pela classe Texto e seus valores
LETRAS_VOGAIS='aeiou'
LETRAS_CONSOANTES='bcdfghjklmnpqrstvwxyz'
LETRAS_ALFABETO='abcdefghijklmnopqrstuvwxyz'
LETRAS_ALFABETO_COM_ACENTOS='aáàâãäbcçdeéèêëfghiíìîïjklmnñoóòôõöpqrstuúùûüvwxyýÿz'
LETRAS_ACENTUADAS='áéíóúàèìòùÁÉÍÓÚÀÈÌÒÙãõñÃÕÑâêîôûÂÊÎÔÛäëïöüÄËÏÖÜÿýÝçÇ'
LETRAS_SEM_ACENTOS='aeiouaeiouAEIOUAEIOUaonAONaeiouAEIOUaeiouAEIOUyyYcC'
NUMEROS='0123456789'
NUMEROS_SOBRESCRITOS='⁰¹²³⁴⁵⁶⁷⁸⁹'
NUMEROS_SUBSCRITOS='₀₁₂₃₄₅₆₇₈₉'
SINAIS_MATEMATICOS_SIMPLES='+−×÷'
SINAIS_MATEMATICOS_AVANCADOS='√±Σ'
SIMBOLOS_SOBRESCRITOS='⁺⁻⁼⁽⁾'
SIMBOLOS_SUBSCRITOS='₊₋₌₍₎'
ACENTOS='´`^~¨'
SIMBOLOS='(){}[]<>.,-_;:|\\/#!?*@&%$=+\'"�'
ESPACO=' '
GRAUS='°'
INDICADOR_ORDINAL_A='ª'
INDICADOR_ORDINAL_O='º'
FILTRO=None


#� poss�vel verificar todos os m�todos e classes dentro uma classe-lib com o m�todo dir(classe):
import Utils
dir(Utils)

#Classe n�merica com alguns m�todos da lib math
N=Utils.Numero()

#N�mero PI
N.PI

#Arredonda o valor pro mais pr�ximo(2.4 arredonda pra 2, 2.6 arredonda pra 3)
N.arredondar(2.6)

#Arredonda o valor para menos independente do valor mais pr�ximo(2.6=2)
N.arredondarBaixo(2.6)

N.arredondarCima(2.4)#3

N.raizQuadrada(4)

#Troca o atributo de menos para mais e mais para menos(-2=2)
N.trocar_atributo(-2)

#Troca qualquer valor para positivo+(-0=+0)
N.atribuir_positivo(-2)

N.atribuir_negativo(2)

#Calcula potencia(2^4=2*2*2*2=16)
N.potencia(2,4)

#Soma n�meros de uma lista(2+3+5=10)
N.somar_lista([2,3,5])
