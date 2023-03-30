#coding:latin-1

#Uso:
# [py|python] FastPortScan.py 127.0.0.1 80 443
import socket,sys
portas_comuns={20:'Porta de dados do servi�o FTP(Protocolo de transfer�ncia de arquivos)',21:'Porta do protocolo do servi�o FTP de transfer�ncia de arquivos',25:'Porta SMTP para envio de emails',80:'Protocolo HTTP(Site ou servi�o da Internet)',443:'Protocolo HTTPS(Site ou servi�o da Internet com protocolo de seguran�a refor�ado)',8008:'Alternativa ao HTTP(Servi�o da Internet)',8080:'Alternativa ao HTTP(Servi�o da Internet)'}
argv=sys.argv
endereco=''
inicio,fim=-1,-1
def fastPortScan(endereco,inicio=0,fim=65535,timeout=0.3):
    for porta in range(inicio,fim):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as soquete:
            soquete.settimeout(timeout)
            if not soquete.connect_ex((endereco,porta)):#not 0==True
                print('---['+(f'{porta} - {portas_comuns[porta]}'if porta in portas_comuns.keys()else str(porta))+']')
                soquete.close()

if len(argv)!=1:
    endereco=argv[1]
    inicio=argv[2]
    fim=argv[3]
else:
    endereco=input('Host(Endere�o IP):')
    inicio=input('Inicio(-1 ou apenas enter para  valor padr�o 0):')
    fim=input('Fim(-1 ou apenas enter para  valor padr�o 65535):')


if inicio=='-1' or inicio=='':inicio='0'
if fim=='-1' or fim=='':fim='65535'
try:
    inicio=int(inicio)
    fim=int(fim)
except:
    inicio=0
    fim=65535

print(f'Escaneando porta {inicio} at� {fim} do endere�o {endereco}...')
fastPortScan(endereco,inicio,fim)
