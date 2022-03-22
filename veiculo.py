#veiculo.py


#classe mãe
class Veiculo:

    #construtor ou inicializador
    def __init__(self, marca, modelo, placa, ano):
        self.marca=marca
        self.modelo=modelo
        self.placa=placa
        self.ano=ano


    def ligar(self):
        print ('Veívulo ligado...')

    def abastecer(self):
        print ('Veículo abastecendo...')

    #funções builtin: funções prontas que iniciam por __XXX__
    def __str__(self):
        return 'Placa do veiculo: '+ self.placa
    
#carro é um veículo
#classe filha
class Carro(Veiculo):
    def __init__(self, marca, modelo, placa, ano):
        super().__init__(marca, modelo, placa, ano)

    #sobreescreve a função da classe mãe
        def __str__(self):
            return 'Placa do carro:' + self.placa

            
class Motocicleta(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cilindrada):
        super().__init__(marca, modelo, placa, ano)
        self.cilindrada=cilindrada


#v=Veiculo()
#v.ligar()
#v.abastecer()
