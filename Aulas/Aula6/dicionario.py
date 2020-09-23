pessoa = {
    "nome" : "Júlia",
    "idade" : 11,
    "email" : "m@mail.com"
}

print(pessoa)

print(pessoa["nome"])

pessoa["altura"] = 1.3

print(pessoa)

pessoa["terminouTema"] = True

print(pessoa)

if pessoa["terminouTema"] : 
    print("parabéns!")
else:
    print("Sem Refrigerante")

del pessoa["idade"]

print(pessoa)

pessoa2 = {
    "nome" : "Maria",
    "idade" : 25,
    "altura" : 1.75,
    "terminouTema" : False,    
    "email" : "m@mail.com"
}

listPessoas = pessoa, pessoa2

print(listPessoas)