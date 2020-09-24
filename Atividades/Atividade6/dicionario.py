nome = input("Nome do aluno:")
 
nota01 = float(input("Nota 01:"))

nota02 = float(input("Nota 02:"))

notaFinal = (nota01 + nota02)/2

aluno = {
    "nome" : nome,
    "nota01" : nota01,
    "nota02" : nota02,
    "notaFinal" : notaFinal
}

print(aluno)