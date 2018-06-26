import csv

def load_data():
    X = []
    Y = []

    file = open('history_search.csv','r')
    reader = csv.reader(file)
    next(reader)

    for home,busca,logado,comprou in reader:
        dados = [int(home), busca, int(logado)]
        comprou = [int(comprou)]

        X.append(dados)
        Y.append(comprou)

    return X,Y


