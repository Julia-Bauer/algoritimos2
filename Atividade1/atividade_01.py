nomes = ["lápis", "caderno", "caneta"]
precos = ["R$2.20", "R$32.90", "R$1.22"]
quantidades = ["56","20","3"]

def imprimirProduto(posicaoLista):
    print(f'O produto {nomes[posicaoLista]}, com estoque de {quantidades[posicaoLista]}unidades, custa {precos[posicaoLista]}.')

def excluirItem(posicaoLista):
    del nomes[posicaoLista]
    del quantidades[posicaoLista]
    del precos[posicaoLista]
