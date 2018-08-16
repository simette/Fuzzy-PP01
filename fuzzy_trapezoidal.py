# coding: utf-8
import ConjuntoFuzzyTrapezoidal as fuzzy
import util

print("Escolha qual grupo deseja calcular o grau de pertinência:")
print(" -> 1 para o grupo baixo")
print(" -> 2 para o grupo medio")
print(" -> 3 para o grupo alto")

num_conjunto = raw_input()
nome_conjunto = util.getVariavelLinguistica(num_conjunto)

print("Grupo " + nome_conjunto + " escolhido \n")

altura = raw_input("Qual a altura? ")

conjunto = fuzzy.get_valores_conjunto(num_conjunto)
pertinencia = fuzzy.calcula_pertinencia(conjunto, altura)
print("A pertinência da altura " + str(altura) + " para o conjunto " + nome_conjunto + " é: " + str(pertinencia))

step = raw_input("\nValor para s: ")
fuzzy.calcula_pertinencia_para_um_intervalo(conjunto, step)

print("\n\n")
ini_suporte, fim_suporte = fuzzy.calcula_suporte(conjunto)
print('O intervalo de suporte para o conjunto ' + nome_conjunto + ' é: [' + str(ini_suporte) + ', ' + str(fim_suporte) + ']')

ini_nucleo, fim_nucleo = fuzzy.calcula_nucleo(conjunto)
print('O núcleo do conjunto ' + nome_conjunto + ' é: [' + str(ini_nucleo) + ', ' + str(fim_nucleo) + ']')

altura = fuzzy.calcula_altura(conjunto)
print('A altura do conjunto ' + nome_conjunto + ' é: ' + str(altura))

alfa_corte = raw_input('Valor para alfa-corte: ')
ini_alfa_corte, fim_alfa_corte = fuzzy.calcula_alfa_corte(conjunto, alfa_corte)
print('O intervalo correspondente ao alfa-corte é: [' + str(ini_alfa_corte) + ', ' + str(fim_alfa_corte) + ']')

print("\n\n")
conjunto_baixo = fuzzy.get_valores_conjunto('1')
conjunto_medio = fuzzy.get_valores_conjunto('2')
conjunto_alto = fuzzy.get_valores_conjunto('3')

grau_inclusao_baixo_medio = fuzzy.calcula_grau_de_inclusao(conjunto_baixo, conjunto_medio)
grau_inclusao_medio_alto = fuzzy.calcula_grau_de_inclusao(conjunto_medio, conjunto_baixo)
print('Grau de inclusão do conjunto baixo no conjunto médio: ' + str(grau_inclusao_baixo_medio))
print('Grau de inclusão do conjunto médio no conjunto alto: ' + str(grau_inclusao_medio_alto))
