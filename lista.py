#arquivo_texto.py

#modo para leitura e gravação de arquivos
#r= read = somente leitura
#w= write = escrita (perde oque já tem no artquivo)
#a= append = anexa dados (nao perde)

#tipos de arquivos: Texto ou binário

lista=[]

def entrada():
    quant=int(input('Quantas frutas você quer digitar?'))
    for x in range (1, quant +1):
        fruta=input(f'Digita a fruta {x}:')
        lista.append(fruta)

    print(lista)

def gravar():
    arquivo=open('frutas.txt', 'w')
    for fruta in lista:
        arquivo.write(fruta + '\n')

    arquivo.close()

def anexar():
    arquivo = open('frutas.txt', 'a')
    for fruta in lista:
        arquivo.write(fruta +'\n')
    


def ler():
    arquivo = open('frutas.txt', 'r')
    for linha in arquivo:
        print(linha)

     
if(__name__=='__main__'):
    entrada()
    #gravar()
    #ler()
    anexar()
