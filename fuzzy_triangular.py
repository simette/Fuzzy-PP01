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

step = raw_input("Valor para step: ")
fuzzy.calcula_pertinencia_para_um_intervalo(conjunto, step)

suporte = fuzzy.calcula_suporte(conjunto)
print('O intervalo de suporte para o conjunto ' + nome_conjunto + ' é: ' + suporte)

nucleo = fuzzy.calcula_nucleo(conjunto)
print('O núcleo do conjunto ' + nome_conjunto + ' é: ' + nucleo)

alfa_corte = raw_input('Valor para alfa-corte: ')
conjunto_alfa_corte = fuzzy.calcula_alfa_corte(conjunto, alfa_corte)
print('O intervalo correspondente ao alfa-corte é:' + conjunto_alfa_corte)
