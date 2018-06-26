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
misterioso3 = [0, 0, 1]

marcacao_teste = [-1, 1,-1]

testes = [misterioso1, misterioso2, misterioso3]
resultado = modelo.predict(testes)


# vamos definir quais o algoritimo acertou, logo faremos uma subtracao entre vetores.
# resultado - marcacaO_teste
# Aqui ele vai pegar cada elemento em suas respectivas casas e subtratir
# -1 -1 => -1 - -1 => -1 +1 = 0
#  1  1 =>  1 - 1 => 0
# -1  1 => -1 - 1 => -2
# Então se o resultado = 0 (pela nossa conta) o resultado foi acerto e qualquer coisa dif de zero o algoritimo errou
diferenca  = resultado - marcacao_teste
# se imprimirmos a diference, veremos a conta efetuada

# Precisamos testar nosso codigo, se ele realmente é bom, logo pegaremos o total de acertos e total de erros
# para isso usaremos a variavel diferenca onde sabemso quais elementos estao corretos

# arrays dos acertos
acertos = [d for d in diferenca if d == 0]

#total de elementos Len
total_acertos = len(acertos)
total_elementos = len(testes)

#agora podemos calcular a taxa de acertos
taxa_de_acertos = 100.0 * (total_acertos / total_elementos) 

print(taxa_de_acertos)






