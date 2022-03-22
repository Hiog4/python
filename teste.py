#matriz.py
print("Matriz usando lista...")

matriz=[
    [3, 2, 6],  #sublista - linha da matriz
    [3, 3, 8],
    [1, 2, 5]
    ]
for linha in matriz:
    print(linha)


lin=int(input('Número da linha' ))
col=int(input('Número da coluna' ))
print(matriz[lin][col])


#criando u8ma matriz por multiplicação
linha=[0]*5  #5colunas
matriz=[linha]*3   #3linhas
print(matriz)
