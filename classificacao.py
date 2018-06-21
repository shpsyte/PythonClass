# gordinho ? tem perninha curta ? faz auau ?

# array
porco1 =    [1, 1, 0]
porco2 =    [1, 1, 0]
porco3 =    [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

# conjunto das array
dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

# macacoes
marcacoes = [1, 1, 1, -1, -1, -1]


from sklearn.naive_bayes import MultinomialNB

#Crate a variable using MultinomialNB
modelo = MultinomialNB()

# Treia os dados,com base na marcacao
modelo.fit(dados, marcacoes)

# tenta adivinhar o que o mistoerioso é, com base na marcacao e treino do nosso modelo
misterioso1 = [1, 1, 1]
misterioso2 = [1, 1, 0]
misterioso3 = [1, 0, 0]

teste = [misterioso1, misterioso2, misterioso3]
print(modelo.predict(teste))


