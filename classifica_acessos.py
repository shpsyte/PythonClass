from getDataCSV import load_data
from sklearn.naive_bayes import MultinomialNB

X,Y = load_data()


modelo = MultinomialNB()
modelo.fit(X, Y)

pessoa1 = [1,0,1]
pessoa2 = [0,0,1]

all_pessoas = [pessoa1, pessoa2]

resultado = modelo.predict(X)
diferenca = resultado - Y

acertos = [d for d in diferenca if d == 0]

total_acertos = len(acertos)
total_elementos = len(resultado)

taxa_de_acertos = 100.0 * (total_acertos / total_elementos) 

print(taxa_de_acertos)

