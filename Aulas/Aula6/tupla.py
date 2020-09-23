carros = ("Uno", "Doblo", "Toro", "Hylux", "Ferrari")
print(carros[1])
print("-------------------------------")

for car in carros:
    print(car)

print("-------------------------------")

print(carros[1:2])

print("-------------------------------")

print(carros[1:3])

print("-------ORDENADO-------")

print( sorted(carros))

print("---------FOR-COM-RANGE---------")

for car in range( len(carros) - 2 ):

    print("posição" + str(car) + ":" + carros[car])

print("-------USANDO-FUNÇÃO-------")

def calcular(x, y):
    return(x+y), (x-y), (x*y), (x/y)

print (calcular(5, 2))

print("-------------------------------")

vet = [1,5,20]
vet = [100,50,20,60]
vet[1] = 10
vet.sort()
print(vet)

