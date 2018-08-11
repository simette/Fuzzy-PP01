# coding: utf-8
import ConjuntoFuzzyTriangular as fuzzy
import util

print("Escolha qual grupo deseja calcular o grau de pertinência:")
print(" -> 1 para o grupo baixo")
print(" -> 2 para o grupo medio")
print(" -> 3 para o grupo alto")

n_grupo = raw_input()
nome_grupo = util.getVariavelLinguistica(n_grupo)
print("Grupo " + nome_grupo + " escolhido \n")

altura = raw_input("Qual a altura? ")

grupo = fuzzy.get_valores_conjunto(n_grupo)
pertinencia = fuzzy.calcula_pertinencia(grupo, altura)
print("pertinencia: " + str(pertinencia))

step = raw_input("Valor para s: ")

x = 0
while(x <= 2):
	pertinencia = fuzzy.calcula_pertinencia(grupo, x)
	print("Valor " + str(x) + " tem pertinência igual a: " + str(pertinencia))
	x = x + float(step)

suporte = fuzzy.calcula_suporte(grupo)
print('O intervalo de suporte para o grupo ' + nome_grupo + ' é: ' + suporte)

nucleo = fuzzy.calcula_nucleo(grupo)
print('O núcleo do grupo ' + nome_grupo + ' é: ' + nucleo)


