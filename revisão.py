def imprimirPi():
    print("valor do Pi:")
    print(3.14)

imprimirPi()

def getSalario():
    return 1045.0

print(getSalario())


def calcular_imprimir_area(largura, comprimento):
    area = float(largura) * float(comprimento)
    print(area)

calcular_imprimir_area(12, 5)

def calcular_area (largura, comprimento):
    area = float(largura) * float(comprimento)
    return area

altura = 5
volume = altura * calcular_area(4, 6)
print(volume)

def calcular_volume(largura, comprimento, artura):
    volume = float(largura) * float(comprimento) * float(altura)
    return volume

portas = 3
def abrirPorta(portas):
    if portas > 0:
        portas -= 1
        print(portas)
        abrirPorta(portas)

abrirPorta(3)

carros = ["Doblo", "Novo Uno", "Sandero"]
print(carros)
print(carros[1])
