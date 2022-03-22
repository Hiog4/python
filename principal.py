#principal.py

from veiculo import*

def principal():
    veiculo=Veiculo('Marca', 'Modelo', 'placa', 2020)

    carro=Carro('VW', 'Polo', 'ABC-1234', 2015)
    moto=Motocicleta('Honda', 'CG-160', 'MMM-3214', 2021, 600)

    veiculo.abastecer()
    print(veiculo)

    carro.abastecer()
    print(carro)

    moto.abastecer()
    print(f'Placa da moto: {moto.placa}')
    print(f'Cilindrada da moto: {moto.cilindrada}')

    lista=[veiculo, carro, moto, 'banana', 123, 1.0]
    for item in lista:
        if(isinstance(item, Carro)):
            print('Temos um carro na lista')
        elif(isinstance(item, Motocicleta)):
            print('Temos uma motocicleta na lista')
        elif(isinstance(item, Veiculo)):
            print('Temos um veiculo na lista')
        elif(isinstance(item, int)):
            print('Temos um int na lista')
        elif(isinstance(item, str)):
            print('Temos um str na lista')
        else:
            print('Item desconhecido na lista')
    

if __name__=='__main__':
    principal()


