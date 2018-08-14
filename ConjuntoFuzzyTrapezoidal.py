# coding: utf-8


def get_valores_conjunto(numero_conjunto):
	if(numero_conjunto is str(1)):
		return {
			"a": 1,
			"m": 1,
			"n": 0.7,
			"b": 1.5
		}

	if(numero_conjunto == str(2)):
		return {
			"a": 1,
			"m": 1.4,
			"n": 1.6,
			"b": 2
		}

	if(numero_conjunto is str(3)):
		return {
			"a": 1.5,
			"m": 1.8,
			"n": 2,
			"b": 2
		}


def calcula_pertinencia(conjunto, altura):
	altura = float(altura)

	if(altura <= conjunto['a']):
		return 0

	if(conjunto['a'] < altura and altura <= conjunto['m']):
		return (altura - conjunto['a']) / (conjunto['m'] - conjunto['a'])

	if(conjunto['m'] < altura and altura <= conjunto['n']):
		return 1

	if(conjunto['n'] < altura and altura <= conjunto['b']):
		return (conjunto['b'] - altura) / (conjunto['b'] - conjunto['n'])

	if(altura > conjunto['b']):
		return 0


def calcula_pertinencia_para_um_intervalo(grupo, step):
	print('--------------------------------------------------')
	x = 0
	while (x <= 2):
		pertinencia = calcula_pertinencia(grupo, x)
		print("Valor " + str(x) + " tem pertinência igual a: " + str(pertinencia))
		x = x + float(step)
	print('--------------------------------------------------\n')


def calcula_suporte(conjunto):
	return "]" + str(conjunto['a']) + ", " + str(conjunto['b']) + "["


def calcula_nucleo(conjunto):
	return "[" + str(conjunto['m']) + ", " + str(conjunto['n']) + "]"


def calcula_altura(conjunto):
	return calcula_pertinencia(conjunto, conjunto['m'])


def calcula_alfa_corte(conjunto, alfa_corte):
	conjunto_alfa_corte = []
	x = 0
	while x <= 2.0:
		pertinencia = calcula_pertinencia(conjunto, x)
		if pertinencia >= float(alfa_corte):
			valor = round(x, 2)
			conjunto_alfa_corte.append(valor)
		x = x + 0.01

	return "[" + str(conjunto_alfa_corte[0]) + ", " + str(conjunto_alfa_corte[-1]) + "]"


def calcula_cardinalidade(conjunto):
	cardinalidade = 0
	x = 0
	while(x <= 2):
		pertinencia = calcula_pertinencia(conjunto, x)
		cardinalidade = cardinalidade + pertinencia
		x = x + 0.01

	return cardinalidade


def calcula_soma_max(conjunto_a, conjunto_b):
	soma = 0
	x = 0
	while(x <= 2):
		pertinencia_a = calcula_pertinencia(conjunto_a, x)
		pertinencia_b = calcula_pertinencia(conjunto_b, x)
		soma = soma + max(0, pertinencia_a - pertinencia_b)
		x = x + 0.01

	return soma


def calcula_grau_de_inclusao(conjunto_a, conjunto_b):
	cardinalidade_a = calcula_cardinalidade(conjunto_a)
	valor = calcula_soma_max(conjunto_a, conjunto_b)

	grau_de_inclusao = (1*(cardinalidade_a - valor)) / cardinalidade_a

	return round(grau_de_inclusao, 2)
