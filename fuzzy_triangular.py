# coding: utf-8
import ConjuntoFuzzyTriangular as fuzzy
import util

print("Escolha qual grupo deseja calcular o grau de pertinência:")
print(" -> 1 para o grupo baixo")
print(" -> 2 para o grupo medio")
print(" -> 3 para o grupo alto")

num_conjunto = raw_input()
nome_conjunto = util.getVariavelLinguistica(num_conjunto)
print("Conjunto " + nome_conjunto + " escolhido \n")

altura = raw_input("Qual a altura? ")

conjunto = fuzzy.get_valores_conjunto(num_conjunto)
pertinencia = fuzzy.calcula_pertinencia(conjunto, altura)
print("Pertinência: " + str(pertinencia))
print("\n")

step = raw_input("Valor para step: ")
fuzzy.calcula_pertinencia_para_um_intervalo(conjunto, step)
print("\n")

suporte = fuzzy.calcula_suporte(conjunto)
print('O intervalo de suporte para o conjunto ' + nome_conjunto + ' é: ' + suporte)

nucleo = fuzzy.calcula_nucleo(conjunto)
print('O núcleo do conjunto ' + nome_conjunto + ' é: ' + nucleo)

altura = fuzzy.calcula_altura(conjunto)
print('A altura do conjunto ' + nome_conjunto + ' é: ' + str(altura))

alfa_corte = raw_input('Valor para alfa-corte: ')
conjunto_alfa_corte = fuzzy.calcula_alfa_corte(conjunto, alfa_corte)
print('O intervalo correspondente ao alfa-corte é:' + conjunto_alfa_corte)

print("\n\n")
conjunto_baixo = fuzzy.get_valores_conjunto('1')
conjunto_medio = fuzzy.get_valores_conjunto('2')
conjunto_alto = fuzzy.get_valores_conjunto('3')

grau_inclusao_baixo_medio = fuzzy.calcula_grau_de_inclusao(conjunto_baixo, conjunto_medio)
grau_inclusao_medio_alto = fuzzy.calcula_grau_de_inclusao(conjunto_medio, conjunto_baixo)
print('Grau de inclusão do conjunto baixo no conjunto médio: ' + str(grau_inclusao_baixo_medio))
print('Grau de inclusão do conjunto médio no conjunto alto: ' + str(grau_inclusao_medio_alto))
