#----------------------PARADIGMA----------------------

#Paradigma é uma fora de abordar um problema

#No contexto da modelagem de um sistema de software um paradigma tem a ver com forma com que esse sistema é entendido e construido

#-------------------ORIENTACAO-A-OBJETOS-------------------

#O paradigma OO surgiu no fim dos anos 60

#Alan kay um dos pais desse paradigma formulou a analogia biologica.
    #- como seria um sistema de software que funcionase como ser vivo?

#-------------FUNDAMENTOS-DA-ORIENTACAO-A-OBJETO-------------

#-Qualquer coisa é um OBJETOS

#-Objetos realizam tarefas atraves da requisição de servicos a outros Objetos

#-Cada objeto pertence a uma determinada classe. Uma classe agrupa objetos similares

#-A classe é um repositorio para comportamento associado ao objeto

#-Classes são organizadas em hierarquias

#-O paradigma POO visualiza um sistema de software como uma coleção de agentes interconectados chamados objetos

# -Cada objeto é responsavel por realizar tarefas especificas

#-É atraves da interacao entre objetos que uma tarefa computacional é realizada

#-Um sistema de software OO consiste em objetos em colabioração para realizar as funcionalidades do sistema

#----------------------POO----------------------
#aprroximacao dos sistemas de informacao do mundo real. 

#solucao de dificuldades da programacao estruturada
    #-Melhor organização
    #-Escrita de menos linhas
    #-Divisão lógica do código
    #Pode-se trabalhar em vários arquivos
    #-Mais proximo da vida real, simula o mundo real

#***Mas e como fazer a máquina “pensar” como um humano?
#Utilizando conceitos de POO
#Classe
#Objeto
#Atributo - características
#Método - ações
#Herança 
#Polimorfismo - várias formas de fazer a mesma coisa

#-------------------------CLASSE-------------------------

#É o molde ou projeto de qualquer coisa em seu mundo

#São especificações para objetos;

#Representam um conjunto de objetos que compartilham características e comportamentos comuns.

#As classes definem como os objetos devem se parecer e se comportar, ou seja, define as características e funcionalidades.

#Uma classe é um molde para objetos.

#*****Um objeto é uma instância de uma classe*****

#Uma classe possui atributos (características) e métodos(funções/ações)

#----------------CLASSES,-OBJETOS-E-MENSAGENS--------------

#O mundo real é formado de coisas.

#Na terminologia de orientação a objetos, estas coisas do mundo real são denominadas objetos.

#Seres humanos costumam agrupar os objetos para entendê-los

#A descrição de um grupo de objetos é denominada classe de objetos, ou simplesmente de classe.

#---------------CLASSE----------------
#-------------------------------------
#-           Nome da Classe          -
#-       + atributoPublico: tipo     -acessivel no projeto
#-       #atributoProtegido: tipo    -acessivel no pacote
#-       -atributoPrivado: tipo      -acessivel na sua classe
#-------------------------------------
#- + operacao(argumento):tipoRetorno -
#-------------------------------------

#-----------------------------OBJETO------------------------

#É algo do mundo real – concreto ou abstrato

#As percepção dos seres humanos é dada através dos objetos

#Um objeto é uma entidade que exibe algum comportamento bem definido.

#OBJETO = DADOS + OPERAÇÕES

#Um objeto é um exemplar de uma classe. Só existe em tempo de execução. É chamado de instância de classe.

#------CARACTERISTICAS-----
#Características: dados representam características
    #São chamados atributos
    #São as variáveis do objeto.

#-------COMPORTAMENTO------
#Comportamento: operações definem comportamento
    #São os métodos de um objeto
    #São as funções que são executadas por um objeto

#----------------OBJETO-PROPRIEDADES---------------

#Estado

#Representado pelos valores dos atributos de um objeto

#Comportamento

#Definido pelo conjunto de métodos do objeto

#Estado representa o resultado cumulativo de seu comportamento

#Identidade

#Um objeto é único, mesmo que o seu estado seja idêntico ao de outro;

#Seu valor de referência

#Os valores dos DADOS são modificados a partir das OPERAÇÕES sobre estes dados 

#--------------------------GET-SET------------------------

#propcia criar verificações quando necessárias. exemplo: verificar se uma idade é positiva

#GET - Pega uma informação
#SET - Define uma informação

#--------------------------ATRIBUTO-----------------------

#Características dos objetos de uma classe, também são conhecidos como variáveis ou campos

#Essas propriedades definem o estado de um objeto, fazendo com que esses valores possam sofrer alterações

#--------------------------MÉTODO-------------------------

#São ações ou procedimentos, onde podem interagir e se comunicarem com outros objetos. A execução dessas ações se dá através de mensagens, tendo como função o envio de uma solicitação ao objeto para que seja efetuada a rotina desejada.

#Como boas práticas, é indicado sempre usar o nome dos métodos declarados como verbos, para que quando for efetuada alguma manutenção seja de fácil entendimento. Veja algumas nomenclaturas de nomes de métodos: acaoVoltar, voltar, avançar, correr, resgatarValor, pesquisarNomes


#-------------------------RESUMO------------------------

#Objeto
    #Qualquer entidade que possui características e comportamento
#Classe
    #Descreve um tipo de objeto
    #Define atributos e métodos
#Atributo
    #Define características do objeto
#Método
    #Operações que o objeto pode realizar 

#----------------------OO-EM-PYTHON---------------------

#Quase tudo em Python é um objeto, com as suas propriedades e métodos.

#Uma classe é como um construtor de objeto, ou um "modelo" para criar objetos

#-----METODO-CONSTRUTOR-DE-CLASSE-----
#Todas as classes têm uma função chamada __init__ (), que é sempre executada quando a classe está sendo inicializada.

#Use o __init__ () para atribuir valores a propriedades do objeto, ou outras operações que são necessárias para fazer quando o objeto está sendo instanciado.

#-----------------------------------------------------------

#*NOME DO MÉTODO COMO VERBO - BOA PRATICA - imprimir, cadastrar, etc...
