import csv

def load_data():
    X = []
    Y = []

    arquivo = open('acesso_pagina.csv', 'r')
    reader  = csv.reader(arquivo)
    next(reader)
    
    for home,como_funciona,contato,comprou in reader:
        dados = [int(home), int(como_funciona), int(contato)]

        X.append(dados)
        Y.append(int(comprou))

    return X, Y