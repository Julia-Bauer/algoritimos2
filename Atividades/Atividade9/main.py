# Implemenrar as classes no diagrama a seguir, considerando os modificadores de acesso de cada atributo e método

#   ---------------------------------
#   -             PESSOA            -
#   ---------------------------------
#   -   - código: int               - 
#   -   + nome: string              -
#   -   # endereço: string          -
#   -   - telefone: string          - 
#   ---------------------------------
#   -   +imprimeNome(): sring       -
#   -   -imprimeTelefone(): void    -
#   ---------------------------------
#
#   ----------------------      ----------------------------
#   -        FÍSICA      -      -        JURÍDICA          -
#   ----------------------      ----------------------------
#   -   - cpf: string    -      -  - cnpj: string          -
#   -   + idade: int     -      -  - inscricaoEstadual: str-
#   -   + peso: double   -      -  + quantFuncionarios: int- 
#   -   + altura: double -      ----------------------------
#   ----------------------      -  + imprimeCNPJ(): void   -
#   - + imprimeCPF(): str-      -  - emiteNotaFisc(): void -
#   - - calculaIMC(): flt-      ----------------------------
#   ----------------------

from pessoa import Pessoa

p = Pessoa()
p.setNome('Maria')
p.imprimeNome()
