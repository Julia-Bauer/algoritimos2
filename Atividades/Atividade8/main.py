#Exercício

#Construa um algorítimo para implementar a classe Aluno (código, nome, matrícula). A classe Aluno possui duas subclasses, a classe AluEnsinoMedio(ano) e AlunoGraduacao(semestre). As 3 classes possuem o métodp construtor e também o método imprimir(), que imprime na tela os valores de todos os atributos da sua classe.

from aluno import Aluno
from medio import AluEnsinoMedio
from graduacao import AlunoGraduacao

a = Aluno("001", "Ana Carolina", "111")

m = AluEnsinoMedio("002", "Anita", "112", "3")

g = AlunoGraduacao("003", "Betina", "113", "8")

a.imprimir()
m.imprimir()
g.imprimir()